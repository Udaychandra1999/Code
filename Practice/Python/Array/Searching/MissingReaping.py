"""Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 2 is missing and 3 occurs twice 

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1"""

def getMissingReapting(arr:list):
    temp = [0] *len(arr)
    repeating_number = missing_number = -1
    snum =0
    for i in arr:
        snum+=i
        temp[i-1]+=1
        if temp[i-1]>1:
            repeating_number = i
    n = len(arr)
    missing_number = (n*(n+1)//2) -snum+repeating_number
    print(repeating_number,missing_number)
    

if __name__ == "__main__":
    arr = [4, 3, 6, 2, 1, 1]
    getMissingReapting(arr)