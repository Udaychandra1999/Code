def max_pattern_occurences(text,pattern):
    max_occurences=0
    for i in range(len(text)+1):
        for j in range(2):
            modified_text=text[:i]+pattern[j]+text[i:]
            occurences = count_subsequence_occurences(modified_text,pattern)
            max_occurences = max(max_occurences,occurences)
    return max_occurences
def count_subsequence_occurences(text,pattern):
    dp=[0]*(len(pattern)+1)
    dp[0]=1
    for char in text:
        for i in range(len(pattern)-1,-1,-1):
            if char==pattern[i]:
                dp[i+1]+=dp[i]
    return dp[len(pattern)]
text=input()
pattern=input()
result=max_pattern_occurences(text,pattern)
print(result)