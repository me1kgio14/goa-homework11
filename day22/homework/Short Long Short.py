def solution(a, b):
    if len(b)<len(a):
        return b+a+b
    else:
        return a+b+a