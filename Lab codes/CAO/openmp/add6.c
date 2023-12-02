#include<stdio.h>
#include<omp.h>

void main()
{
    int a[5] = {1};
    int b[5] = {1,2,3,4,5};
    int c[5];
    int tid;
    // change the threads for other array addition in digital assessment
    #pragma omp parallel num_threads(6)
    {
        tid = omp_get_thread_num();
        c[tid] = a[tid] + b[tid];
        printf("c[%d] = %d\n",tid,c[tid]);
    }
}