def isValidIP(s:str)->bool:
    try:
        l = s.split('.')
        if len(l)!=4:
            return False
        for i in l:
            if i.isdigit() and int(i)<256 and int(i)>=0:
                pass
            else:
                return False

    except:
        return False
    return True

if __name__ == "__main__":
    s = "125.512.100.1"
    if (isValidIP(s)):
        print("Valid IP")
    else:
        print("Not a valid IP")