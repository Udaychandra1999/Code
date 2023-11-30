def find_common_elements(arr1, arr2, arr3):
    result = []
    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    if not result:
        print("No Elements")
    else:
        print(" ".join(map(str, result)))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input( ).split()))
arr3 = list(map(int, input().split()))


find_common_elements(arr1, arr2, arr3)
                                                                                                                            