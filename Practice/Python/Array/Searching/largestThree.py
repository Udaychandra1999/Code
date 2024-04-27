def getLargestThree(arr:list):
    first = second = third = -1
    for i in arr:
        if(i>first):
            third = second
            second = first
            first = i
        elif i>second and i!=first:
            third = second
            second = i
        elif i>third and i !=second and i!=first:
            third = i
    print(f"The three largesst numbers are {first},{second},{third}")

if __name__ == "__main__":
    arr =  [12, 13, 1, 10, 34, 11, 34 ]
    getLargestThree(arr)