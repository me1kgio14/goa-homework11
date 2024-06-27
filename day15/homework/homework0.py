num1=int(input("enter number:"))
if num1%2==0:
    print("your number is even")
else:
    print("your number is odd")
    print(num1+1)


user_pass="Goa best"
input_pass=input("enter pass:")
while input_pass!=user_pass:
    input_pass=input("enter pass:")



user=input("enter word:")
if user[0:1]=="G":
    print("true")
else:
    print("false")



name0=input("enter name:")
name1=input("enter name:")
name2=input("enter name:")
name3=input("enter name:")
name4=input("enter name:")
list=[]
list.append(name0)
list.append(name1)
list.append(name2)
list.append(name3)
list.append(name4)
print(list[0:3])



i=11
while i>1:
    i-=1
    print(i)





num0=int(input("enter number:"))
num1=int(input("enter number:"))

print(num0+num1)
print(num0-num1)
print(num0*num1)
print(num0/num1)
print(num0**num1)



name=input("enter your name:")
print(name[-1:])


helper=[]
user_num=int(input("enter number:"))
for i in range(0,user_num) :
    if i%2==0:
        helper.append(i)
print (helper)



fact_num=int(input("enter number:"))
for i in range(0,fact_num+1):
    fact=(i*i)
print(fact)

































