// importing libs
#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

// node declaration
struct node
{
    int data;
    struct node *link;
}*header,*ptr,*newnode,*ptr1;

// insertion at begin
void insertatBegin(int data)
{
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = data;
    if(header == NULL)
        newnode->link = NULL;
    else
        newnode->link = header;
    header = newnode;
}

// insertion at end

void insertatLast(int data)
{
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = data;
    newnode->link = NULL;
    if(header == NULL)
        header = newnode;
    else
    {
        ptr = header;
        while(ptr->link!=NULL)
            ptr = ptr->link;
        ptr->link = newnode;
    }
    
}

//insertion at position

void insertatPosition(int data,int pos)
{
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = data;
    ptr = header;
    for(int i=1;i<pos-1;i++)
    {
        ptr = ptr->link;
    }
    newnode->link = ptr->link;
    ptr->link = newnode;
}

// deletion at beginning

void deleteatStart()
{
    if(header == NULL)
        printf("\nList is empty");
    else
    {
        ptr = header;
        header =header->link;
        free(ptr);
    }
}

// deletion at the end

void deleteatEnd()
{
    if(header == NULL)
    {
        printf("\nList is empty");
    }
    ptr = header;
    while(ptr->link!= NULL)
    {
        ptr1 = ptr;
        ptr = ptr->link;
    }
    ptr1->link = NULL;
    free(ptr);
}

// deletion at a position

void deleteatPosition(int pos)
{
    ptr =header;
    for(int i =0;i<pos;i++)
    {
        ptr1 = ptr;
        ptr = ptr->link;
    }
    ptr1->link= ptr->link;
    free(ptr);

}

void display()
{
    if(header == NULL)
    {
        printf("\nList is empty");
    }
    else
    {
        ptr = header;
        while(ptr!=NULL)
        {
            printf("%d ",ptr->data);
            ptr = ptr->link;
        }
    }
    printf("\n");
}

void search(int key)
{
    int i =0;
    ptr = header;
    while(ptr!=NULL)
    {
        i++;
        if(ptr->data == key)
        {
            printf("Item %d is found at location: %d\n",key,i);
            break;
        }
        ptr = ptr->link;
    }

}

int main()
{
    header = NULL;
    int i,x;
    int a[]={2,9,10,5,6,3,1};
    int n = sizeof(a)/sizeof(a[0]);
    for(i=0;i<n;i++)
        insertatLast(a[i]);
    display();
    insertatLast(11);
    display();
    insertatBegin(12);
    display();
    insertatPosition(14,4);
    display();
    search(10);
    deleteatPosition(2);
    display();
    return 0;
}