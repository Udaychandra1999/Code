from typing import Optional
from linkedlist import LinkedList,Node

def mergeList(head1:Optional[Node],head2:Optional[Node])->Optional[Node]:
    temp = LinkedList()
    while(head1 and head2):
        if head1.data > head2.data:
            temp.append(head2.data)
            head2 = head2.next
        if head1.data <= head2.data:
            temp.append(head1.data)
            head1 = head1.next
    while(head1):
        temp.append(head1.data)
        head1 = head1.next
    while(head2):
        temp.append(head2.data)
        head2 = head2.next
    return temp.head

if __name__ =="__main__":
    l1 = LinkedList()
    for i in range(0,10,2):
        l1.append(i)
    l1.display()
    l2 = LinkedList()
    for i in range(1,10,2):
        l2.append(i)
    l2.display()
    l3 = LinkedList()
    l3.head = mergeList(l1.head,l2.head)
    l3.display()
