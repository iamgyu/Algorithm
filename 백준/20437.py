T = int(input()) # 게임 수

for i in range(T):
    W = input() # 입력 받은 문자열
    K = int(input()) # 졍수 K

    word_dict = {}

    for char in W:
        word_dict[char] = word_dict.get(char, 0) + 1

    short_length = 10000
    long_length = 0
    check_dict = {}

    for i in range(len(W)):
        if word_dict[W[i]] < K:
            continue

        check_dict[W[i]] = check_dict.get(W[i], []) + [i]

    for k, v in check_dict.items():
        for i in range(len(v) - K + 1):
            short_length = min(short_length, v[i + K - 1] - v[i] + 1)
            long_length = max(long_length, v[i + K - 1] - v[i] + 1)
    
    if short_length != 10000:
        print(short_length, long_length)
    else:
        print(-1)