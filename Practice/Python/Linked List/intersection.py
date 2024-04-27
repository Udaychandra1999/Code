from typing import Optional
from linkedlist import LinkedList,Node

def intersection(head1:Optional[Node],head2:Optional[Node])->Optional[Node]:
    while(head2):
        temp = head1
        while(temp):
            if temp ==head2:
                return head2
            temp = temp.next
        head2 = head2.next

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l1.head = Node(10)
    l2.head = Node(3)
    l2.head.next = Node(6)
    l2.head.next.next = Node(9)
    l1.head.next =l2.head.next.next.next = Node(15)
    l1.head.next.next =l2.head.next.next.next.next = Node(30)

    point = intersection(l1.head,l2.head)
    if point:
        print(point.data)
    else:
        print("NO intersection point")