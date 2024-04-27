from typing import Optional
from linkedlist import LinkedList,Node

def nthFromLast(head : Optional[Node],n:int) ->str:
    temp = head
    length =0
    while(temp):
        temp = temp.next
        length+=1
    
    if n>length:
        return f"Give length:{n} is greater than the size:{length}"
    temp = head
    for i in range(length-n):
        temp = temp.next
    return temp.data
if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,6):
        li.append(i)
    li.display()
    li.append(67)
    li.append(88)
    li.display()
    print(nthFromLast(li.head,6))