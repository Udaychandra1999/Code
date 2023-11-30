def sliding_subarray_beauty(arr, k, n):
    result = []
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        subarray.sort()  
        result.append(str(subarray[n-1]))  
    return " ".join(result)

arr_input = input()
arr = list(map(int, arr_input.split()))
k = int(input())
n = int(input())
result = sliding_subarray_beauty(arr, k, n)
print(result)