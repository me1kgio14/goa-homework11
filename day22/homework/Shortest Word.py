def find_short(s):
    helper=[]
    list=s.split()
    for i in list:
        helper.append(len(i))
        helper=sorted(helper)
    
    return helper[0]