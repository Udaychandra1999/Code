from linkedlist import Node

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self)->bool:
        return self.front == None
    
    def enQueue(self,item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
    
    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if(self.front==None):
            self.rear = None
    
    def display(self):
        if self.isEmpty():
            print(f"The queue is empty")
        temp = self.front
        while(temp != self.rear):
            print(f"{temp.data}",end=" ")
            temp= temp.next
        print(temp.data)

if __name__ == '__main__':
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)
    q.deQueue()
    q.deQueue()
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    q.deQueue()
    q.display()