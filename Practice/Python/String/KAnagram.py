from collections import defaultdict

def areKAnagram(s1:str,s2:str,k:int)->bool:
    if len(s1)!=len(s2):
        return False
    
    count = defaultdict(int)
    for ch in s1:
        count[ch]+=1
    
    for ch in s2:
        if count[ch]>0:
            count[ch]-=1

    diff_count = sum(count.values())

    if diff_count>k:
        return False
    else:
        return True
    
if __name__ == "__main__":
    s1 = "anagram"
    s2 = "grammar"
    k=2
    if areKAnagram(s1,s2,k):
        print("Yes")
    else:
        print("No")