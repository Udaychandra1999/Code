def replaceSubString(s:str,s1:str,s2:str)->str:
    return s.replace(s1,s2)


if __name__ == "__main__":
    s = "geeksforgeeks"
    s1 = "eek"
    s2="ok"
    print(replaceSubString(s,s1,s2))
