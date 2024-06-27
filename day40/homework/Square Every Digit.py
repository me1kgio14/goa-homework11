def square_digits(num):
    emp=""
    for i in str(num):
        i=str(int(i)**2)
        emp+=i
    return int(emp)
        
        