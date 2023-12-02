#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
// This code is to add some random numbers to check the time taken in both sequential and parallel time execution

int main()
{
    int a, b;
    int sadd = 0, padd = 0;
    printf("Sequential time execution:\n");
    double st1, st2;
    st1 = omp_get_wtime();
    for (int i = 0; i < 1000000000; i++)
    {
        a = 1;
        sadd += a;
    }
    st2 = omp_get_wtime();
    printf("Serial time sum = %d and execution time %lf\n", sadd, st2 - st1);
    printf("Parallel time execution:\n");
    double pt1, pt2;
    pt1 = omp_get_wtime();
#pragma omp parallel for reduction(+ : padd)
        for (int i = 0; i < 1000000000; i++)
        {
            a = 1;
            padd += a;
        }
    pt2 = omp_get_wtime();
    printf("Parallel time sum = %d and execution time %lf\n", padd, pt2 - pt1);
    return 0;
}