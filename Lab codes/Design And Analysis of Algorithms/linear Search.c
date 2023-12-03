#include<stdio.h>
int main()
{
    int n,i,key;
    int a[10];
    printf("Enter the size of the array:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    printf("Enter the element to search:");
    scanf("%d",&key);
    for(i=0;i<n;i++)
    {
        if(a[i] == key)
        {
            printf("The element %d found at %d",key,i);
            break;
        }
    }
}