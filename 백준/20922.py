N, K = map(int, input().split()) # N: 수열의 길이, K: 허용되는 같은 정수
arr = [0 for i in range(100001)] # 같은 정수의 개수를 세기 위한 리스트
num_list = list(map(int, input().split())) # 입력받은 수열

answer = 0 # 최장 길이 수열 값
left, right = 0, 0

while right < N:
    if arr[num_list[right]] < K:
        arr[num_list[right]] += 1
        right += 1
    else:
        arr[num_list[left]] -= 1
        left += 1
    
    if answer < right - left:
        answer = right - left

print(answer)