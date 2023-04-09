def solution(array):
    arr = [0] * (max(array) + 1)
    for i in array:
        arr[i] += 1
    
    a = 0
    for i in arr:
        if i == max(arr):
            a += 1
    
    if a > 1:
        return -1
    else:
        return arr.index(max(arr))