def counter(*user_input):
    sum=0
    for i in user_input:
        if i.isupper()==True:
            sum+=1
