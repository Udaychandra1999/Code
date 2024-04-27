from typing import Optional
from linkedlist import LinkedList,Node

def pairwiseSwap(head:Optional[Node])->Optional[Node]:
    ptr = head
    while(ptr and ptr.next):
        temp = ptr.data
        ptr.data = ptr.next.data
        ptr.next.data = temp
        ptr = ptr.next.next
    return head

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.append(3)
    li.append(5)
    li.append(6)
    li.display()
    li.head = pairwiseSwap(li.head)
    li.display()