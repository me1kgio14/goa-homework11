def find_difference(a, b):
    sum0=1
    sum1=1
    for i in a:
        sum0*=i
    for i in b:
        sum1*=i
    return max(sum0,sum1)-min(sum0,sum1)