from linkedlist import LinkedList,Node
from typing import Optional

def reverse(head:Optional[Node])->Optional[Node]:
    prev = None
    current = head
    while(current):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head


if __name__ =="__main__":
    li = LinkedList()
    for i in range(6):
        li.append(i)
    li.display()
    li.head =reverse(li.head)
    li.display()