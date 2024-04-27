#delete N nodes after M nodes of a linked list
from typing import Optional
from linkedlist import LinkedList,Node

def deleteNafterM(head:Optional[Node],n:int,m:int)->Optional[Node]:
    temp = head
    count =0
    while(temp):
        count+=1
        temp = temp.next
    if m>count:
        print(f"Given m:{m} is greater than list size:{count}")
        return head
    if m == count:
        print(f"There is nothing to remove after m:{m}")
        return head
    temp = head
    for i in range(m-1):
        temp = temp.next
    if n>=count-m:
        temp.next = None
        return head
    ptr = temp
    for i in range(n):
        ptr=ptr.next
    temp.next = ptr.next
    return head

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.append(3)
    li.append(5)
    li.append(6)
    li.display()
    m,n = 2,2 #remove 2 nodes after 2 nodes
    li.head = deleteNafterM(li.head,n,m)
    li.display()
