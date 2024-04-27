def getMinimumDeletion(s:str,i:int,j:int)->int:
    if i>=j:
        return 0
    if (s[i]==s[j]):
        return getMinimumDeletion(s,i+1,j-1)
    
    return (1+min( getMinimumDeletion(s,i+1,j),getMinimumDeletion(s,i,j-1) ))

if __name__ == "__main__":
    s= "geeksforgeeks"
    print(getMinimumDeletion(s,0,len(s)-1))
