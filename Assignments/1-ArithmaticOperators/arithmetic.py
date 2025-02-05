from ctypes import pythonapi
from hashlib import algorithms_available

a=40
b=20

c=0

c=a+b
print("the sum of",a,"and",b,"is",c,) #correct

c=a-b
print("the difference of",a,"and",b,"is",c)#correct

c=a*b
print("the multiplication of",a,"and",b,"is",c)#correct

c=a/b
print("the division of",a,"and",b,"is",c)#correct

c=a//b
print("the division floored of",a,"and",b,"is",c)#correct

c=a%b
print("the reminder after division of",a,"and",b,"is",c)

c=a**b
print("the first variable to power of 2nd variable of",a,"and",b,"is",c)





print(" "*8,"*")
print(" "*5,"*"," "*3,"*")
print(" "*4,"*"," "*5,"*",)
print(" "*3,"*" ," "*7,"*")
print(" "*2,"*"*4," "*3,"****")
print(" "*5,"*"," "*3,"*")
print(" "*5,"*"," "*3,"*")
print(" "*5,"*"*7)



print(" "*9,sep="*",end="*\n")
print(" "*6," "*5,sep="*",end="*\n")
print(" "*4," "*9,sep="*",end="*\n")
print(" "*3," "*12,sep="*",end="*\n")
print(" "*2," "*6,sep="*"*5,end="*****\n")
print(" "*5,"*"," "*4,"*")
print(" "*5,"*"," "*4,"*")
print(" "*5,"********")


x=("maruti","bmw")
y=("maruti","bmw")
z=x

print(z is y)
print(x is z)
print(z is x)


print("maruti" in x)
print("bmw" in y)
print("bmw" in z)
print("fortuner" in x)


print("hello")




'''1 Write a program to print your name, age, and course. All the details should be stored in separate variables and then print'''
name="suraj"
age="23"
course="python"

print("Name:",name)
print("age:",age)
print("course:",course)

print("name:",name,"age",age,"course",course)

'''2 Write a program to print the name, age, and course details of three students. All the details should be stored in separate variables and then print'''

name1,age,course1="ajay",21,"pytohn"
name2,age2,course2="mayank",22,"arts"
name3,age3,course3="suraj",23,"computer science"

print("student1",name1,age,course1)
print("student2",name2,age2,course2)
print("student3",name3,age3,course3)
'''Write a program to sum 2 integer variable values without using a third variable'''

a=10
b=20

print("sum of",a, "and",b, "is", a+b )


'''4 Write a program to multiply 2 floating points'''

num1=5.2
num2=4.2

num3=num1*num2
print("multiplication result:",num3)


'''5 Write a program to print the ASCII Value of a character variable'''
print (ord("*"))
print (ord("b"))


#10print("your name is: ",name")

num=int(input("please inter number:"))
print("your number is:",num)

num2=int(input("please inter your number:"))
print("your number is:",num2)

print("sum of ",num, "and", num2 ,"is",num+num2)



num1=input("please inter your number:")
print("your number is:",num1)

num2-input("please inter your  number:")
print("your number is:",num2)

print("sum of " ,num1, "and ", num2 ,"is ", num+num2, )












print("testing github commit push")