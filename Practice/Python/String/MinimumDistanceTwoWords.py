"""Input: S = { “the”, “quick”, “brown”, “fox”, “quick”}, word1 = “the”, word2 = “fox”
Output: 3
Explanation: Minimum distance between the words “the” and “fox” is 3

Input: S = {“geeks”, “for”, “geeks”, “contribute”,  “practice”}, word1 = “geeks”, word2 = “practice”
Output: 2
Explanation: Minimum distance between the words “geeks” and “practice” is 2"""

def getMinimumDistance(l:list,word1:str,word2:str)->int:
    dist = len(l)
    idx=jdx = len(l)
    for i in range(len(l)):
        if l[i] == word1:
            idx =i
        if l[i] == word2:
            jdx = i
        if dist>(abs(idx-jdx)):
            dist  = abs(idx-jdx)
    return dist

if __name__ == "__main__":
    s = ["the","quick","brown","fox","quick"]
    word1 = "the"
    word2 = "fox"

    print(getMinimumDistance(s,word1=word1,word2=word2))
    s2 = ["geeks","for","geeks","contribute","practice"]
    word1="geeks"
    word2="practice"
    print(getMinimumDistance(s2,word1=word1,word2=word2))