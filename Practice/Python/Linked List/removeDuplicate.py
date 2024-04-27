from typing import Optional
from linkedlist import LinkedList,Node

def removeDuplicate(head:Optional[Node])->Optional[Node]:
    ptr = head
    l=[]
    while(ptr):
        if ptr.data not in l:
            l.append(ptr.data)
        ptr = ptr.next
    ptr= head
    for i in range(len(l)-1):
        ptr.data = l[i]
        ptr = ptr.next
    ptr.data = l[len(l)-1]
    ptr.next = None
    
    return head


if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.append(3)
    li.append(5)
    li.append(6)
    li.display()
    li.head = removeDuplicate(li.head)
    li.display()

