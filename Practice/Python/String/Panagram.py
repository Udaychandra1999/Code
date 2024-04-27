"""
Input: “The quick brown fox jumps over the lazy dog” 
Output: is a Pangram 
Explanation: Contains all the characters from ‘a’ to ‘z’] 

Input: “The quick brown fox jumps over the dog”
Output: is not a Pangram 
Explanation: Doesn’t contain all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing
"""
def checkPanagram(s:str)->bool:
    l =[x.lower() for x in s if x != ' ']
    s =set(l)
    if len(s) == 26:
        return True
    else:
        return False
if __name__ == "__main__":
    s = "The quick brown fox jumps over the lazy dog"
    if checkPanagram(s):
        print("Panagram")
    else:
        print("Not a panagram")