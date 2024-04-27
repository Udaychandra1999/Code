ls = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
d = {1:"I",4:"IV",5:'V',9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
ls2=[]

def func(no:int,res:str):
    for i in range(0,len(ls)):
        if no in ls:
            res = d[no]
            rem = 0
            break
        if ls[i]<no:
            quo=no//ls[i]
            rem = no%ls[i]
            res = res+d[ls[i]]*quo
            break

    ls2.append(res)
    if rem ==0:
        pass
    else:
        func(rem,"")

if __name__ =="__main__":
    func(3549,"")
    print("".join(ls2))