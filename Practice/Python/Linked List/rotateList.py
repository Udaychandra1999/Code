"""Input: linked list = 10->20->30->40->50->60, k = 4
Output: 50->60->10->20->30->40. 
Explanation: k is smaller than the count of nodes in a linked list so (k+1 )th node i.e. 50 becomes the head node and 60’s next points to 10

Input: linked list = 30->40->50->60, k = 2
Output: 50->60->30->40."""

from linkedlist import LinkedList,Node
from typing import Optional
def rotate(head:Optional[Node],k:int)->Optional[Node]:
        if k ==0:
            return head
        current = head
        count =1
        while(count<k and current is not None):
            current = current.next
            count+=1
        if current is None:
            return
        kthNode = current
        while(current.next):
            current = current.next
        current.next = head
        head = kthNode.next
        kthNode.next = None
        return head

if __name__ == "__main__":
    li = LinkedList()
    for i in range(6):
        li.append(i)
    li.display()
    li.head = rotate(li.head,4)
    li.display()