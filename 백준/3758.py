T = int(input()) # 테스트 데이터의 수
answer_list = []

for num in range(T):

    n, k, t, m = map(int, input().split()) # n: 팀의 개수, k: 문제의 개수, t: 나의 팀 ID, m: 로그 엔트리의 개수

    teamScore = [[0 for i in range(k)] for j in range(n)] # 팀별 문제 점수를 담는 배열
    countSubmit = [0 for i in range(n)] # 팀별 제출 횟수를 담는 배열
    submitTimer = [0 for i in range(m)] # 엔트리별 제출 팀을 담는 배열

    for num in range(m):
        i, j, s = map(int, input().split()) # i: 팀 ID, j: 문제 번호, s: 획득 점수

        if s > teamScore[i - 1][j - 1]:
            teamScore[i - 1][j - 1] = s
        
        countSubmit[i - 1] += 1
        submitTimer[num] = i

    score = sum(teamScore[t - 1]) # 나의 팀 총 점수
    answer = 1  # 등수
    for num in range(n):
        if score < sum(teamScore[num]): # 나의 팀보다 총 점수가 높은 경우
            answer += 1
        elif score == sum(teamScore[num]) and num != (t - 1): # 나의 팀과 총 점수가 같으면서 나의 팀이 아닌 경우
            if countSubmit[t - 1] > countSubmit[num]:
                answer += 1
            elif countSubmit[t - 1] == countSubmit[num]:
                for num2 in range(m - 1, -1, -1):
                    if submitTimer[num2] == t or submitTimer[num2] == num + 1:
                        if submitTimer[num2] == t:
                            answer += 1
                            break
                        else:
                            break

    answer_list.append(answer)

for num in range(T):
    print(answer_list[num])