# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 단어의 길이가 길수록 앞에 배치
# 3. 사전순으로 앞에 있을 때 앞에 배치

N, M = map(int, input().split())
dic = {}

for i in range(N):
    word = input()

    if len(word) < M:
        pass
    else:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

sorted_dic = sorted(dic.items(), key = lambda item:(-item[1], -len(item[0]), item[0]))

for i in sorted_dic:
    print(i[0])