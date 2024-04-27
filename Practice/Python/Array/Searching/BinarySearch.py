#In this case the list(array) should be in sorted order


def binarySearch(arr:list,low:int,high:int,key:int)->int:
    if(low<=high):
        mid = (low+high)//2
        if (arr[mid] == key):
            return mid
        elif arr[mid]>key:
            return binarySearch(arr,low,mid-1,key)
        else:
            return binarySearch(arr,mid+1,high,key=key)
    else:
        return -1
if __name__ == "__main__":
    arr=[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    key = 23
    res = binarySearch(arr,0,len(arr),key)
    if (res!=-1):
        print(f"The value:{key} found at index:{res}")
    else:
        print("The value not found")