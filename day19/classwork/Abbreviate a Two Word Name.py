def abbrev_name(name):
    help=[]
    lis=name.split()
    for i in lis:
        help.append(i[0].upper())
        x=".".join(help)
    return x