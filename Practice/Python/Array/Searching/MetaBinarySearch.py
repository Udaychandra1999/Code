import math
def metaBinarySearch(arr:list,key:int)->int:
    n = len(arr)
    lg = int(math.log2(n-1))+1

    pos =0
    for i in range(lg-1,-1,-1):
        if arr[pos] == key:
            return pos
        
        new_pos = pos | (1<<i)

        if ((new_pos<n) and (arr[new_pos]<=key)):
            pos = new_pos
    return (pos if arr[pos]==key else -1)

if __name__ == "__main__":
 
    A = [ -2, 10, 100, 250, 32315 ]
    print( metaBinarySearch(A, 10))