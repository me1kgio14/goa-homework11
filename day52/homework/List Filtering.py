def filter_list(l):
    ints=[]
    for i in l:
        if isinstance(i,str)==False:
            ints.append(i)
            
    return ints