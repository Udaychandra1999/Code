from BinarySearch import binarySearch
def exponentialSearch(arr:list,high:int,key:int)->int:
    if arr[0] == key:
        return 0
    
    i =1

    while(i<n and arr[i]<=key):
        i=i*2

    return binarySearch(arr,i//2,min(i,n-1),key)


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 10
    result = exponentialSearch(arr, n, x)
    if result == -1:
        print ("Element not found in the array")
    else:
        print ("Element is present at index %d" %(result))