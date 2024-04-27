from bisect import bisect_left

def fibonacciSearch(arr:list,key:int,n:int)->int:
    fibm2 = 0
    fibm1 = 1
    fibm = fibm2+fibm1

    while(fibm<n):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1+fibm2

    offset = -1

    while(fibm>1):
        i = min(offset+fibm2,n-1)

        if(arr[i] <key):
            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm-fibm1

        elif arr[i]>key:
            fibm = fibm2 
            fibm1 = fibm1-fibm2
            fibm2 = fibm - fibm1

        else:
            return i
        
    if(fibm1 and arr[n-1] ==  key):
        return n-1
    
    return -1

if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 
       80, 82, 85, 90, 100,235] 
    n = len(arr) 
    x = 235
    ind = fibonacciSearch(arr, x, n) 
    if ind>=0: 
        print("Found at index:",ind) 
    else: 
        print(x,"isn't present in the array"); 