#include<stdio.h>

int binarySearch(int a[],int low,int high,int key)
{
    int mid = (low+high)/2;
    if(low>high)
    {
        return -1;
    }
    else{

    if(a[mid] == key)
        return mid;
    else if(a[mid]>key)
        return binarySearch(a,low,mid,key);
    else
        return binarySearch(a,mid+1,high,key); 
    }
}
int main()
{
    int i,key,n;
    int a[10];
    printf("Enter the size of the array:");
    scanf("%d",&n);
    printf("Enter the elements in sorted order:");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    printf("Enter the key to search:");
    scanf("%d",&key);
    int x = binarySearch(a,0,n,key);
    if(x ==-1)
        printf("Element is not found\n");
    else
        printf("Element :%d is found at location : %d",key,x);
    return 0;
}