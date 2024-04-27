def linearSearch(a:list,k:int)->int:
    for i in range(len(a)):
        if a[i] ==k:
            return i
    return -1

if __name__ == "__main__":
    a=[10, 50, 30, 70, 80, 20, 90, 40]
    k=30
    res = linearSearch(a,k)
    if (res != -1):
        print(f"The value:{k} is found at index:{res}")
    else:
        print(f"The value:{k} is not found")