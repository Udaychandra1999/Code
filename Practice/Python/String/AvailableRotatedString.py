def isAvailableRotated(s1:str,s2:str)->bool:
    if s2 in s1+s1:
        return True
    else:
        return False
    
if __name__ == "__main__":
    s1 = "amazon"
    s2 = "azonam"
    if(isAvailableRotated(s1,s2)):
        print("Yes")
    else:
        print("No")