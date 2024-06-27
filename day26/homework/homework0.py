def manual_sum(*list):
    sum=0
    for i in list:
        sum+=i
    return sum
print(manual_sum(1,2,34,5,64,23,23,4))


def max_find(*numbers):
    numbers=sorted(numbers)
    return numbers[-1]



def min_find(*nums):
    nums=sorted(nums)
    return nums[0]
print(min_find(1,5,2,8.4,52,4,5,2,9))






def length_find(*leng):
    length=len(leng)
    return length
print(length_find(1,2,3,42,3,4,4,56,))



def menual_reduce(*ist):
    copy_list=[]
    for i in list:
        copy_list.append(i)
    return ist 
print(menual_reduce(1,2,34,6,7,9,6,45,32,))




