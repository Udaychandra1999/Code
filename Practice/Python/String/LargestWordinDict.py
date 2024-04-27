"""Input : dict = {"ale", "apple", "monkey", "plea"}   
        str = "abpcplea"  
Output : apple 

Input  : dict = {"pintu", "geeksfor", "geeksgeeks", 
                                        " forgeek"} 
         str = "geeksforgeeks"
Output : geeksgeeks"""

def getLargestWord(d:dict,s:str)->str:
    res=''
    for i in d:
        flag =1
        for j in i:
            if j not in s:
                flag =0
        if flag ==1:
            if len(res)<len(i):
                res =i
    return res

if __name__ =="__main__":
    dict1 = ["ale", "apple", "monkey", "plea"];
    str1 = "abpcplea" ;
    print(getLargestWord(dict1,str1))