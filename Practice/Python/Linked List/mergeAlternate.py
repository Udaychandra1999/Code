from typing import Optional
from linkedlist import LinkedList,Node

def mergeAlternate(head1:Optional[Node],head2:Optional[Node])->Optional[Node]:
    temp = LinkedList()
    while(head1 and head2):
        temp.append(head1.data)
        temp.append(head2.data)
        head1 = head1.next
        head2 = head2.next
    while(head1):
        temp.append(head1.data)
        head1 = head1.next
    while(head2):
        temp.append(head2.data)
        head2 = head2.next
    return temp

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.display()
    li2 = LinkedList()
    for i in range(55,66):
        li2.append(i)
    li2.display()
    li3 = mergeAlternate(li.head,li2.head)
    li3.display()