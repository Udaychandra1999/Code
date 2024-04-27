#This search is specifically to avoid out of bound comparisions
def sentinelLinearSearch(arr:list,n:int,key:int):
    last = arr[n-1]
    arr[n-1] = key
    i=0
    while(arr[i] != key):
        i+=1

    arr[n-1] = last

    if((i<n-1) or (arr[n-1]==key)):
        print(f"{key} is present at index:{i}")
    else:
        print("Element not found")

if __name__ == "__main__":
    arr = [10, 20, 180, 30, 60, 50, 110, 100, 70]
    n = len(arr)
    key = 180
    sentinelLinearSearch(arr,n,key)
