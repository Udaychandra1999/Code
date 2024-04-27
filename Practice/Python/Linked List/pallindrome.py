from typing import Optional
from linkedlist import LinkedList,Node

def checkPallindrome(head:Optional[Node])->bool:
    middle = middleOfList(head=head)
    ptr = head
    while(ptr.next != middle):
        ptr = ptr.next
    middle = reverse(middle)
    temp = head
    while(middle):
        if temp.data == middle.data:
            temp = temp.next
            middle = middle.next
        else:
            return False
    return True

def reverse(head:Optional[Node])->Optional[Node]:
    prev = None
    current = head
    while(current):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head

def middleOfList(head: Optional[Node])->Optional[Node]:
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr
if __name__ == "__main__":
    s = input("Enter a string:")
    li = LinkedList()
    for i in s:
        li.append(i)
    if(checkPallindrome(li.head)):
        print(f"Pallindrome")
    else:
        print("Not a pallindrome")