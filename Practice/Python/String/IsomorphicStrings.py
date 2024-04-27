"""Input:  str1 = “aab”, str2 = “xxy”
Output: True
Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.

Input:  str1 = “aab”, str2 = “xyz”
Output: False
Explanation: One occurrence of ‘a’ in str1 has ‘x’ in str2 and other occurrence of ‘a’ has ‘y’"""
def isIsomorphicString(s1:str,s2:str)->bool:
    if len(s1)!=len(s2):
        return False
    else:
        d = dict()
        for i in range(len(s1)):
            if s1[i] not in d.keys() and s2[i] not in d.values():
                d[s1[i]]=s2[i]
            elif d[s1[i]]!=s2[i]:
                return False
            
    return True

if __name__ == "__main__":
    s1 = "aab"
    s2 = "xyz"

    if(isIsomorphicString(s1,s2)):
        print("Isomorphic")
    else:
        print("Not Isomorphic")
    