import sys
def min_set_size(num,k):
    if num<k or k<0 or k>9:
        return -1
    set_size = round((num-k)/ 10 + (1 if (num-k)%10!=0 else 0))
    return set_size-1

def main():

        num=int(input())
        k_input=sys.stdin.readline().strip()
        if not k_input:
            print("-1")
            return-1
        k = int(k_input)    
        
        result = min_set_size(num,k)
        if result ==-1 or result is None:
            print("-1")
        else:
            print(result-1)
    
if __name__ =="__main__":
    main()