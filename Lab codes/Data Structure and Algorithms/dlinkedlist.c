#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

struct node
{
    int data;
    struct node *prev;
    struct node *next;
} *header, *newnode, *ptr, *ptr1,*ptr2;

int insertAtBegin(int data)
{
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = data;
    if (header == NULL)

        newnode->next = NULL;

    else
    {
        newnode->next = header;
        header->prev = newnode;
    }
    newnode->prev = NULL;
    header = newnode;
}

void insertAtEnd(int data)
{
    newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data = data;
    if (header == NULL)
    {
        newnode->prev = NULL;
        header = newnode;
    }
    else
    {
        ptr = header;
        while (ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = newnode;
        newnode->prev = ptr;
    }
    newnode->next = NULL;
}

void insertAtPosition(int data, int pos)
{
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = data;
    ptr = header;
    for(int i =1;i<pos;i++)
        ptr = ptr->next;
    ptr1 = ptr->next;
    newnode->next = ptr1;
    ptr1->prev = newnode;
    newnode->prev = ptr;
    ptr->next = newnode;
    
}

void deleteAtBegin()
{
    if(header == NULL)
        printf("Doubly linked list is empty\n");
    else
    {
        ptr = header;
        header = header->next;
        header->prev = NULL;
        free(ptr);
    }
}

void deleteAtEnd()
{
    if(header == NULL)
        printf("Doubly linked list is empty\n");
    else
    {
        ptr = header;
        while(ptr->next != NULL)
            ptr = ptr->next;
        ptr1 = ptr->prev;
        ptr1->next = NULL;
        free(ptr);
    }
}
void deleteAtPos(int pos)
{
    if(header == NULL)
        printf("Doubly linked list empty\n");
    else
    {
        ptr = header;
        for(int i=1;i<pos;i++)
            ptr = ptr->next;
        ptr1 = ptr->prev;
        ptr2 = ptr->next; 
        ptr1->next = ptr2;
        ptr2->prev = ptr1;
        free(ptr);
    }   
}
void search(int key)
{
    int i=0;
    for(ptr = header;ptr!=NULL;ptr = ptr->next)
    {
        i++;
        if(ptr->data == key)
            {
                printf("Item %d Found in position:%d\n", key,i);
                break;
            }
    }
}
void display()
{
    for(ptr = header;ptr!=NULL;ptr = ptr->next)
        printf("%d ",ptr->data);
    printf("\n");
}
int main()
{
    header = NULL;
    int x;
    for(int i=0;i<7;i++)
    {
        scanf("%d",&x);
        insertAtEnd(x);
    }
    display();
    insertAtEnd(11);
    display();
    deleteAtEnd();
    insertAtBegin(12);
    display();
    insertAtPosition(14,3);
    search(10);
    deleteAtPos(2);
    display();
    return 0;

}