

"""
https://pytorch.org/blog/accelerating-pytorch-with-cuda-graphs/
"""

import torch
from itertools import chain


def func_case1():

    N, D_in, H, D_out = 640, 4096, 2048, 1024
    model = torch.nn.Sequential(torch.nn.Linear(D_in, H),
                                torch.nn.Dropout(p=0.2),
                                torch.nn.Linear(H, D_out),
                                torch.nn.Dropout(p=0.1)).cuda()
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    # Placeholders used for capture
    static_input = torch.randn(N, D_in, device='cuda')
    static_target = torch.randn(N, D_out, device='cuda')

    # warmup
    # Uses static_input and static_target here for convenience,
    # but in a real setting, because the warmup includes optimizer.step()
    # you must use a few batches of real data.
    s = torch.cuda.Stream()
    s.wait_stream(torch.cuda.current_stream())
    with torch.cuda.stream(s):
        for i in range(3):
            optimizer.zero_grad(set_to_none=True)
            y_pred = model(static_input)
            loss = loss_fn(y_pred, static_target)
            loss.backward()
            optimizer.step()
    torch.cuda.current_stream().wait_stream(s)

    # capture
    g = torch.cuda.CUDAGraph()
    # Sets grads to None before capture, so backward() will create
    # .grad attributes with allocations from the graph's private pool
    optimizer.zero_grad(set_to_none=True)
    with torch.cuda.graph(g):
        static_y_pred = model(static_input)
        static_loss = loss_fn(static_y_pred, static_target)
        static_loss.backward()
        optimizer.step()

    real_inputs = [torch.rand_like(static_input) for _ in range(10)]
    real_targets = [torch.rand_like(static_target) for _ in range(10)]

    for data, target in zip(real_inputs, real_targets):
        # Fills the graph's input memory with new data to compute on
        static_input.copy_(data)
        static_target.copy_(target)
        # replay() includes forward, backward, and step.
        # You don't even need to call optimizer.zero_grad() between iterations
        # because the captured backward refills static .grad tensors in place.
        g.replay()
        # Params have been updated. static_y_pred, static_loss, and .grad
        # attributes hold values from computing on this iteration's data.



def func_case1():

    N, D_in, H, D_out = 640, 4096, 2048, 1024
    model = torch.nn.Sequential(torch.nn.Linear(D_in, H),
                                torch.nn.Dropout(p=0.2),
                                torch.nn.Linear(H, D_out),
                                torch.nn.Dropout(p=0.1)).cuda()
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    # Placeholders used for capture
    static_input = torch.randn(N, D_in, device='cuda')
    static_target = torch.randn(N, D_out, device='cuda')

    # warmup
    # Uses static_input and static_target here for convenience,
    # but in a real setting, because the warmup includes optimizer.step()
    # you must use a few batches of real data.
    s = torch.cuda.Stream()
    s.wait_stream(torch.cuda.current_stream())
    with torch.cuda.stream(s):
        for i in range(3):
            optimizer.zero_grad(set_to_none=True)
            y_pred = model(static_input)
            loss = loss_fn(y_pred, static_target)
            loss.backward()
            optimizer.step()
    torch.cuda.current_stream().wait_stream(s)

    # capture
    g = torch.cuda.CUDAGraph()
    # Sets grads to None before capture, so backward() will create
    # .grad attributes with allocations from the graph's private pool
    optimizer.zero_grad(set_to_none=True)
    with torch.cuda.graph(g):
        static_y_pred = model(static_input)
        static_loss = loss_fn(static_y_pred, static_target)
        static_loss.backward()
        optimizer.step()

    real_inputs = [torch.rand_like(static_input) for _ in range(10)]
    real_targets = [torch.rand_like(static_target) for _ in range(10)]

    for data, target in zip(real_inputs, real_targets):
        # Fills the graph's input memory with new data to compute on
        static_input.copy_(data)
        static_target.copy_(target)
        # replay() includes forward, backward, and step.
        # You don't even need to call optimizer.zero_grad() between iterations
        # because the captured backward refills static .grad tensors in place.
        g.replay()
        # Params have been updated. static_y_pred, static_loss, and .grad
        # attributes hold values from computing on this iteration's data.




def func_case2():


    N, D_in, H, D_out = 640, 4096, 2048, 1024

    module1 = torch.nn.Linear(D_in, H).cuda()
    module2 = torch.nn.Linear(H, D_out).cuda()
    module3 = torch.nn.Linear(H, D_out).cuda()

    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(chain(module1.parameters(),
                                      module2.parameters(),
                                      module3.parameters()),
                                lr=0.1)

    # Sample inputs used for capture
    # requires_grad state of sample inputs must match
    # requires_grad state of real inputs each callable will see.
    x = torch.randn(N, D_in, device='cuda')
    h = torch.randn(N, H, device='cuda', requires_grad=True)

    module1 = torch.cuda.make_graphed_callables(module1, (x,))
    module2 = torch.cuda.make_graphed_callables(module2, (h,))
    module3 = torch.cuda.make_graphed_callables(module3, (h,))

    real_inputs = [torch.rand_like(x) for _ in range(10)]
    real_targets = [torch.randn(N, D_out, device="cuda") for _ in range(10)]

    for data, target in zip(real_inputs, real_targets):
        optimizer.zero_grad(set_to_none=True)

        tmp = module1(data)  # forward ops run as a graph

        if tmp.sum().item() > 0:
            tmp = module2(tmp)  # forward ops run as a graph
        else:
            tmp = module3(tmp)  # forward ops run as a graph

        loss = loss_fn(tmp, target)
        # module2's or module3's (whichever was chosen) backward ops,
        # as well as module1's backward ops, run as graphs
        loss.backward()
        optimizer.step()

if __name__ == '__main__':

    func_case1()
    func_case2()
