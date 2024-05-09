N, M = map(int, input().split()) # N: 메모장에 적은 키워드 개수, M: 블로그에 쓴 글의 개수

word_list = set() # 메모장에 적은 키워드 저장을 위한 리스트
list_len = [] # 블로그 글 이후 남은 키워드 갯수 저장 리스트

for i in range(N):
    word_list.add(input())

for i in range(M):
    use_word = list(input().split(','))
    
    for c in use_word:
        if c in word_list:
            word_list.remove(c)
    
    list_len.append(len(word_list))

for i in range(M):
    print(list_len[i])