from linkedlist import Node

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self)->bool:
        if self.head:
            return False
        else:
            return True
    
    def push(self,data):
        if self.head==None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            popNode = self.head
            self.head = self.head.next
            return popNode.data
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
        
    def display(self):
        if self.isEmpty():
            print(f"Stack  is empty")
        else:
            ptr = self.head
            while(ptr):
                print(f"{ptr.data}->",end=" ")
                ptr=ptr.next

if __name__ == "__main__":
    stk = Stack()
    for i in range(6):
        stk.push(i)
    stk.display()