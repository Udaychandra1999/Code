from typing import Optional
from linkedlist import LinkedList,Node

def deleteLast(head : Optional[Node],x)-> Optional[Node]:
    temp = head
    ptr= None
    while(temp):
        if(temp.data == x):
            ptr = temp
        temp= temp.next

    if(ptr and ptr.next):
        temp = head
        while(temp.next != ptr):
            temp = temp.next

        temp.next = None

    if(ptr and ptr.next):
        ptr.data = ptr.next.data
        temp.next = ptr.next
        ptr.next = ptr.next.next
    return head

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,6):
        li.append(i)
    li.display()
    li.append(67)
    li.append(88)
    li.display()
    li.head = deleteLast(li.head,67)
    li.display()
    
