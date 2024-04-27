def interpolationSearch(arr:list,low:int,high:int,key:int)->int:
    if(low<=high and key>=arr[0] and key<= arr[high]):
        pos = low + ((high - low)//(arr[high]-arr[low]))*(key-arr[0])

        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            return interpolationSearch(arr,pos+1,high,key)
        if arr[pos] >key:
            return interpolationSearch(arr,low,pos-1,key)
    return -1

if __name__ =="__main__":
    arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    key = 10

    index = interpolationSearch(arr,0,n-1,key)

    if index!= -1:
        print(f"The element:{key} is found at index:{index}")
    else:
        print("Element not found")