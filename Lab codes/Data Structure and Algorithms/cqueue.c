#include<stdio.h>
int front =-1, rear = -1;
int size,i,data;
int queue[10];

int isempty()
{
    if (front ==-1)
        return 1;
    else
        return 0;
}
int isfull()
{
    if(rear == size -1 && front ==0)
        return 1;
    else
        return 0;
}

void enqueue(int data)
{
    if(isfull())
        printf("Circular Queue is full\n");
    else if(front == -1)
    {
        front =0;
        queue[++rear] =data;
    }
    else if(rear == size -1 && front!=0)
        {
            rear =0;
            queue[rear]=data;
        }
    else
        queue[++rear]=data;
}

void dequeue()
{
    if(isempty())
        printf("Circular Queue is empty\n");
    else
    {
        if(front == rear)
        {
            front =-1;
            rear =-1;
        }
        else if(front == size -1)
            front =0;
        else  
            front++;
    }
}

void display()
{
    if(isempty())
        printf("Circular Queue is empty\n");
    else{
        printf("\n");
        int i;
        if(rear>=front)
        {
            for(i=front;i<=rear;i++)
                printf("%d ",queue[i]);
        }
        else
        {
            for(i=front;i<size;i++)
                printf("%d ",queue[i]);
            for(i=0;i<=rear;i++)
                printf("%d ",queue[i]);
            printf("\n");
        }
    }
}
int main()
{
    display();
    scanf("%d",&size);
    for(int i=0;i<size;i++)
        {
            scanf("%d",&data);
            enqueue(data);
        }
    display();
    for(i=0;i<size;i++)
    {
        dequeue();
        display();       
    }
    return 0;
}