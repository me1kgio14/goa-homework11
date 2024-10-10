def max_multiple(divisor, bound):
    if bound%divisor==0:
        return bound
    for i in range(bound,divisor,-1):
        if i%divisor==0:
            return i
        