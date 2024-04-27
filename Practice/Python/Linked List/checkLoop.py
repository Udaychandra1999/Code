from typing import Optional
from linkedlist import LinkedList,Node

def checkLoop(head: Optional[Node])->bool:
    temp = head
    s = set()
    while(temp):
        if temp in s:
            return True
        s.add(temp)
        temp=temp.next

    return False

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.append(3)
    li.append(5)
    li.append(6)
    li.display()
    #creating a loop which follows infinite loop if display fucntion is used
    li.head.next.next.next = li.head
    if(checkLoop(li.head)):
        print("Loop found")
    else:
        print("Loop not found")
