#include<stdio.h>
#include<stdlib.h>

void insertionSort(int arr[],int n)
{
    for(int i=1;i<n;i++)
    {
        int key =arr[i];
        int j = i-1;
        while(j>=0 && arr[j]>key)
        {
            arr[j+1] = arr[j];
            j++;
        }
        arr[j+1] = key;
    }
}

int main()
{
    int n,i;
    int ar[10];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&ar[i]);
    insertionSort(ar,n);
    for(i=0;i<n;i++)
        printf("%d ",ar[i]);
    printf("\n");
    return 0;
}