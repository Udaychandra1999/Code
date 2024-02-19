#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#define MAX_SIZE 100

int isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' ||  ch =='^');
}


int precedence(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    if(op == '^')
        return 3;
    return 0; 
}

void infixToPostfix(char infix[], char postfix[]) {
    int i, j;
    char stack[MAX_SIZE];
    int top = -1; 

    for (i = 0, j = 0; infix[i] != '\0'; i++) {
        char ch = infix[i];

        if (isalnum(ch)) {
            postfix[j++] = ch; 
        } else if (ch == '(') {
            stack[++top] = ch; 
        } else if (ch == ')') {
        
            while (top >= 0 && stack[top] != '(') {
                postfix[j++] = stack[top--];
            }
            if (top >= 0 && stack[top] == '(') {
                top--; // Pop '(' from the stack (discard it)
            }
        } else if (isOperator(ch)) {

            while (top >= 0 && precedence(stack[top]) > precedence(ch)) {
                postfix[j++] = stack[top--];
            }
            stack[++top] = ch; 
        }
    }


    while (top >= 0) {
        postfix[j++] = stack[top--];
    }

    postfix[j] = '\0'; 
}

int main() {
    char infix[100];
    char postfix[100];
    int i;
    scanf("%s", infix);

    infixToPostfix(infix, postfix);

    int length = strlen(postfix);
    for(i=0;i<length;i++)
    {
        printf("%c ",postfix[i]);
    }    

    return 0;
}
