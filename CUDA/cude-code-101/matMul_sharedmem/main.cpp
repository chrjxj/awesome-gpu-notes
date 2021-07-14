// Include C++ header files.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

// Include local CUDA header files.
#include "include/matMul.cuh"

 
static Matrix createMatrix(int height_, int width_)
{
  Matrix A;
  A.height = height_;
  A.width = width_;

  A.elements = (float*) malloc(sizeof(*A.elements) * width_ * height_);
  for (int row = 0; row < height_; row++)
    for (int col = 0; col < width_; col++)
      A.elements[row * width_ + col] = 1.0f; /* row * 10.0 + col; */ 
  return A;
}
 
static void printMatrix (Matrix A, char *name)
{
  printf("Matrix sharp: %d x %d, name: %s\n", A.width, A.height, name);
  for (int row = 0; row < A.height; row++) {
    if (row < 8 || (A.height - row) < 8) {
        printf("row %d: [ ", row);
        for (int col = 0; col < A.width; col++) {
            if (col < 8 || (A.width - col) < 8)
                printf ("%f, ", A.elements[row * A.width + col]);
        }
        printf("]\n");
    }
  }
}
 
// Multiply an m*n matrix with an n*p matrix results in an m*p matrix.
// Usage: tx_cuda_matmul [ m [ n [ p ] ] ]
// m, n, and p default to 1, and are multiplied by BLOCK_SIZE.
int main(int argc, char **argv)
{
//  cudaSetDevice(0);
  const int m = (argc > 1 ? atoi(argv[1]) : 1);
  const int n = (argc > 2 ? atoi(argv[2]) : 1);
  const int p = (argc > 3 ? atoi(argv[3]) : 1);
  Matrix A = createMatrix(m, n);
  Matrix B = createMatrix(n, p);
  Matrix C = createMatrix(m, p);
  MatMul(A, B, C);
  printMatrix(A, "A");
  printMatrix(B, "B");
  printMatrix(C, "C");
  return 0;
}
