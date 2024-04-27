from typing import Optional
from linkedlist import LinkedList,Node

def countOccurence(head:Optional[Node])->dict:
    d = dict()
    temp = head
    while(temp):
        if temp.data not in d:
            d[temp.data] = 1
        else:
            d[temp.data]+=1
        temp = temp.next
    return d

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.append(3)
    li.append(5)
    li.append(6)
    li.display()
    print(countOccurence(li.head))