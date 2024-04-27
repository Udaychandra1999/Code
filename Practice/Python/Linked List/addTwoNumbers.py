from typing import Optional
from linkedlist import LinkedList,Node

def addTwoNumbers(head1:Optional[Node],head2:Optional[Node])->Optional[Node]:
    one = reverse(head1)
    two = reverse(head2)
    sres =0
    carry =0
    res = None
    prev = None
    while one or two:
        sres = carry + (one.data if one else 0)+(two.data if two else 0)
        carry = sres//10
        sres = sres%10
        temp = Node(sres)
        if res is None:
            res = temp
        else:
            prev.next = temp
        prev = temp

        if one:
            one = one.next
        if two:
            two = two.next
        
        if carry>0:
            temp.next = Node(carry)
        ans = reverse(res)
        return ans

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


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    la = LinkedList()
    lb = LinkedList()
    for i in str(a):
        la.append(int(i))
    for i in str(b):
        lb.append(int(i))
    lc = LinkedList()
    lc.head = addTwoNumbers(la.head,lb.head)
    lc.display()