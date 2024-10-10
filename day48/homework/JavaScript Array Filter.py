def get_even_numbers(arr):
    helper=[]
    for i in arr:
        if i%2==0:
            helper.append(i)
    return helper