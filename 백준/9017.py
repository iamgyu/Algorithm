T = int(input()) # 테스트 케이스 갯수

for i in range(T):
    N = int(input()) # 데이터 갯수
    num_input = list(map(int, input().split())) # 팀 번호 입력
    count_member = [0 for i in range(201)] # 1~200번 팀 멤버 카운트를 위한 리스트
    team_completion = list() # 멤버가 6명이 확정된 팀 리스트

    for i in num_input:
        count_member[i] += 1
    
    for i in range(len(count_member)):
        if count_member[i] == 6:
            team_completion.append(i)

    num_input = [i for i in num_input if i in team_completion] # input에서 6명 확정된 팀만 남도록 조정
    team_rank = {} # 각 팀 선수들 점수 딕셔너리

    for i in range(len(num_input)):
        if num_input[i] not in team_rank:
            team_rank[num_input[i]] = []
        team_rank[num_input[i]].append(i + 1)
    

    answer, min_score = -1, float('inf')
    
    for i in team_rank:
        score_sum = sum(team_rank[i][:4])

        if score_sum < min_score:
            min_score = score_sum
            answer = i

        if score_sum == min_score:
            if team_rank[answer][4] > team_rank[i][4]:
                answer = i

    print(answer)