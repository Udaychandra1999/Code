from linkedlist import LinkedList,Node
from typing import Optional


def middleOfList(head: Optional[Node]):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data



li = LinkedList()
for i in range(1,6):
    li.append(i)
li.display()
print(middleOfList(li.head))

