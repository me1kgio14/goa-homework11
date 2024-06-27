def sun(*lis):
    sum=0
    for i in lis:
        sum+=i
    return sum
print(sun(2,3,4))



def greater(*string):
    helper=[]
    for i in string:
        if len(i)>5:
            helper.append(i)
    return helper
print(greater("gio","giorgi"))



def even(*numbers):
    list=[]
    for i in numbers:
        if i%2==0:
            list.append(i)
    return list
print(even(1,2,3,4,5,6,7,8))



def largest(*nums):
    ampty=[]
    m=max(nums)
    return m
print(largest(1,2,8,3,4,5))




def first_a(*strs):
    helper=[]
    for i in strs:
        if i[0:1]=="a":
            helper.append(i)
    return helper
print (first_a("anastasia","giorgi"))


def square(*numbs):
    halper=[]
    for i in numbs:
        i=i**2
        halper.append(i)
    return halper
print(square(1,2,3,4,4,5))




def legth(*strs):
    helper=[]
    for i in strs:
        i=len(i)
        helper.append(i)
    return helper
print(legth("giorgi","saba"))



def greater_10(*high):
    sum=0
    for i in high:
        if i>10:
            sum+=i
    return sum
print(greater_10(1,2,3,3,4,4,44,12))









    