
def is_anagram(test, original):
    l=[]
    test=test.lower()
    for i in test:
        l.append(i)
        l=sorted(l)
    b=[]
    original=original.lower()
    for i in original:
        b.append(i)
        b=sorted(b)
    if b==l:
        return True
    else:
        return False
    
    