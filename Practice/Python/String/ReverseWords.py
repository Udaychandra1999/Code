def reverseWords(s:list,start:int,end:int)->list:
    while(start<end):
        s[start] ,s[end] = s[end] ,s[start]
        start+=1
        end-=1

if __name__ == "__main__":
    s = "I like this program very much"
    s = list(s)
    start =0
    while True:
        try:
            end = s.index(' ',start)
            reverseWords(s,start,end-1)
            start = end+1
        except ValueError:
            reverseWords(s,start,len(s)-1)
            break

    s.reverse()

    s = ''.join(s)
    print(s)