n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
start = 1 # 1 - n을 스택에 넣기 위함
i = 0 # arr배열을 검사하기 위함
ans = []

while True:
    if stack and stack[-1] == arr[i]:
        ans.append("-")
        stack.pop()
        i += 1
    else:
        if start > n:
            break     
        stack.append(start)
        ans.append("+")
        start += 1
        
if not stack:
    for i in range(len(ans)):
        print(ans[i])
else:
    print("NO")