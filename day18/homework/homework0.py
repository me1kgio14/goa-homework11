def four(*nums):
    helper=[]
    for i in nums:
        if i%4==0:
            helper.append(i)
    return helper
print(four(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))



def user(name,surname):
    list=[]
    list.append(name)
    list.append(surname)
    return list
print(user("girgi","melqaZe"))



def square(first,last):
    halper=[]
    for i in range(first,last):
            if i%2==0:
                i==i**2
                halper.append(i)
            else:
                 i=i**0,5
                 halper.append(i)
    return halper
print (square(1,10))



def surname(lastnme):
    iteration=0
    helper=[]
    for i in lastnme:
        iteration+=1
        if iteration%2==0:
             helper.append(i)
    helper="".join(helper)
    return helper
print(surname("melkadze"))



def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum/len(numbers)

print(average(1,2,3,4,5,6))



def word(strs):
    return strs[::-1]
print(word("giorgi"))


def fiter(*nums):
    list=[]
    for i in nums:
        if nums.count(i)>1:
            list.append(i)
    return list

print(fiter(1,1,2,7,5,5))












