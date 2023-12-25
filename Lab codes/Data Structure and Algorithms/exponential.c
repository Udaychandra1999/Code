#include<stdio.h>
#include<stdlib.h>

int min(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;
}
int binarysearch(int arr[],int low,int high,int key)
{
    while(low<=high)
    {
        int mid = (low+high)/2;
        if(arr[mid] == key)
            return mid;
        else if(arr[mid]<key)
            low = mid+1;
        else
            high = mid-1;
    }
    return -1;
}
int exponentialsearch(int arr[],int n,int key)
{
    if(arr[0] == key)
        return 0;
    int i=1;
    while(i<n && arr[i]<=key)
        i=i*2;
    
    return binarysearch(arr,i/2,min(i,n-1),key);
}

int main()
{
    int i,n,key;
    int a[10];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    scanf("%d",&key);
    int res = exponentialsearch(a,n,key);
    if(res ==-1)
        printf("Key not found");
    else
    {
        printf("Element %d found in position %d",key,res+1);
    }
    return 0;
}