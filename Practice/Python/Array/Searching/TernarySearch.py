import math

def ternarySearch(l:int,r:int,key:int,ar:list):
    if(r>=l):
        mid1 = l+(r-l)//3
        mid2 = r-(r-l)//3

        if(ar[mid1]==key):
            return mid1
        if(ar[mid2] == key):
            return mid2
        
        if(key<ar[mid1]):
            return ternarySearch(l,mid1-1,key,ar)
        
        if(key>ar[mid2]):
            return ternarySearch(mid2+1,r,key,ar)
        
        else:
            return ternarySearch(mid1+1,mid2-1,key,ar)
        
    return -1

if __name__ == "__main__":
    l,r,k = 0,9,5
    ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    p = ternarySearch(l,r,k,ar)
    print(f"Index of {k}:{p}")
