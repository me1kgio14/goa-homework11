# return masked string
def maskify(cc):
    length=len(cc)
    if int(length)>4:
        return (int(length)-4)*"#"+cc[-4:]
    elif int(length)<=4:
        return cc
    else:
        return cc