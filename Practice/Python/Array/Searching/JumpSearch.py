import math
def jumpSearch(arr:list,key:int,n:int)->int:
    step = math.sqrt(n)
    prev =0
    while arr[int(min(step,n)-1)]<key:
        prev = step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
        
    while arr[int(prev)]<key:
        prev+=1
        if prev == min(step,n):
            return -1
    if arr[int(prev)] == key:
        return prev
    return -1

if __name__ == "__main__":
    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
    x = 55  
    index = jumpSearch(arr,x,len(arr))
    print(f"Number {x} is at index:{index}")