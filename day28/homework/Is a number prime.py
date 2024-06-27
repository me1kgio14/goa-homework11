def is_prime(num):
    if num==1 or num==0 or num<0:
        return False 
    elif num==2 or num==3:
        return True
    elif num%2>0 and num%3>0:
        return True
    else:
        return False
    