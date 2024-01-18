def solution(array, n):
    arr = []
    array.sort()
    for i in array:
        arr.append(abs(i-n))
    
    answer = array[arr.index(min(arr))]
    
    return answer