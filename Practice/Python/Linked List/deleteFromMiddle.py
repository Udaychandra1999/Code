from typing import Optional
from linkedlist import LinkedList,Node

def deleteFromMiddle(head: Optional[Node])-> Optional[Node]:
    slow_ptr = head
    fast_ptr = head
    count =0
    while(fast_ptr and fast_ptr.next):
        count+=1
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    ptr =head
    for i in range(count-1):
        ptr=ptr.next
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
    li.head = deleteFromMiddle(li.head)
    li.display()
    