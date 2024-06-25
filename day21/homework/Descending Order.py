def descending_order(num):
    helper=[]
    for i in str(num):
        helper.append(i)
    helper=sorted(helper)
    helper.reverse()
    x="".join(helper)
    return  int(x)