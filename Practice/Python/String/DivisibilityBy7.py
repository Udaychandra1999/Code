def checkDivisibleBy7(n:int)->bool:
    if n<0:
        return checkDivisibleBy7(-n)
    if n==0 or n==7:
        return True
    if n<10:
        return False
    return checkDivisibleBy7(n//10 -2*(n-n//10 *10))

if __name__ == "__main__":
    n=47
    if(checkDivisibleBy7(n)):
        print("Divisible")
    else:
        print("Not Divisible:")