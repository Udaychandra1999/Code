"""Input: S = “aaaaaaaaaaa”
Output: ba  
Explanation:

First convert the given string to “a11” i.e. write, character along with its frequency.
Then, change “a11” to “ab” because 11 is b in hexadecimal.
Then, finally reverse the string i.e “ba”.
Input: S = “abc”
Output: 1c1b1a"""


def getStringEncrypt(s:str)->str:
    d=dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    res=""
    for i in d.keys():
        res+=i+str(hex(d[i])[2:])
    return res 

if __name__ == "__main__":
    s = "aaaaaaaaaaa"
    print(getStringEncrypt(s))