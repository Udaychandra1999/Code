def can_transform(start: str, end: str) -> bool:
    if len(start) != len(end):
        return "false"

    if start.replace('X', '') != end.replace('X', ''):
        return "false"

    n = len(start)
    Lstart = [i for i in range(n) if start[i] == 'L']
    Lend = [i for i in range(n) if end[i] == 'L']

    Rstart = [i for i in range(n) if start[i] == 'R']
    Rend = [i for i in range(n) if end[i] == 'R']

    for i, j in zip(Lstart, Lend):
        if i < j:
            return "false"

    # check R positions are correct
    for i, j in zip(Rstart, Rend):
        if i > j:
            return "false"

    return "true"
    
a  = input()
b = input()
result = can_transform(a,b)
print(result)