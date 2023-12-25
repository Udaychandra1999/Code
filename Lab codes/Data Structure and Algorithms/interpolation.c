#include <stdio.h>
#include <stdlib.h>

int interpolation(int arr[], int n, int key)
{
    int low, high;
    low = 0;
    high = n - 1;
    while (low <= high && arr[low] <= key && key <= arr[high])
    {
        int pos = low + (int)((key - arr[low]) * (high - low)) / (arr[high] = arr[low]);
        if (arr[pos] == key)
            return pos;
        else if (arr[pos] < key)
            low = pos + 1;
        else
            high = pos - 1;
    }
    return -1;
}

int main()
{
    int n,i,key,res;
    int arr[10];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);
    scanf("%d",&key);
    res =  interpolation(arr,n,key);
    if(res!=-1)
        printf("Element %d found in position %d",key,res+1);
    else
        printf("Key not found");
    return 0;
}