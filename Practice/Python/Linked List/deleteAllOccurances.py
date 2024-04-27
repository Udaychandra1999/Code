from typing import Optional
from linkedlist import LinkedList,Node

def deleteAllOccurances(head:Optional[Node],n:int)->Optional[Node]:
    while(head.data == n):
        head = head.next
    temp = head
    while(temp and temp.next):
        if(temp.next.data == n):
            temp.next = temp.next.next
        temp = temp.next
    return head


if __name__ == "__main__":
    l=[2,2,1,8,2,3,2,7]
    li = LinkedList()
    for i in l:
        li.append(i)
    li.display()
    li.head = deleteAllOccurances(li.head,2)
    li.display()