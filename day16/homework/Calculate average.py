def find_average(numbers):
    sum=0
    for i in numbers:
        sum+=i
    
    if len(numbers)==0:
        return 0
    else:
        return sum/len(numbers)