#include <stdio.h>

int front = -1, rear = -1;
int queue[10];
void enqueue(int data,int size); // for insertion process
void dequeue();         // for deletion process
void display();         // to display elements
void isfull(int size);
void display()
{
    int i;
    if (front == -1)
    {
        printf("Queue empty");
    }
    else
    {
        printf("\n");
        for (i = front; i <= rear; i++)
            printf("%d ", queue[i]);
    }
}

void enqueue(int data, int size)
{
    if (rear == size - 1)
    {
        printf("\nQueue full");
    }
    else
    {
        if (front == -1)
            front = 0;
        queue[++rear] = data;
    }
}
void isfull(int size)
{
    if (rear == size - 1)
        printf("\nQueue full");
}

void dequeue()
{
    if (front == -1 || front > rear)
    {
        printf("Queue empty");
    }
    else
    {
        front++;
    }
}

int main()
{
    int n, i, data;
    scanf("%d", &n);
    display();
    for (i = 0; i < n; i++)
    {
        scanf("%d", &data);
        enqueue(data, n);
    }
    display();
    isfull(n);
    for (i = 0; i < n; i++)
    {
        dequeue();
        display();
    }
    dequeue();
    return 0;
}