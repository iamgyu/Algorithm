def solution(rsp):
    table = str.maketrans('205', '052')
    return rsp.translate(table)