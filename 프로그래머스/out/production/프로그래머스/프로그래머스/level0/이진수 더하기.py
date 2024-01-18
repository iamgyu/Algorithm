def solution(bin1, bin2):
    b1 = int(bin1, 2)
    b2 = int(bin2, 2)
    return str(bin(b1 + b2)).replace('0b', '')