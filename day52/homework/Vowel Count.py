def get_count(sentence):
    counter=0
    for i in sentence:
        if i=="a":
            counter+=1
        elif i=="e":
            counter+=1
        elif i=="i":
            counter+=1
        elif i=="o":
            counter+=1
        elif i=="u":
            counter+=1
    return counter