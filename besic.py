'''print("hello")

print("11111111")

print("000000")

print("h")
print("e")
print("L")
print("L")
print("O")

print("0000000")
print("h\ne\nl\nl\no")


#print("suraj how you")
print("everything is okay")


print("suraj")

print("12345678\n"*8)

print("8+8")

print("100+100")

print("everthing is cleared")

print("1234567890")

print("hello")
print("a=5+b=5")

print("hello\n"*9)
#print("**********\n**********\n**********\n**********\n**********")


print("*********\n"*9)

print(2.2)
print("2.2")
print(True)

print("suraj",sep="_")

print("suraj",end="_")

print("suraj",end="@")

print("suraj",sep="%")



print(1,2,3,4,5,6,)
print(1,2,3,4,5,6,)

print("*********\n*********\n*********\n*********\n*********\n")

print("age=4")
print("age")

age=4
print(age)

print(type(age))


age="four"
print(age)
print(type(age))


name="aditya"
profession="software developer"
experience=10
print("hello, i am",name,", i am a",profession," profesionaly .and i have around",experience,"with it")

print("0000000000")




























a=50
b=10
c=0
c=a+b
print(a,"and",b,"is",c)

c=a-b
print(a,"and",b,"is",c)

c=a*b
print(a,"and",b,"is",c)

c=a/b
print(a,"and",b,"is",c)

c=a//b
print(a,"and",b,"is",c)

c=a%b
print(a,"and",b,"is",c)

c=a**b
print(a,"and",b,"is",c)


# print("     *"   )
print(" "*5, end="*\n")
# print("    *  *")
print(" "*4, " "*2, sep="*", end="*\n")

print(" "*2,  " "*6, sep="*", end="*\n")

print("*"*3," "*4,"*"*3 )

#print("  *      *")
print(" "*2, " "*6, sep="*", end="*\n")
print(" "*2, " "*6, sep="*", end="*\n")

print(" "*1,"*"*8)




print(" "*1,"*"*8)
print(" "*2, " "*6, sep="*", end="*\n")
print(" "*2, " "*6, sep="*", end="*\n")
print("*"*3," "*4,"*"*3 )
print(" "*2,  " "*6, sep="*", end="*\n")
print(" "*4, " "*2, sep="*", end="*\n")
print(" "*5, end="*\n")

#print("hello")

print("*"*17 )

print("*              *")
print("*              *")
print("*              *")
print("*              *")
print("*              *")
print("*              *")
print("*"*17)


# arithmetic operator
print("sum is :", 4 + 5)
print("difference is :", 10 - 5)
print("multiplication is :",  10*  5)
print("division is :",  10 / 5)
print("flor division is :", 15 // 2)
print("remainder is :", 2 % 5)
print("exponentiation is :" 4 ** 3)


#assignment operators
x = 5
y=x
print(x,y)
x+=y
print(x,y)
x -= y
print(x,y)
x *= y
print(x,y)

#comparision_opreatoo"
n1=10
n2=20
print(n1 == n2)
print(n1 != n2)
print(n1 > n2)
print(n1 < n2)
print(n1 >= n2)
print(n1 <= n2)

#logical_operator(and,or,not)
exp1=2 > 3
exp2=5 < 4
print("exp1 and exp2 :", exp1 and exp2)
print("exp1 and exp2 :", exp1 or exp2)
print("not exp1  :", (exp1))

#identity_operatores(is,,is_not)
x = 5
y = 5
print("if x is y :", x is y )
print("if x is not y :", x is not y )

#membership_operator(in,in_not)
fruits=("apple","banana","cherry")
print("if banana is present in fruits :", "banana" in fruits)
print("if mango is not present fruits :", "mango" not in  fruits)

#bitwise_operaotr


#typecasting



#ascii value
print (ord("*"))
print (ord("b"))
print(ord("A"))
print(ord("D"))
print(ord("#"))

print(chr(98))
print(chr(100))
print(chr(103))
print(chr(110))
print(chr(111))'''


'''n = int(input("Enetr a numbe rof n:"))
for i in range(1,n):
    for j in range(1,n+1):
        print(j,end = "")
    print()
'''



'''n = int(input("Enter a number rof n:"))
for i in range(n):
    for j in range(1,i+1):
        print(j,end = "")
    print()'''



'''list = [1,2,3,4,5]
list.insert(2,7)
print("updated list after insert",list)'''


'''list = [1,2,3,4,5]
list.inse,7)
print("updated list after insert",list)'''

'''list=[]
for count in range (10):
    list.append(count +1)
print(list)'''


'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for count in range(len(my_list)):
    my_list[count] += 1
print(my_list)
'''

'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for count in range(len(my_list , )):
    my_list[count] += 1
print(my_list)
'''

'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0
for count in range(len(my_list)):
    sum = sum + my_list[count]
    print(sum)'''




'''n = int(input("enter n:"))
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()'''





'''print("*" * 17)  # Top border
for i in range(1,10):
    print("*"+" "*15+"*")
print("*" * 17)  # Bottom border'''

'''n = int(input("enter a n:"))
for i in range(1,n+1):
    print(" "*(n-i),end ="")
    for j in range(1,2*i):
        print(j,end = "")
    print()'''


# List(mutable)
fruits = ["Apple","banana","cherry","Kiwi"]
fruits[0] = 1
print(fruits)              # print a list

#print(type(fruits))       #cheak type of list

#print(len(fruits))         #  how to cheak lenth of  list

# checking if item is present  in a list.


