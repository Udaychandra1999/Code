#Insertion,deletion,search in sorted array
#arr = [12, 16, 20, 40, 50, 70] 
class SortedArray():
    def __init__(self):
        self.size = 0
        self.arr = list()
    
    def insert(self,x:int):
        if self.size == 0:
            self.size+=1
            self.arr.append(x)
        else:
            self.size+=1
            self.arr.append(0)
            i=0
            while(self.arr[i]<x and i<self.size-1):
                i+=1
            idx = i
            j = self.size-1
            while(j>i):
                self.arr[j] = self.arr[j-1]
                j-=1
            self.arr[idx] = x
    
    def getSize(self)->int:
        return self.size
    
    def display(self):
        print(self.arr[:self.size])
    def search(self,x:int)->int:
        if self.size == 0:
            print("List is empty")
            return -1
        else:
            for i in range(self.size):
                if self.arr[i] == x:
                    return i
            return -1

    def delete(self,key:int):
        idx =self.search(key)
        if idx == -1:
            print("Element Not found")
        else:
            j = idx
            while(j<self.size-1):
                self.arr[j] = self.arr[j+1]
                j+=1
            self.size-=1
            self.arr.remove(self.arr[self.size])

if __name__ == "__main__":
    li = SortedArray()
    li.search(1)
    ar = [12,88,20,16, 50, 40, 70]
    for i in ar:
        li.insert(i)
    li.display()
    li.delete(16)
    li.display()
    idx = li.search(50)
    if(idx == -1):
        print("Not found")
    else:
        print(f"Found at the index:{idx}")



            
