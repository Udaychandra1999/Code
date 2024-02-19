#include<stdio.h>
#include<stdlib.h>
#define max_size 10
int top =-1;
int stack[max_size];
int n;
int isempty()
{
    if (top == -1)
    {
        return 1;
    }
    else
        return 0;
}

int isfull()
{
    if(top == n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void display()
{
    if(isempty())
    {
        printf("Stack is empty\n");
    }
    else
    {
    for(int i=0;i<=top;i++)
        printf("%d ",stack[i]);
    printf("\n");
    }
}

void push(int data)
{
    if(isfull())
        printf("Stack is full\n");
    else
    {
        stack[++top] = data;
    }
}

int pop()
{
    if(isempty())
        printf("Stack is empty\n");
    else
        return stack[top--];

    return -1;
}

int main()
{
    int i,j;
    scanf("%d",&n);
    display();
    for(i=0;i<n;i++)
    {
        scanf("%d",&j);
        push(j);
    }
    display();
    for(i=0;i<n;i++)
    {
        pop();
        display();
    }
    return 0;
}