from typing import Optional
from linkedlist import LinkedList,Node

def sortedIntersection(head1:Optional[Node],head2:Optional[Node])->Optional[Node]:
    temp = LinkedList()
    while(head1 and head2):
        if head1.data == head2.data:
            temp.append(head2.data)
            head2 = head2.next
            head1 = head1.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next
    return temp.head

if __name__ == "__main__":
    a = LinkedList()
    b = LinkedList()
    for i in range(1,16):
        a.append(i)
    for i in range(2,10):
        b.append(i)
    
    a.display()
    b.display()
    c = LinkedList()
    c.head = sortedIntersection(a.head,b.head)
    c.display()

    
