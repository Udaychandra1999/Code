def getMissingNumber(arr:list,n:int)->int:
    s = n*(n+1)//2
    s1 = sum(arr)
    return s-s1


if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    N = len(arr)
    print(getMissingNumber(arr,N+1))
