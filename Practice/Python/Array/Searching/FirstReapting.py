def getFirstReapting(arr:list)->int:
    l=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

if __name__ == "__main__":
    arr = [10, 5, 3, 4, 3, 5, 6]
    print(getFirstReapting(arr))