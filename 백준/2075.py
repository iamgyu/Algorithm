import heapq;
N = int(input()) # N번째 큰 수 찾기
heap = []

for i in range(N):
    temp = list(map(int, input().split()))
    for num in temp:
        if len(heap) != N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])