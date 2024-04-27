def getatoi(s:str)->int:
    try:
        val = int(s)
    except:
        val =0

    return val

if __name__ == "__main__":
    print(getatoi("8"))
    print(getatoi("gk"))