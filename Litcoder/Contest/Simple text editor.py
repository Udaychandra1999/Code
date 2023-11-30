stk =[]
deleted_stack=[]
stack_command=[]
cursor = 0
n = input()
n = n.split(',')
for i in n:
    x = i.split()
    if x[0] == '1':
        stack_command.append(x)
        l = list(x[1])
        stk=stk[0:cursor]+l+stk[cursor:]
        cursor = cursor + len(l)
    elif x[0] == '2':
        stack_command.append(x)
        cursor = cursor - int(x[1])
        deleted_stack.append(stk[cursor])
        stk.remove(stk[cursor])
    elif x[0] == '3':
        i = int(x[1])-1
        print(stk[i])
    elif x[0] == '4':
        command,value = stack_command.pop()
        if command == '1':
            stk = stk[:cursor - len(value)]+stk[cursor:]
            cursor -=len(value)
        elif command =='2':
            stk = stk[:cursor]+deleted_stack.pop()+stk[cursor:]