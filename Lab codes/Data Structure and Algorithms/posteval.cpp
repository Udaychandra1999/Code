#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

int performOperation(int operand1, int operand2, char op) {
    switch (op) {
        case '+':
            return operand1 + operand2;
        case '-':
            return operand1 - operand2;
        case '*':
            return operand1 * operand2;
        case '/':
            if (operand2 != 0) {
                return operand1 / operand2;
            } else {
                cerr << "Error: Division by zero" << endl;
                exit(1);
            }
        case '^':
            return pow(operand1, operand2);
        default:
            cerr << "Error: Invalid operator" << endl;
            exit(1);
    }
}

int evaluatePostfix(string expression) {
    stack<int> operands;
    
    for (char c : expression) {
        if (isdigit(c)) {
            operands.push(c - '0');  // Convert char to int
        } else if (c == ' ') {
            continue;
        } else if (isOperator(c)) {
            int operand2 = operands.top();
            operands.pop();
            int operand1 = operands.top();
            operands.pop();
            int result = performOperation(operand1, operand2, c);
            operands.push(result);
        } else {
            cerr << "Error: Invalid character in expression" << endl;
            exit(1);
        }
    }
    
    if (operands.size() == 1) {
        return operands.top();
    } else {
        cerr << "Error: Invalid postfix expression" << endl;
        exit(1);
    }
}

int main() {
    string postfixExpression;
    getline(cin, postfixExpression);

    int result = evaluatePostfix(postfixExpression);

    cout << result << endl;

    return 0;
}