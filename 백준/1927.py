import heapq;

N = int(input()) # 연산의 개수
heap = []
answer = []

for i in range(N):
    num = int(input()) 
    if num == 0:
        if heap == []:
            answer.append(0)
        else:
            answer.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)

for i in range(len(answer)):
    print(answer[i])