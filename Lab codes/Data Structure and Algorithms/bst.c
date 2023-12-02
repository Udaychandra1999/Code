#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

// tree declaration

struct node
{
    int key;
    struct node* left;
    struct node* right;
}*root,*newnode,*temp,*succparent,*succ;

struct node* insert(struct node *root,int data)
{
    if(root == NULL)
    {
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->key = data;
    newnode->left = NULL;
    newnode->right = NULL;
        root = newnode;
    }
    else
    {
        if(root->key<data)
        {
            root->right = insert(root->right,data);
        }
        else
            root->left = insert(root->left,data);
    }
    return root;
}
struct node* delelenode(struct node* root, int data)
{
    if(root == NULL)
        return root;
    if(root->key>data)
    {
        root->left = delelenode(root->left,data);
        return root;
    }
    else if(root->key< data)
    {
        root->right = delelenode(root->right,data);
        return root;
    }
    else
    {
        // if one of the chilren is empty
        if(root->left == NULL)
        {
            temp = root->right;
            free(root);
            return temp;
        }
        else if(root->right == NULL)
        {
            temp = root->left;
            free(root);
            return temp;
        }
        else if(root->left == NULL && root->right == NULL)
        {
            free(root);
            return NULL;
        }
        else
        {
            // if the element has both children
            succparent = root;
            succ = root->right;
            while(succ->left!=NULL)
            {
                succparent = succ;
                succ = succ->left;
            }
            if(succparent!= root)
                succparent->left = succ->right;
            else
                succparent->right = succ->right;
            
            root->key = succ->key;
            free(succ);
            return root;
        }
    }
}

void inorderTraversal(struct node *root)
{
    if(root != NULL)
    {
        inorderTraversal(root->left);
        printf("%d ",root->key);
        inorderTraversal(root->right);
    }
}

void preorderTraversal(struct node *root)
{
    if(root != NULL)
    {
        printf("%d ",root->key);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

void postorderTraversal(struct node *root)
{
    if(root != NULL)
    {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        printf("%d ",root->key);
    }
}


int main()
{
    root = NULL;
    int a[] = {5,10,3,2,15,6,4};
    for(int i =0;i<7;i++)
        root = insert(root,a[i]);
    root = insert(root,40);
    root = insert(root,20);
    root = insert(root,30);
    delelenode(root,6);
    inorderTraversal(root);
    printf("\n");
}