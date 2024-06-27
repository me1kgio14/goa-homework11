def longest(a1, a2):
    whole_str=a1+a2
    result=[]
    for i in whole_str:
        if i not in result:
            result.append(i)
    result=sorted(result)
    result="".join(result)
    return result
    