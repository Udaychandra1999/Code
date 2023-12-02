#include<stdio.h>

void tower(int n,char source,char auxilliary,char destination)
{
    if(n==1)
    {
        printf("%c -> %c\n",source,destination);
    }
    else
    {
        tower(n-1,source,destination,auxilliary);
        printf("%c -> %c\n",source,destination);
        tower(n-1,auxilliary,source,destination);
    }
}

int main()
{
    tower(3,'a','b','c');
    return 0;
}