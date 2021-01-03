// Include C++ header files.
#include <iostream>

// Include local CUDA header files.
#include "include/vectorAdd.cuh"



/*
int main() {

    int N = 1024;
    float *a, *b, *c;

    a = (float *)malloc(N * sizeof(float));
    b = (float *)malloc(N * sizeof(float));
    c = (float *)malloc(N * sizeof(float));
    memset(c, 0, N  * sizeof(float));
    init_rand_f(a, N);
    init_rand_f(b, N);

    // Sum array elements across ( C[0] = A[0] + B[0] ) into array C using CUDA.
    vectorAdd(A, B, C, 3);

    // Print out result.
    std::cout << "C = " << C[0] << ", " << C[1] << ", " << C[2] << std::endl;

    return 0;
}
*/

int main() {

    // Initialize arrays A, B, and C.
    double A[3], B[3], C[3];

    // Populate arrays A and B.
    A[0] = 1; A[1] = 2; A[2] = 3;
    B[0] = 1; B[1] = 1; B[2] = 1;

    // Sum array elements across ( C[0] = A[0] + B[0] ) into array C using CUDA.
    vectorAdd(A, B, C, 3);

    // Print out result.
    std::cout << "C = " << C[0] << ", " << C[1] << ", " << C[2] << std::endl;

    return 0;

}