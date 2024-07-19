from collections import deque

T = int(input()) # T : 테스트 갯수

for i in range(T):
    N, M = map(int, input().split()) # N : 문서의 개수, M : queue에 몇 번쨰에 놓여있는지
    q = deque(list(map(int, input().split())))
    count = 0

    while q:
        max_value = max(q)
        pop_value = q.popleft()
        M -= 1

        if max_value == pop_value:
            if M < 0:
                print(count + 1)
                break
            else:
                count += 1
        else:
            q.append(pop_value)
            if M < 0:
                M = len(q) - 1