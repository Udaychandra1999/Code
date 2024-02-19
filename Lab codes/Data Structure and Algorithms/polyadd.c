// Polynomial addtition using linked list

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int coeficient;
    int exponent;
    struct node *link;
};

struct node *createnode(int coefficient, int exponent)
{
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode->coeficient = coefficient;
    newnode->exponent = exponent;
    newnode->link = NULL;
    return newnode;
}

void addnode(struct node **poly, int coefficient, int exponent)
{
    struct node *newnode = createnode(coefficient, exponent);
    if (*poly == NULL)
        *poly = newnode;
    else
    {
        struct node *current = *poly;
        while (current->link != NULL)
            current = current->link;
        current->link = newnode;
    }
}

struct node *addpoly(struct node *poly1, struct node *poly2)
{
    struct node *result = NULL;
    while (poly1 != NULL && poly2 != NULL)
    {
        if(poly1->exponent>poly2->exponent)
        {
            addnode(&result,poly1->coeficient,poly1->exponent);
            poly1 = poly1->link;
        }
        else if(poly2->exponent>poly1->exponent)
        {
            addnode(&result,poly2->coeficient,poly2->exponent);
            poly2 = poly2->link;
            
        }
        else
        {

            int sumcoeff = poly1->coeficient+poly2->coeficient;
            if(sumcoeff !=0)
            addnode(&result,sumcoeff,poly1->exponent);
            poly1 = poly1->link;
            poly2 = poly2->link;
        }
    }
    while(poly1!=NULL)
    {
        addnode(&result,poly1->coeficient,poly1->exponent);
        poly1 = poly1->link;
    }
    while(poly2!=NULL)
    {
        addnode(&result,poly2->coeficient,poly2->exponent);
        poly2 - poly2->link;
    }
    return result;
}

void displaypolynomial(struct node *node)
{
    while(node != NULL)
    {
        printf("%d %d\n",node->exponent,node->coeficient);
        node = node->link;
    }
}

int main()
{
    struct node *poly1 = NULL;
    struct node *poly2 = NULL;
    int n1,n2,e,c,i;
    scanf("%d",&n1);
    for(i=0;i<n1;i++)
    {
        scanf("%d%d",&e,&c);
        addnode(&poly1,c,e);
    }
    scanf("%d",&n2);
    for(i=0;i<n2;i++)
    {
        scanf("%d%d",&e,&c);
        addnode(&poly2,c,e);
    }
    struct node *result = addpoly(poly1,poly2);
    printf("\nResult:\n");
    displaypolynomial(result);

    while(poly1!=NULL)
    {
        struct node *temp = poly1;
        poly1 = poly1->link;
        free(temp);
    }
    while(poly2!=NULL)
    {
        struct node *temp = poly2;
        poly2 = poly2->link;
        free(temp);
    }
    return 0;
}