from ctypes import pythonapi
from hashlib import algorithms_available
'''
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




#1 Write a program to print your name, age, and course. All the details should be stored in separate variables and then print
name="suraj"
age="23"
course="python"

print("Name:",name)
print("age:",age)
print("course:",course)

print("name:",name,"age",age,"course",course)

#2 Write a program to print the name, age, and course details of three students. All the details should be stored in separate variables and then print

name1, age1, course1 = "Ajay", 21, "python"
name2, age2, course2 = "mayank", 22, "arts"
name3, age3, course3 = "suraj", 20, "Computer Science"


print("Student 1 - Name:", name1, "| Age:", age1, "| Course:", course1)
print("Student 2 - Name:", name2, "| Age:", age2, "| Course:", course2)
print("Student 3 - Name:", name3, "| Age:", age3, "| Course:", course3)


#Write a program to sum 2 integer variable values without using a third variable

a=10
b=20

print("sum of",a, "and",b, "is", a+b )


#4 Write a program to multiply 2 floating points

num1=5.2
num2=4.2

num3=num1*num2
print("multiplication result:",num3)


#5 Write a program to print the ASCII Value of a character variable'
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

num2=input("please inter your  number:")
print("your number is:",num2)

print("sum of " ,num1, "and ", num2 ,"is ", num1+num2 )'''









print("testing github commit push")


'''
a=input("please inter first side: ")
print("first side is ", a)
b=input("please inter 2nd side: ")
print("first side is ", b)

c=((int(a)**2)+(int(b)**2))**0.5
print("**","is",c)'''


a=0
print("assignning",a==1)
a=1
print("assignning",a==0)




'''number1=int(input("enter the first number"))
number2=int(input("enter the second number"))

if number1 > number2:larger_number=number1
else:larger_number=number2
print("the larger number is:", larger_number)'''


'''number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
number3=int(input("enter the first number"))
largest_number=number1
if number2>largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
print("the largest no is:",largest_number)'''






'''number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the first number:"))
print(max(number1,number2,number3))'''



'''number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the first number:"))
print(min(number1,number2,number3))'''


#ae calculation by hyphothenes
'''a=int(input("enter the first number:"))
b=int(input("enter your second number:"))
hypo=((a**2+b**2)**0.5)
print("HYPOTHENESS IS :", hypo'''

#create rectangle
'''print("+"+"-"*10+"+")
print("|"," "*10,"|\n"*5,end="")
print("+"+"-"*10+"+")'''



#ascii value
print(ord("A"))
print(chr(65))



a=0
print("assignning",a==1)
a=1
print("assignning",a==1)


'''num1=int(input("please inter your number:"))
num2=int(input("please inter your number"))
print("sum is :", num1+num2)'''


'''num=int(input("please inter number:"))
print("your number is:",num)

num2=int(input("please inter your number:"))
print("your number is:",num2)

print("sum of ",num, "and", num2 ,"is",num+num2)'''


'''num1=int(input("please enter your number:"))
print("your number is:",num1)
num2=int(input("please enter your number:"))
print("your number is :", num2)

print("multiplication of",num1, "and", num2, "is",num1*num2)'''


'''num1=int(input("please enter your num:"))
print("your number is:",num1)
num2=int(input("please enter your num:"))
print("your number is:",num2)
print("flor division of ", num1 ,"and", num2,"is", num1//num2)



#remeinder operator
num1=int(input("please inter your numebr:"))
print("your number is", num1)
num2=int(input("please inter your numebr:"))
print("your number is:",num2)
print("your calculation or",num1 and num2 ,"is", num1 % num2)'''

#2 Write a program to print the name, age, and course details of three students. All the details should be stored in separate variables and then printagr"name","age","course:",
'''student1=("suraj",10,"ssc")
student2=("mayank",10,"bio")
student3=("ajay",20,"jaava")

print("student 1",student1)
print("student2", student2)
print("studenet3",student3)'''





#hyphotheness calculate
'''a=int(input("please inter your first number:"))
b=int(input("please inter your second number"))
hypo=((a**2+b**2)**0.5)
print("hypoyheness is :",hypo)'''

'''print("+" + "-"*10 + "+")
print(("|" + " "*10 +"|\n")*5,end="")
print("+" + "-"*10 + "+")



#2 Write a program to print the name, age, and course details of three students. All the details should be stored in separate variables and then print

student1=name1,age1,course1="suraj",22,"hindi"
student2=name2,age2,course2="mayank",22,"english"
student3=name3,age3,course3="ajay",22,"math"

print(student1,"\n",student2,"\n ", student3)




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




#1 Write a program to print your name, age, and course. All the details should be stored in separate variables and then print
name="suraj"
age=22
course="pytohn"

print("student:",name,age,course)


#Write a program to sum 2 integer variable values without using a third variable
a=10
b=10
print("sum of:", a ,"and",b ,"is",a+b)


#4 Write a program to multiply 2 floating points
num1=4.5
num2=5.2
print("multiplication  :",num1,"and",num2, "is",num1*num2)'''





'''a=int(input("please enter first side:"))
b=int(input("please enter second side:"))
hyp=((a**2+b**2)**0.5)
print("hyphotheness is :", hyp)'''

'''number=int(input("enter a  positive number:"))
if number % 2 == 0:
    print("the number is even:")
else:
    print("the number is odd:")'''


'''a=input(" please inter plant name:  ")
if a == "Spathyphillum":
    print("yes,spathyphillum is best plant:")
elif a=="spathyphillum":
    print("no ,i want a big spathyphillum:")
else:
    print("no! spathyphillum,not" ,a)'''



income=float(input("enter income:"))
if income <= income:
    tax=18*income/100
    tax -=556.2
else:
    tax=((32*(income-85528))/100)
    tax+=14839.2

if tax<=0:
    print("tax=0")

else:
    print("tax",tax)









