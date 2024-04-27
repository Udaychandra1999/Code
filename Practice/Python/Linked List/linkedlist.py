# Linked list definition
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    #insertion statements
    #push for insertion at beginning
    #append for insertion at the end
    #insertAfter for insertion after the position

    #insertion at the beginning
    def push(self,new_data):

        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node
    
    #insertion at the end
    def append(self,new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        ptr = self.head
        while(ptr.next):
            ptr = ptr.next

        ptr.next = new_node

    #insertion after the  position
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next

        prev_node.next = new_node

    #deletion statements
    #beginning
    #End
    #Middle

    #deletion at beginning
    def deleteAtBegin(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            self.head = self.head.next
            del temp
    
    #deletion at the end
    def deleteAtEnd(self):
        ptr = self.head
        while(ptr.next):
            ptr1 = ptr
            ptr=ptr.next
        ptr1.next = None
        del ptr
    
    #deletion at the position
    def deleteAtPos(self,pos:int):
        ptr = self.head
        for i in range(pos):
            ptr1 = ptr
            ptr = ptr.next
        ptr1 = ptr.next
        del ptr

    def display(self):
        ptr = self.head
        while(ptr):
            print(f"{ptr.data}",end=" ")
            ptr = ptr.next
        print()
    
    def search(self,val)->bool:
        ptr = self.head
        while(ptr):
            if(ptr.data==val):
                return True
            ptr=ptr.next
        return False
    
    

if __name__ == "__main__":
    li = LinkedList()
    for i in range(1,5):
        li.append(i)
    li.display()
    if(li.search(4)):
        print("In linked list")
    else:
        print("Not in linked list")
    print(str(li.getMiddle()))



        
        
        

