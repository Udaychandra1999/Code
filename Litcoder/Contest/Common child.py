def doSomething(s1,s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    matrix = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[len_s1][len_s2]
    
s1 = input()
s2 = input()
outputVal = doSomething(s1,s2)
print(outputVal)