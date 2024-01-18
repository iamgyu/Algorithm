def solution(before, after):
    return 1 if ''.join(sorted(before)) == ''.join(sorted(after)) else 0