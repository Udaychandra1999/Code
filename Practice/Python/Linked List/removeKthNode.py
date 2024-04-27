from typing import Optional
from linkedlist import LinkedList,Node

def removeKthNode(head:Optional[Node],k:int)->Optional[Node]:
    temp = head
    count =0
    while(temp):
        count+=1
        temp=temp.next
    if(count<k):
        print(f"Given k:{k} is more than list size:{count}")
        return head
    temp = head
    for i in range(k-1):
        temp = temp.next
    temp.next = temp.next.next
    return head

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,11):
        li.append(i)
    li.append(3)
    li.append(5)
    li.append(6)
    li.display()
    li.head = removeKthNode(li.head,3)
    li.display()
    