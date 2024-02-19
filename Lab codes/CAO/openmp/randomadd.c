#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define SIZE 1000

int main() {
    int i;
    int sum_serial = 0, sum_parallel = 0;
    int numbers[SIZE];

    // Initialize array with random numbers
    for (i = 0; i < SIZE; i++) {
        numbers[i] = rand() % 100;
    }

    // Serial computation
    double start_time_serial = omp_get_wtime();
    for (i = 0; i < SIZE; i++) {
        sum_serial += numbers[i];
    }
    double end_time_serial = omp_get_wtime();

    printf("Serial sum: %d\n", sum_serial);
    printf("Serial time: %f seconds\n", end_time_serial - start_time_serial);

    // Parallel computation using OpenMP
    int num_threads;
    double start_time_parallel = omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp for reduction(+:sum_parallel)
        for (i = 0; i < SIZE; i++) {
            sum_parallel += numbers[i];
        }

        // Get the number of threads used
        #pragma omp single
        num_threads = omp_get_num_threads();
    }
    double end_time_parallel = omp_get_wtime();

    printf("Parallel sum: %d\n", sum_parallel);
    printf("Parallel time: %f seconds\n", end_time_parallel - start_time_parallel);
    printf("Number of threads: %d\n", num_threads);

    return 0;
}
