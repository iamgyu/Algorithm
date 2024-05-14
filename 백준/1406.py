str_stack = list(input()) # 입력받은 문자열 스택
N = len(str_stack) # 문자열의 길이
M = int(input()) # 명령어의 개수
store_stack = [] # 커서 이동에 따른 문자 저장을 위한 스택

for i in range(M):
    command = list(input().split())

    if command[0] == 'L': # 커서 왼쪽으로 이동 시 기존 스택 pop, 저장 스택 append
        if len(str_stack) == 0:
            continue
        else:
            store_stack.append(str_stack.pop())

    elif command[0] == 'D': # 커서 오른쪽 이동 시 저장 스택 pop, 기존 스택 append
        if len(store_stack) == 0:
            continue
        else:
            str_stack.append(store_stack.pop())

    elif command[0] == 'B': # 커서 왼쪽 문자 삭제 시 기존 스택 pop
        if len(str_stack) == 0:
            continue
        else:
            str_stack.pop()
    
    elif command[0] == 'P': # 새로운 문자 추가 시 기존 스택 append
        str_stack.append(command[1])

for i in range(len(store_stack)): # 커서 이후에 남은 문자 기존 스택에 append
    str_stack.append(store_stack.pop())

print(''.join(str_stack))