from ctypes import pythonapi
from enum import nonmember
from os import WCONTINUED

#from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from hashlib import algorithms_available
from tkinter.font import names

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


'''a=0
print("assignning",a==1)
a=1
print("assignning",a==0)'''




'''number1=int(input("enter the first number"))
number2=int(input("enter the second number"))

if number1 > number2:larger_number=number1
else:larger_number=number2
print("the larger number is:", larger_number)'''


'''number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
number3=int(input("enter the third number"))
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
#print(ord("A"))
#print(chr(65))



'''a=0
print("assignning",a==1)
a=1
print("assignning",a==1)'''


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

print("multiplication of",num1, "and", num2, "is",num1*num2)

num1=int(input("please enter your num:"))
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




'''(Q1)Practice Question:
Write a program that utilizes the concept of conditional execution, takes a string as input, and:
● prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the
inputted string is "Spathiphyllum" (upper-case)
● prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum"
(lower-case)
● prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.'''

'''plant = input("please enter plane name:")
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "Spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [plant]!")'''








''''#(q2)Practice Question:
Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The
people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income
Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
● if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus
556 thalers and 2 cents (this was what they called tax relief)
● if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of
the surplus over 85,528 thalers.
Your task is to write a tax calculator.
● It should accept one floating-point value: the income.
● Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which
will do the rounding for you – you'll find it in the skeleton code in the editor.
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it
would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.'''



'''income=float(input("enter income:"))

if income <= income:
    tax=18*income/100
    tax -=556.2
else:
    tax=((32*(income-85528))/100)
    tax+=14839.2

if tax<=0:
    print("tax=0")

else:
    print("tax",tax)'''





'''while True:
    print("I am stuck in a loop")'''




'''largest_number=-99999999

number=int(input("enter a number or type -1 to stop :"))
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("enter a number or type -1 to atop:"))
print("the largest number is :", largest_number)'''


#-----





'''2.⁠ ⁠Write a Program to Count Numbers of Digits in this String
    a. Input: string = "Uraan Softskills password2 is : 1234"
    b. Output: Total number of Digits = 5'''


'''def count_digits(input_string):
    # Initialize a variable to count the digits
    digit_count = 0

    # Loop through each character in the string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            digit_count += 1

    # Print the result
    print(f"Total number of Digits = {digit_count}")'''







'''3.⁠ ⁠Write a Program to Count Numbers of Digits in this String
    a. Input: string = "U r a a n S 0 f t s k i l l 1 s 1234"
    b. Output: Total number of Digits = 6'''


'''def count_digits(input_string):
    # Initialize a variable to keep track of the count of digits
    digit_count = 0

    # Loop through each character in the string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            digit_count += 1

    # Print the result
    print(f"Total number of Digits = {digit_count}")'''










'''4.⁠ ⁠Write a program to find the count for the occurrence of 's' or 'S' character in a string
    a. Input: "UraanSoftskills"
    b. Output: 3'''


'''def count_s_occurrences(input_string):
    # Convert the string to lowercase and count the occurrences of 's'
    count = input_string.lower().count('s')

    # Print the result
    print(f"Count of 's' or 'S' in the string: {count}")'''


'''Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The
people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income
Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
● if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus
556 thalers and 2 cents (this was what they called tax relief)
● if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of
the surplus over 85,528 thalers.
Your task is to write a tax calculator.
● It should accept one floating-point value: the income.
● Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which
will do the rounding for you – you'll find it in the skeleton code in the editor.
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it
would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
'''

'''def calculate_tax(income):
    # First tax bracket: income less than or equal to 85,528 thalers
    if income <= 85528:
        tax = 0.18 * income - 556.02
    # Second tax bracket: income greater than 85,528 thalers
    else:
        tax = 14839.02 + 0.32 * (income - 85528)
    
    # If the tax is negative, return 0 (no tax)
    if tax < 0:
        return 0
    
    # Round the tax to the nearest whole thaler
    return round(tax)'''

'''6.⁠ ⁠Write a program to find the frequency of each character in a given string
    a. Input: "UraanSoftskills"'''

'''def character_frequency(input_string):
    # Use Counter to count the frequency of each character in the string
    freq = Counter(input_string)

    # Print the frequency of each character
    for char, count in freq.items():
        print(f"'{char}': {count}")'''



'''5.⁠ ⁠Write a program to count the number of repeated characters and unique characters in a string
    a. Input: "UraanSoftskills"'''

'''def count_characters(input_string):
    # Count frequency of each character using Counter
    freq = Counter(input_string)
    
    # Initialize counts for repeated and unique characters
    repeated = 0
    unique = 0
    
    # Loop through each character and its frequency
    for count in freq.values():
        if count > 1:
            repeated += 1  # Increase repeated count if character occurs more than once
        else:
            unique += 1  # Increase unique count if character occurs only once

    # Print the results
    print(f"Number of repeated characters: {repeated}")
    print(f"Number of unique characters: {unique}")'''










'''6.⁠ ⁠Write a program to find the frequency of each character in a given string
    a. Input: "UraanSoftskills"'''


'''def character_frequency(input_string):
    # Use Counter to count the frequency of each character in the string
    freq = Counter(input_string)

    # Print the frequency of each character
    for char, count in freq.items():
        print(f"'{char}': {count}")'''


'''name= "suraj"
#print(name[0:3])
print(name[-4:  -1])
print(name[1:4  ])'''



#print("hello world \"suraj\"")


'''name=input("enter your name")
print("good after noon",name)'''



'''#latter= "Dear suraj , this python  course is nice. Thanks "
latter=("Dear suraj, \n\t this pytohn course is nice .\n Thanks!")
print(latter)'''


'''Practice Question:
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.'''



'''year=int(input("enter a year:"))
if year < 1582:
    print(not"the gregorian calendar:")
else:
    if year % 4!=0:
        print("it's a common year")
    elif year % 100!=0:
        print("it's a leap year")
    elif year % 400!=0:
        print("it's a common year")
    else:
        print("it's a leap year")'''



'''Write a program to create 2 variables, initialize them with integer values, Print the sum of both
variables'''
'''a=5
b=5
c=a+b
print("sum is", a+b)'''



'''Write a program to calculate hypotenuse between to sides'''
'''a=int(input("please enter first side: "))
b=int(input("Please enter second side:"))
hyp=((a**2+b**2)**0.5)
print("hypotenuse is :",hyp)'''


'''Write a program to print this pattern using just print function
+----------+
|          |
|          |
|          |
|          |
|          |
+----------+'''
'''print("+"+"-"*10+"+")
print(("|" + " " * 10 + "|\n")*5)
print("+"+"-"*10+"+")'''

'''It's time to complicate the code – let's find the largest of three numbers. Will it enlarge the code? A bit.
We assume that the first value is the largest. Then we verify this hypothesis with the two remaining values.
Look at the code below:'''
'''number1=int(input("Enter the first number"))
number2=int(input("Enter the second number"))
number3=int(input("enter the third number"))

largest_number = number1


if number2 > largest_number:
    largest_number = number2


if number3 > largest_number:
   largest_number = number3

print("the largest_number is ",largest_number)'''

    
'''Your code correctly finds and prints both the largest and smallest numbers among the three user inputs. It is clean and efficient'''
'''number1=int(input("Enter  a first number:"))
number2=int(input("Enter a second number:"))
number3=int(input("Enter a third number:"))

largest_number=max(number1,number2,number3)
smallest_number=min(number1,number2,number3)

print("largest number is:",largest_number)
print("smallest number is:",smallest_number)'''




'''Write a program that utilizes the concept of conditional execution, takes a string as input, and:
● prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the
inputted string is "Spathiphyllum" (upper-case)
● prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum"
(lower-case)
● prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.'''
'''plant=input("pleae enter plant name:")
if plant=="Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant=="spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]!",plant)'''

'''Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The
people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income
Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
● if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus
556 thalers and 2 cents (this was what they called tax relief)
● if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of
the surplus over 85,528 thalers.
Your task is to write a tax calculator.
● It should accept one floating-point value: the income.
● Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which
will do the rounding for you – you'll find it in the skeleton code in the editor.
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it
would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
'''


'''def calculate_tax(income):
    # First tax bracket: income less than or equal to 85,528 thalers
    if income <= 85528:
        tax = 0.18 * income - 556.02
    # Second tax bracket: income greater than 85,528 thalers
    else:
        tax = 14839.02 + 0.32 * (income - 85528)

    # If the tax is negative, return 0 (no tax)
    if tax < 0:
        return 0

    # Round the tax to the nearest whole thaler
    return round(tax)'''






#counter=0
#while counter < 100:
#    counter+=1
#    print("counter",counter)



#for counter in range(100):
#   print("counter",counter+1)

#for counter in range (2,8):
# print("the value of counter is" ,counter)

#for counter in range (2 , 8 ,3):
#  print("the value of counter is", counter)

#print("going in for loop:")
#for counter in range(1,1):

#power=1
#for expo in range(16):
#    print("2 to the power of",expo,"is",power)
#   power *= 2

'''import time
for counter in range (5):
    print(counter+1,"mississippi")
    time.sleep(1)
print("read or  read, hear i come!")'''


# break-  example
'''print("The beak instruction:")
for counter in range (1,6):
    if counter == 3:
        break
    print("inside the loop.",counter)
print("outside the loop.")'''

#countinue - example
'''print("\n The countinue instruction:")
for counter in range (1,6):
    if counter == 3:
        continue
    print("inside the loop",counter)
print("out side the loop.")'''




'''largest_number=-99999999
counter=0
while True:

    number = int(input("enter a number or type -1 to end program:"))
    if number  == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number
if counter!= 0:
 print("the largest number is :", largest_number)
else:
 print("you haven't enterd my number")'''



'''You must design the (ugly) vowel eater! Write a program that uses:
a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:
ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.'''


'''word = input(" please Enter a word: ")
print("word is:", word)
word=word.upper()
word_without_vowels=""
for itr in word:
    print("Latter is",itr)
    if itr == "A" or itr == "E" or itr == "I" or itr == "O" or itr == "U":
        continue
    word_without_vowels += itr
print("not eaten word are:",word_without_vowels)'''

'''counter = 1
while counter < 5:
    print("counter",counter)
    counter +=1
else:
    print("else counter:", counter)


counter = 111
for counter in range (2,1):
    print("counter")
else:
    print("else:",counter)'''


'''Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are
building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according
to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
Your task is to write a program which reads the number of blocks
the builders have, and outputs the height of the pyramid that can
be built using these blocks.
Note: the height is measured by the number of fully completed layers –
if the builders don't have a sufficient number of blocks and cannot
complete the next layer, they finish their work immediately.'''


'''blocks=int(input("Enter the number of blocks:"))
height = 0
used_blocks = 0

while   used_blocks +(height +1) <= blocks:
    height =  +1
    used_blocks += height

print("The height of the pyramid:", height)'''


#Calculator   (match case)

'''num1 = int(input("Enter  number 1:"))
num2 = int(input("Enter number 2:"))

operator = input("Enter operator:" )
match operator:
    case"+": 
        print("sum is ", num1 + num2)
    case"-":
        print("Difference is ", num1 - num2 )
    case"*":
        print("multiplication is ", num1 * num2 )
    case"%":
        print("divisiom is ", num1 % num2)
    case"/":
        print("flot division is ", num1 / num2 )'''






#turnery operator
'''num = int(input("enter a number :"))
output ="Even" if num % 2 == 0 else"Odd"
print("output is ", output)'''



'''list = [10,20,30,40,50,60]

for i in list:
        
    print(i)'''

'''fruits=["apple","banana","kiwi"]
for i in fruits:
    print(i)'''


'''i = 2
while i < 101:
    print(i)
    i += 2'''

'''j = 0
while j  <= 10:
    print(j)
    j = j+1'''

'''x = 1
while x  == 1:
    x= x-1
    print(x)'''

'''x =  4
y = 0
while x >= 0:
    x -= 1
    y += 1
    if x ==y:
     continue
else:
    print(x,y)'''


'''name = "Suraj"
roll_number = 12
number = 92.5
is_student = True'''

#print(name ,roll_number,  number ,is_student)
#print(name ,roll_number,  number ,is_student)
#print("my name is "  + name + "and my number is " ,number )
#print("my number has change",number - 5.0)
#print(name ,roll_number,  number ,is_student, sep = "-")


'''x=10
y="5"
print(x+int(y))'''


#Take the integer input and tell if it is positive or negative.
'''number = int(input("Enter a number:"))
if number >= 0:
    print("The number is positive:")
else:
    print("The number is negative:)"'''

#Take positive integer input and tell if it is even or odd.
'''number = int(input("Enter  positive number: "))
if number % 2 == 0:
    print("It is even number")
else:
    print("It is odd number")'''


'''IF COST PRICE AND SELLING PRICE OF AN ITEM IS INPUT THROUGH THE KEYBORD, WRITE  A PROGRAM TO DETERMIE WHETEHR THE SELLER HAS MADE PROFIT
OR INCUURED LOSS OR NO PROFIT NO LOSS. ALSO DETERMINE HOW MUCH PROFIT HE MADE OR LOSS INCUURED'''

'''cost_price = int(input("Enter the cost price:"))
selling_price = int(input("Enter the selling price:"))

if  cost_price < selling_price:
    profit = selling_price - cost_price
    print("We have made profit", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("we have made loss", loss)
else:
    print("We have made no loss no profit ")'''

# Take input percentage of student and print the grade according of marks:
'''marks = int(input("Enter the marks:"))

if marks > 80:
    print("very good grade ")
elif marks > 60:
    print(" good grade")
elif marks > 40:
    print("average grade")

else:
    print("student is fail")'''

# using multiple condition and , or :

'''english_marks = int(input("Enter a english marks:"))
math_marks = int(input("Enter a math marks:"))
if english_marks > 80 and math_marks >80:
    print(" A grade ")
elif english_marks > 80 or math_marks >80 :
    print(" B grade ")
else:
    print("C grade ")'''

# Take positive integer input and tell if it is a four digit number or not.if
'''number = int(input("Enter a number:"))
if number >= 1000 and number <= 9999:
    print("it is four digit number")
else:
    print("not a four digit number")'''

# Take 3 positive integer input and print the greatest of them.
'''n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))

if n1 > n2 and n1 > n3 :
    print(n1 , "is greatest number")
elif n2 > n1 and n2 > n3 :
    print(n2, " is greatest number")
else:
    print(n3, "is greatest number")'''

# Taking nested if else statement:

'''n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))
if n1 > n2:
    if n1 > n3:
        print(n1, "is the greatest element:")
    else:
        print(n3,"is the greatest element:")
else:
      if n2 > n3:
          print(n2, "is greatest element")
      else:
          print(n3,"is the greatest element")'''

# Take a positive input and tell if it is divisible by 5 or 3 but not divisible by 15.

'''num = int(input("Enter a positive number "))
if num % 15 == 0:
     print("number is divisible by 15")
else:
    if num % 3 == 0 or num % 5 == 0 :
        print("number is not divisible by 15 but divisible by 3 or 5")
    else:
        print("number is neither divisible by 3 bor by 5  ")'''

# calculator create by match case :
'''num1= int(input("Enter number1 :"))
num2= int(input("Enter number2 :"))

operator = input("Enter operator")
match operator:
    case("+"):
        print("sum is ",num1+num2 )
    case("-"):
        print("difference is ",num1 - num2)
    case("*"):
        print("multiplication is ",num1 * num2)
    case("%"):
        print("division is ", num1 % num2 )'''

#Write a program to check if number is odd or even using ternary operator.
'''num = int(input("enter a positive number :"))

operator = "even" if num % 2 == 0 else "odd"
print("operator is " , operator )'''

#for loop
#for i in  range (10,20,):
#    print(i,"hello world")

#Print element of a list using for loop.
'''list = [10,20,30,40,50,60]

for i in list:
    print(i)'''

'''fruits = ["apple", "banana", "kiwi"]
for i in fruits:
    print(i)'''

# while loop.(its run till a condition is true )

'''i = 0
while i < 10:
    print(i)
    i += 1'''

# while loop help print even no
'''i = 2
while i <= 101:
    print(i)
    i += 2'''

#predict the output

'''j = 0
while j < 10:
    print(j)
    j = j + 1'''


'''x = 1
while x== 1:
    x = x-1
    print(x)'''

# while loop computer buff
'''i = 10
while i == 20:
    print("computer buff")#this code will not run'''


# while loop (continue) keyword.

'''x = 4
y = 0
while x >= 0:
    x -= 1
    y += 1
if x == y:
        continue
else:
    print(x,y)'''

'''i = 1
while i <= 5:
    print(i)
    i += 1'''

# Print the multiplication table of a number n.(while loop )
'''n = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1'''

#print the elements of the following list using  a loop:
#[1,4,9,16,25,36,49,64,81,100]

'''nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1'''

#Search for a number x in this Tuple    (Error)------------
#(1,4,9,16,25,36,49,64,81,100)
'''nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("FOUND at idx",i)
    else:
        print("finding.... ")
        i += 1'''



#cost_price and selling_price calculation
'''cost_price = int(input("Enter a cost price:"))
selling_price= int(input("Enter a selling price:"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("we have made profit", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("we have made loss inncured")
else:
    print("we have made no loss no profit")'''

# Take positive integer input and tell if it is a four digit number or not.
'''number = int(input("Enter a positive number:"))
if number >= 1000 and number <= 9999 :
    print("it is four digit number :")
else:
    print("not a four digit number ")'''

# Take the 3 positive integer and tell the greatest of them .
'''n1 = int(input("enter a number1 :"))
n2 = int(input("enter a number 2 :"))
n3 = int(input("enter a number 3 :"))

if n1 > n2 and n1 > n3:
    print(n1 ,"is greatest number ")
elif n2 > n1 and n2 > n3:
    print(n2,"is greatest number")
else:
    print(n3,"is greatest number")'''


# Take the 3 positive integer and tell the greatest of them .(using nested if else ; statement

'''n1 = int(input("enter a number1 :"))
n2 = int(input("enter a number 2 :"))
n3 = int(input("enter a number 3 :"))

#comparision n1 and n2
if n1 > n2:
    #either n1 or n3 is greatest:
    if n1 > n3:
        print(n1, "is the greatest element")
    else:
        print(n3, "is the greatest element")
else:
    #either n2 or n3 is greatest
    if n2 > n3:
        print(n2, "is hte greatest element")
    else:
        print(n3, "is greatest element")'''


# print the pattern given (*****),
'''n = int(input("enter n:"))
for _ in range (n):
    print("*"*5)'''

#print the pattern (1234), (123456)

'''n = int(input("Enter n:"))

for i in range (n):
    for j in range(1,n+1):
        print(j,end = "")
    print()'''

#print the pattern  (1), (12), (123), (1234)
'''n = int(input("Enter n:"))

for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end = "")
    print()'''

# for pattern question :(*****)
'''n = int(input("Enter n:"))
for i in range (n):
    print("*"*5)'''

#for pattern question(1234,123456)
'''n = int(input("Enter n:")) # user input

for i in range(n): #loop for rows

    for j in range (1,n+1): #loop for columns
        print(j,end="")
    print()'''

# print the given pattern (for n = 4)(1,12,123,1234,)
'''n = int(input("Enter n:"))

for i in range(1,n+1):

    for j in range (1,i+1):
        print(j,end = "")
    print()'''



#print the given pattern.(for n = 4).(A,AB,ABC,ABCD)

'''n = int(input("enter n :")) #user input

for i in range (1,n+1): # loop for rows
    
    for j in range(i): #loop for columns.
        
        print(chr(65),end="")
    print()'''


# print the given pattern (1,123,1234,12345,123456,1234567,)

'''n = int(input("Enter n: "))  # User input for number of rows

for i in range(1, n + 1):  # Loop for rows
    # Printing spaces to center the pattern
    print(" " * (n - i), end="")
    # Printing numbers
    for j in range(1, 2 * i):
        print(j, end="")
    print()  # Move to the next line'''


#pyramid (for loop )
'''In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains
unproven) which can be described in the following way:
1. take any non-negative and non-zero integer number and name it c0;
2. if it's even, evaluate a new c0 as c0 ÷ 2;
3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4. if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural
number (it may even require artificial intelligence), but you can use Python to check some individual numbers.
Maybe you'll even find the one which would disprove the hypothesis.
Write a program which reads one natural number and executes the above steps as long as c0 remains different
from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the
intermediate values of c0, too.
Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the
key to success.'''

'''c0 = int(input("Enter the value of c0: "))

if c0 <= 0:
    print("c0 cannot be zero or negative. Please enter a positive integer.")
else:
    counter = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 //= 2  # Integer division
        else:
            c0 = 3 * c0 + 1
        print("c0 =", c0)
        counter += 1

    print("Final c0:", c0, "\nSteps it took:", counter)'''

# use  while loop(number validation 1,100)
'''x = 0
while not(1<=x<=100):
    x=int(input("please inter a number of 1 to 100"))
print("valid of ",x)'''

# for loop(number validation 1,100)
'''for i in range(100):
    x = int(input("enter a number of 1 to 100:"))
    if 1 <= x <= 100:
        print("valid number ",x)
        break
    print("enter a valid number ")'''

#for i in range(10):
#print("*"*10)

'''i = 0
while i <= 50:
    print("*"*10)
    i += 1'''


'''for i in range(1,51,):
    if i % 2 ==0:
        print("t")
    else:
        print(i)'''

'''for i in range(1,51,):
    if i % 3 == 0:
        print("t")
    else:
        print(i)'''

'''for i in range(1,51):
    if i % 3 == 0:
        print("fiz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
  
        print(i)'''



# print(1,2,3,4,5,6,7,8,9..........50)(using while loop )
'''n = 1
while  n <= 50:
    if n % 3 == 0:
        print("fizz")
    if n % 5 ==0:
        print("buzz")
    if n % 3 ==0 and n % 5 == 0:
        print("fizzbuzz")
        n += 1'''


'''
1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5 '''

'''r = 6
for i in range(1,r+1):
    for j in range(1,i):
        print(j,end=" ")
    print()'''

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 '''

'''r = 6
for i in range(r,0,-1):
    for j in range(1,i):
        print(j,end = "")
    print()'''






'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

'''n = 5
for i in range(n):
    print(" " * (n-i-1) + "* " *(i+1))'''

#(******) user input lena hai or y print krna h
'''n = int(input("Enter a number of rows:"))

for i in range(n):
    print("*"*5)'''


'''n = int(input("enter a number of rows:"))
for i in range(n):
    for j in range(1,n+1):
        print(j,end = "")
    print()

'''

# list
#list1 = [20,5.5,"hello"]
#list1[2]="good"
#print(list1)

# asendng print list
'''list = [1,5,6,4,3,2,]
print(list.sort())
print(list)

# decending print list
list = [1,5,6,4,3,2,]
print(list.sort(reverse = True))
print(list)'''



#Q1 Write a program to print the first 10 natural numbers using for loop.
#for i in range(1,11):
#   print(i)

#Q2 Write a program to print all the even numbers within the range of 10

'''for i in range(1,10):
    if  i % 2 == 0:
        print(i)'''

#Q3 Write a program to calculate the sum of all numbers from 1 to a given number - 15.


'''n = 15

sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum of numbers from 1 to", n, "is:", sum_n)'''

#Q4 Write a program to calculate the sum of all the odd numbers within the given range of 15.

'''for i in range(1,15):
    if i % 3 == 0:
        print(i)'''


#Q5 Write a program to print a multiplication table of a given number 15.
'''n = 15
for i in range(n*1):
    print(i)
    i += 1'''####wrong....



# list
'''numbers = [10,5,7,2,1,]
print(numbers)

numbers = [10,5,7,2,1,]
print(numbers[0])

numbers = [10,5,7,2,1,]
print(numbers[1])


numbers = [10,5,7,2,1,]
print(numbers[2])

numbers = [10,5,7,2,1,]
print(numbers[3])'''

#numbers = [10,5,7,2,1,]
#numbers[0] = 111
#print("new list contains",numbers)

'''numbers = [10,5,7,2,1,]
numbers[1] = numbers[4]
print("new list contains",numbers)'''

# use len()
#numbers = [10,5,7,2,1,1,2,3,]
#print(len(numbers))

#delete
'''numbers = [10,5,7,2,1,]
del numbers[1]
print(len(numbers))
print(numbers)'''

#[-1]
'''numbers = [10,5,7,2,1,]
print(numbers[-1])'''


#(*****)
'''n = int(input("Enter a number n:"))
for i in range(n):
    print("*"*5,end = "")
    print()'''

'''n = int(input("Enter a number n:"))
for i in range(1,n+1):
    for  j in range(i):
        print("* " ,end = "")
    print()'''

'''n = int(input("Enter a number n:"))
for i in range(n,0,-1):

    for j in range(i):
        print("*",end = "")
    print()'''

'''num = 6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = " ")
    print()'''

'''rows = 6
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()'''







#Q1--Write a program to print the first 10 natural numbers using for loop.
'''for i in range(1,11):
    print(i)'''

#Q2--Write a program to print all the even numbers within the range of 10
'''num = 10
for i in range(num):
    if i % 2 ==0:
        print(i)'''



#Q3--Write a program to calculate the sum of all numbers from 1 to a given number - 15

'''n= 15
num = 0
for i in range(1,n +1):
    sum += i
print("sum of all numbers from 1 to a given number - 15",sum)'''


#Q4--Write a program to calculate the sum of all the odd numbers within the given range of 15

'''n = 15
sum_odd = 0
for i in range(1,16):
    if n % 2 != 0:
        sum_odd += n
print("sum of all the odd numbers within the given range of 15:",sum_odd)'''


#Q5--Write a program to print a multiplication table of a given number 15

'''n = 15
for i in range(1,15):
    print(n * i)'''

#Q6--Write a program to display numbers from a list using a for the loop [1,2,4,6,88,125]
'''numbers = [1,2,4,6,88,125]
for i in list (numbers):
    print(i)'''


#Q7--Write a program to count the total number of digits in a number 129475
'''number = 129475

print(len(str(number)))'''


#Q7--Write a program to check if the given string is a palindrome - madam


#Ek program likhe jo kisi bhi do numbers (a aur b) ka input le aur unka hypotenuse calculate kare, jisme:
'''a = int(input("Enter a first side:"))
b = int(input("Enter a second side:"))
hypo = ((a**2+b**2)**0.5)
print("hypothesis is  ",hypo)'''


# factorial num.
'''n = int(input("Enter num n:"))
fact = 1

for i in range(1,n+1):
    fact *= i
print("Factorial num is",fact)
'''
#factorial num.(120)
'''n = 10
fact = 1
for i in range(1,11):
    fact *= i
print("factorial num is",fact)'''


# fibonacci series.
'''n = int(input("Enter n:"))
a = 0
b = 1
if n ==1:
    print(a)
else:
    for i in range(1,n+1):
        c = a+b
        a = b
        b = c
        print(c)'''



# armstrong number().

'''
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
power = len(str(num)) 

while temp > 0:  
    digit = temp % 10  
    sum += digit ** power  
    temp //= 10  

if num == sum:  
    print(num, "is an Armstrong number")  
else:  
    print(num, "is not an Armstrong number")  '''


# even 0dd .
'''n = int(input("enter number n:"))
if n % 2== 0:
    print("Even number")
else:
    print("Odd number")'''


'''for i in range(1,10):
    if i % 2 != 0:
        print(i)'''


#palindrome:
'''word = input("Enter word:")
reverse = ""
for char in word:
 reverse = char + reverse
if reverse == word:
    print("Yes, its a palindrome string")

else:
    print("Not, a palindrome string")'''



# print(1234,12345,123456)
'''n = int(input("Enter a number of n:"))
for i in range(n):
    for j in range(1,n+1):
        print(j,end = "")
    print()'''

# using if statement.
'''age = int(input("Enter age :"))

if age > 18:
    print("You are capable for licence")
print ("Ypu are not capable for licence")'''

# if else (statement)
'''age = int(input("Enter age:"))
if age >= 18:
    print("You are capable for licence")
else:
   print ("You are not capable for licence")'''

# if... elif....else:(statement)
'''handsome = True
Good_salary = True

if handsome == "True" and  Good_salary == "True":
    print("You will merry with super model:")
elif handsome != "True" and  Good_salary == "True":
    print("you will merry with beauty full girl")
elif handsome == "True" and  Good_salary != "True":
    print("You will merry with a girl")
else:
    print("depends of god!")'''

#nested if .
'''age = int(input("Enter age:"))
own_car = True
if age > 18:

    if own_car == True:
        print("Drive your car")
    else:
        print("Work hard & buy a new car")
else:
    print("firstly bde to ho jao")'''


#pyramid.
'''blocks = int(input("Enter a number of blocks:"))
height = 0
layer = 0
while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1
print("The height of is",height)'''



'''numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i)'''

'''num = []
for i in range(10):
    print(i)
    num[i] = i+1'''

'''num = [10,20,30,40,50,60,70,80,90,100]
for i in range(len(num)):
    num[i] = num[i] + 1
print(num)'''



'''Write a program to calculate the sum of all the elements in the list:
list=> my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''
'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total_sum = 0
for i in my_list:
    total_sum += i
print("Sun of all elements:",total_sum)'''

#Q1--sum of list all elements
'''numbers  = [10,20,30,40,50,60,70,80,90,100]
total_sum = sum(numbers)
print("the sum of all elements in a list",total_sum)'''



#Q6--find the max numbers in a list
'''numbers  = [10,20,30,40,50,60,70,80,90,100]
max_numbers = max(numbers)
print(max_numbers)'''

#Q7--find the min numbers in a list
'''numbers  = [10,20,30,40,50,60,70,80,90,100]
min_numbers = min(numbers)
print(min_numbers)'''

#Q8--reverse a list
'''numbers  = [10,20,30,40,50,60,70,80,90,100]
numbers.sort(reverse = True)
print(numbers)'''

#Q9--insert number in a list
'''numbers  = [10,20,30,40,50,60,70,80,90,100]
numbers.insert(1,5000)
print(numbers)'''

#Q10--remove elements in a list
'''my_list = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
 
my_list.remove(21)
print(my_list)'''


#Q4--- program to blank list update.
'''numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)'''

#Q sum list elements.
'''numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = sum(numbers)
print(numbers)'''


'''num1 = 1
num2 = 10
print("value of num1 and num2",num1,num2)

num3 = 0

num3 = num1
num1 = num2
num2 = num3

num1,num2 = num2,num1
print("After swapping")
print("value of num1 and num2",num1,num2)'''

'''numbers = [10,1,8,3,5]
numbers[0],numbers[4] = numbers[4],numbers[0]
numbers[1],numbers[3] = numbers[3],numbers[1]
print(numbers)'''


'''beatles = []
print(beatles)
beatles.append("john Lennon" )
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)
for i in range(1,3):
    name = input("Enter name of members ") #Stu Suteliffe, Pete Best
    beatles.append(name)
print(beatles)

del beatles[3:5]
print(beatles)
beatles.insert(0,"Ringo Starr")
print(beatles)'''

'''numbers = [10,20,30,40,50]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])'''


'''numbers = [10,20,30,40,50]
count = 0
print(numbers[count])
count += 1
print(numbers[count])
count += 1
print(numbers[count])
count += 1
print(numbers[count])
count += 1
print(numbers[count])


numbers = [10,20,30,40,50]
numbers[0] = 111
print(numbers)


numbers = [10,20,30,40,50]
numbers[1] = numbers[4]

print(numbers)'''

'''numbers = [10,20,30,40,50]
del numbers
print(numbers)'''


'''numbers = [1,2,3,4,5]
print(len(numbers))
del numbers[-1]
print(numbers)

numbers = [10,20,30,40,50]
del numbers[len(numbers)-1]'''


'''numbers = [10,20,30,40,50]
n = int(input("enter n:"))
numbers[len(numbers) // 2] = n
print(numbers)'''


'''list = [10,1,8,3,5]
#for traversing list
for count in range(len(list)):
    #print("index:",count)
    #print("element",list[count])
    print("list[",count,"] => ",list[count])'''



'''list = [10,1,8,3,5]
for element in list:
    print("element => ",element)'''


'''num1 = 5
num2 = 10
print(num1)
print(num2)

num3 = num1
num1 = num2
num2 = num3
print(num1)
print(num2)'''

'''num1 = 5
num2 = 10
print(num1,num2)

num1,num2 = num2,num1
print(num1,num2)'''


'''numbers = [10,1,8,3,5]
print(numbers)
numbers[0],numbers[4] = numbers[4],numbers[0]
print(numbers)

numbers[1],numbers[3] = numbers[3],numbers[1]

print(numbers)'''


'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
● step 1: create an empty list named beatles;
● step 2: use the append() method to add the following members of the band to the list: John Lennon,
Paul McCartney, and Geroge harrison;
● step 3: use the for loop and the append() method to prompt the user to add the following members of
the band to the list: Stu Sutcliffe, and Pete best:
● step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
● step 5: use the insert() method to add Ringo Starr to the beginning of the list.
 '''


'''beatles = []
print(beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("Geroge harrison")
print(beatles)

for i in range(1,2):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete best")
print(beatles)

del beatles[3]
del beatles[3]
print(beatles)

beatles.insert(0,"Ringo starr")
print(beatles)'''



'''list = [1,2,3,4,5]
list2 = []
add = 0
for number in list:
    add += number
    list2.append(add)
print(list2)
print(list)'''

#list traversing

'''You
can
use
for loop to traverse a list.Can you write a program to do that?'''
'''num = [10,20,30,40,50,60,70,80,90,100]

for count in range(len(num)):
    print(num[count])'''


#list traversing another way.
'''num = [10,20,30,40,50,60,70,80,90,100]
for i in num:
    print(i)'''


#you can use for loop to add data to the list as well.
'''Write a program to insert 10 numbers starting from 1 to 10 to a list list = []'''
#USing for loop:
#numbers = [i for i in range(1,11)]
#print(numbers)


#Swapping list members
'''name = ["suraj","mayank","sourabh","kanak","ajay"]
print(name)
name[0],name[4] = name[4],name[0]
print(name)'''

#swapping list numbers
'''numbers = [1000,20,30,40,50,60,70,200000]
print(numbers)
numbers[0],numbers[7] = numbers[7],numbers[0]
print(numbers)'''

#--------list add string and swap string
'''numbers = []
print(numbers)

numbers.append("suraj")
numbers.append("mayank")
numbers.append("harsh")
numbers.append("ajay")
print(numbers)

numbers[0],numbers[3] = numbers[3],numbers[0]
print(numbers)'''

#----swapping value in variable (a,b ) using third variable
'''a = 5
b = 10
c = 0
print(a,b)
c = a
a = b
b = c
print(a,b)'''

'''my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)
'''

#---calculate sum using for loop.

'''numbers = [5,5,5,5,5,5,5,5]
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)'''


'''lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)
print(lst)'''


#--Calculate sum 0=of given list.

'''numbers  =[10,20,30,40]
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)'''


#update existing list.
'''num = [10,20,30,40,50,60]
print(num)

for count in range(10):
    num[count] += 1

print(count)'''


#-----
'''numbers = [10,20,30,40,50,60,70]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)'''

#-----
'''numbers = [10,20,30,40,50,60,70,80,90,100]

for i in range(7):
      numbers[i] += 1
print(numbers)'''


#--Empty list update---using fro loop---
'''num = []
for i in range(1,11):
    num.append(i)
print(num)'''


#-traversing a list.
'''num = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(num)):
    print(i)'''

#traversing a list.
'''num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)'''


'''numbers = [10,20,30,40,5,60,70,80]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)'''


'''numbers  =[10,20,30,40] 
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)'''

'''num = []
num.append(10)
num.append(20)
num.append(30)
num.append(40)
num.append(50)
print(num)

num[0],num[3]  = num[3],num[0]
print(num)'''



#numbers = [1,2,3,4,5]
#print(len(numbers))
#numbers.pop(0)
#numbers.pop()
#print(numbers)

'''num = []
for i in range(1,11):
    num.append(i)
print(num)'''

'''num = [10,20,30,40,50,60,70,80]
for i in range(len(num)):
    num[i] += 1
print(num)'''


'''lst = [9,1,3,4,7,8,6,5,2]

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
           
print(lst)'''


'''list1 = [1,2,3,4,5]
list2 = []
add  = 0
for num in list1:
    add += num
    list2.append(add)
print(list1)
print(list2)'''


#sort---list.
'''list = [10,4,2,7,8,1]
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)'''

'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
● step 1: create an empty list named beatles;
● step 2: use the append() method to add the following members of the band to the list: John Lennon,
Paul McCartney, and George Harrison;
● step 3: use the for loop and the append() method to prompt the user to add the following members of
the band to the list: Stu Sutcliffe, and Pete Best;
● step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
● step 5: use the insert() method to add Ringo Starr to the beginning of the list.
 
 '''
'''beatles = []
print(beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Herrison")
print(beatles)

for i in range(1,2):
   beatles.append("Stu Sutcliffe")
   beatles.append("Pete Best")
print(beatles)

del beatles[3]
del beatles[3]
print(beatles)

beatles.insert(0,"Ringo starr")
print(beatles)'''

'''a = 3
b = 1
c = 2
lst = [a, c, b]
lst.sort()
print(lst)
'''

'''a = "A"
b = "B"
c = "C"
d = " "
lst = [a, b, c, d]
lst.reverse()
print(lst)'''

'''list1 = [1]
list2 = list1
list1[0] = 2
print(list2)'''

'''lst = [5, 3, 1, 2, 4]

lst.sort(reverse = True)
print(lst)  # outputs: [4, 2, 1, 3, 5]
'''

'''list_1 = [1]
list_2 = list_1[:]  # स्लाइस का उपयोग करते हुए list_1 की पूरी कॉपी बनाते हैं
list_1[0] = 2
print(list_2)  # आउटपुट: [1]'''

#String(slicing):
'''name = "SurajPatidar"

print(name[5:10])
print(name[:10])
print(name[5:])
print(name[:])
print(name[-8:-3])
print(name[5::2])
print(name[::-1])'''

'''my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)'''

'''my_list = [1,4,6,7,10]
print(5 in my_list)
print(1 in my_list)
print(100 in my_list)'''

'''list = [17,3,11,5,1,9,7,15,13]
list = max(list)
print(list)'''


'''list = [10,20,50,100,30000,100,200,330]
largest = 0
for i in list:
    if i > largest:
        largest = i
print("largest numbers is",largest)'''

'''list = [1,2,3,4,5,6,7,8,9,0]
list.reverse()
print(list)'''

'''my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)'''

#---largest numbers find in list
'''list = [10,100,1500,130,900]
largest = 0
for i in list:
    if i > largest:
        largest = i
print(largest)'''


'''list = [2,4,6,1,8,10]
smallest = 0
for i in list:
    if i <= smallest:
        smallest = i
print(smallest)'''

'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
● step 1: create an empty list named beatles;
● step 2: use the append() method to add the following members of the band to the list: John Lennon,
Paul McCartney, and George Harrison;
● step 3: use the for loop and the append() method to prompt the user to add the following members of
the band to the list: Stu Sutcliffe, and Pete Best;
● step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
● step 5: use the insert() method to add Ringo Starr to the beginning of the list.'''

'''beatles = []
print(beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison ")
print(beatles)

for i in range(1,2):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
print(beatles)

del beatles[3]
del beatles[3]
print(beatles)

beatles.insert(0,"Ringo Starr")
print(beatles)'''


'''num = []
for i in range(1,11):
    num.append(i)
print(num)'''


'''Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.'''
'''number = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
number2 = []
for i in number:
    if i not in number2:
        number2.append(i)
print(number2)'''

'''my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)'''

'''num = [1,2,7,5,10,22,77,5,222,8,]
largest_number = 0
for i in num:
    if i > largest_number:
        largest_number = i

print(largest_number)'''

'''num = [1,2,7,5,10,22,77,5,222,8,]
smallest_number  = float("input")

for i in num:
    if i < smallest_number:
        smallest_number = i
print(smallest_number)'''

'''num = [1,2,7,5,10,22,77,5,222,8,]
sum = 0
for i in num:
    sum += i
print(sum)'''

'''lst = [9,1,3,4,7,8,6,5,2]

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)'''


'''numbers = [10,5,20,15,7,8]
numbers.sort()
print(numbers)'''


'''#list = [1,2,3,4,5,6,7,8,9,10]
list = [1,2,3,4,5,6,7,8,9]
print(list)

if len(list) // 2 % 2 == 0:
    t = len(list)  / 2
else:
    t = len(list)//2 - 1
    #typcasting float to int(t)
t = int(t)

for index in range(t):

    list[index],list[-(index+1)] = list[-(index+1)],list[index]
print("list after reverse",list)'''

# reverse list
'''list = [1,2,3,4,5,6,7,8,9,10]
list.reverse()
print(list)'''


'''list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_1)

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

list = [10,8,6,4,2]
new_list = list[1:3]
print(new_list)
'''

#find the largest element in list.
'''number = [17,3,11,5,1,9,7,15,13]
largest_number = 0
for i in number:
    if i > largest_number:
        largest_number = i
print("largest Number is ", largest_number)
'''


# find element in list:
'''number = [17,3,11,5,1,9,7,15,13]
found = 0
for i in range(len(number)):
    if number[i] == 5:
        print("Found 5 at index",i)
        found = 1
        break
if found == 0:
    print("sorry,5 is not found")'''


#-
'''chosen_number = [3,7,11,42,34,49]
draw_number = [5,11,9,42,3,49]
number_hit = 0
for i in chosen_number:
    if i in draw_number:
        number_hit += 1

print(number_hit)'''

#--list double element remove:
'''list =[1,2,4,4,1,4,2,6,2,9]
deleted = []
for index in range(len(list)-1):
    for index1 in range(index +1,len(list)):
        if index1 not in deleted:
            if list[index] == list[index1]:
                deleted.append(index1)
print(list)
print(deleted)
deleted.sort()
print(deleted)
for index in range(len(deleted)):
    del list[deleted[len(deleted)-(index+1)]]
print(list)'''



'''list = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in list:

        sum += i
print("list sum is", sum)'''

#delete double elements from a list:

'''numbers = [6,4,2,9,1,3,1,2,6]
new_numbers = list(set(numbers))

print(new_numbers)'''


# delete double elements from a list using for loop
'''numbers = [1,3,4,6,1,2,3,4,5,6,7]
new_numbers = []
for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print(new_numbers)'''




#list comprehension:

'''numbers = [12,45,34,8,10,3,100,120,43,65]
new_numbers = []
for i in numbers:
    if i > 3:
        new_numbers.append(i)

print(new_numbers)'''


#other way:
'''numbers = [12,45,34,8,10,3,100,120,43,65]
new_numbers = [numbers for numbers in numbers if numbers > 25]
print(new_numbers)
'''

#list comprehension for string:
'''fruit = ["apple","banana","cherry","kiwi"]
new_fruits = [fruit for fruit in fruit if  "a" in fruit]
print(new_fruits)'''





#usion long loop method:
'''fruits = ["apple","banana","cherry","kiwi"]
new_fruits = [ ]
for i in fruits:
    if "a" in i:
        new_fruits.append(i)
print(new_fruits)'''



#copy a list:
'''list = [1,2,3,4,5,6,7,8,9]
print(list)
new_list = list.copy()
print(new_list)'''


#list comprehension:

'''name = []
for i in range(1,9):
    name.append("WHITE_PAWN")
print(name)'''

#list comprehension : other way
'''name = []
name = ["WHITE_PAWN" for i in range(1,9)]
print(name)'''


#update the list 0,10 for all the square number:
'''number = []
for i in range(4):
   number.append( i ** 2)
print(number)'''


'''numbers =[1,2,3,1,4,4,4,4,4,4,4,5,6,7,8,2,]
new_number = []
for i in numbers:
    if i not in new_number:
        new_number.append(i)
print(new_number)'''


'''list =[1,2,4,4,1,4,2,6,2,9]
deleted = []
for index in range(len(list)-1):
    for index1 in range(index +1,len(list)):
        if index1 not in deleted:
            if list[index] == list[index1]:
                deleted.append(index1)
print(list)
print(deleted)
deleted.sort()
print(deleted)
for index in range(len(deleted)):
    del list[deleted[len(deleted)-(index+1)]]
print(list)'''

'''list = []
WHITE_PAWN = 1
#for i in range(8):
list = [WHITE_PAWN for i in range(8)]
   # list.append(WHITE_PAWN)
print(list)'''

'''square = []
square =[x ** 2 for x in range(10)]
print(square)
odds = [x for x in square if x % 2 != 0 ]
print(odds)'''





'''twos = []
twos = [2** i for i in range(8)]
print(twos)'''


'''board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
print(board)
'''







'''print(" "*5, end="*\n")

print(" "*4, " "*2, sep="*", end="*\n")

print(" "*2,  " "*6, sep="*", end="*\n")

print("*"*3," "*4,"*"*3 )

print("  *      *")
print(" "*2, " "*6, sep="*", end="*\n")
print(" "*2, " "*6, sep="*", end="*\n")

print(" "*1,"*"*8)'''


'''a  = 2
b = 2
c  = 2 +2
print("sum or a and b is", c)
c = a - b
print("difference of a and b is", c)
c = a * b
print("multiplication  and b is ",c)
c = a / b
print("division of a and b is",c)
c = a // b
print("division floored a and b is ", c)
c = a % b
print("remainder of a and b is ",c)
c = a ** b
print("a to the power b is",c)'''


# Logical operator:

'''x= 2

print(x < 5 and x < 10)

x =4

print(x < 5 or x < 4)

x = 11
print(not(x < 5 and x < 10))'''

#identity operator:
'''x = 5
y = 6
print(x is y)
print(x is not y)
'''


'''x = ['suraj']
y = ['suraj']
z = [x is not y]
print(z)'''


#Q(--Write a Python program to find the list of words that are longer than n from a given list of words.)

'''fruits = ["apple","banana","cherry","kiwi"]
n = 5
new_list = []
for element in fruits:
    if (len(element) > n):
        new_list.append(element)
print(new_list)
'''

#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or
# more and the first and last characters are the same. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
'''Sample_List = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in Sample_List:
    if i[0] == i[-1]:
        count += 1
print(count)'''



# remove duplicate numbers from a list:
'''list = [1,2,3,4,5,6,77,2,5,4,62,56,1,2,3,4,5]
duplicate_numbers = []
for element in list:
    if element not in duplicate_numbers:
        duplicate_numbers.append(element)
print(duplicate_numbers)'''


#----






#list _comprehension:
'''list = [20,3,40,50,60,70,0,80,90]
new_list = []
for i in list:
    if i > 50:
        new_list.append(i)
print(new_list)'''


#
'''square = []
square =[x ** 2 for x in range(10)]
print(square)
odds = [x for x in square if x % 2 != 0 ]
print(odds)'''


#list comprehension:

'''temps = [[0.0 for h in range(24)] for d in range(31)]
#print(temps)


total = 0.0
for day in temps:
    total += day[11]
average = total / 31
print(average)


highest = -100
for day in temps:
    for temps in day:
        if temps > highest:
            highest = temps
print("The highest temp was:",highest)'''


#rooms = [[[False for r in range(20)]for f in range(15)]for t in range(3)]
#print(rooms)

'''#avalible
row = 15
flor = 15
rooms = false

for rows in range(20):
    if rows[2][14][rows] == false
        print("vacant rooms")
    else:
        print("room is not vacant")'''


'''nums = [1,2,3]
vals = nums[-1:-2]
print(vals)'''


'''for i in range(1):
    print("#")
else:
    print("#")
'''


#Q 3 Write a Python program to get the largest number from a list
'''numbers = [10,20,34,23,440,324,2045,424,2424,353,4334,3353,]
largest_number = 0
for i in numbers:
    if i > largest_number:
        largest_number = i
print(largest_number)'''

#find smallest_number in list :
'''numbers = [10,20,34,23,440,324,2045,424,2424,353,4334,3353,]
smallest_number = numbers[0]
for i in numbers:
    if i < smallest_number:
        smallest_number = i
print(smallest_number)'''



#Remove Even Numbers from List | List: [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
'''List = [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
odd_list = []
for i in List:
    if i % 2 != 0:
        odd_list.append(i)
print(odd_list)'''


#Write a Python program to find the index of an item in a specified list. |
# List: [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7], find index of element 0
#List = [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]



'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
● step 1: create an empty list named beatles;
● step 2: use the append() method to add the following members of the band to the list: John Lennon,
Paul McCartney, and George Harrison;
● step 3: use the for loop and the append() method to prompt the user to add the following members of
the band to the list: Stu Sutcliffe, and Pete Best;
● step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
● step 5: use the insert() method to add Ringo Starr to the beginning of the list.
 '''

'''beatles = []
print(beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for i in range(1,2):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
    print(beatles)

del beatles[3]
del beatles[3]
print(beatles)

beatles.insert(0,"Ringo starr")
print(beatles)'''



'''Imagine you are creating a list to track the members of a fictional rock band. The band started with three members and later had some changes in the lineup.

Your task is to write a program that performs the following steps:

Step 1: Create an empty list named band_members.
Step 2: Use the append() method to add the following members to the band: "Alice Cooper", "Jim Morrison", and "Jimi Hendrix".
Step 3: Use a for loop and the append() method to prompt the user to add two more members of the band: "Janis Joplin" and "Mick Jagger".
Step 4: Use the del instruction to remove "Jim Morrison" and "Jimi Hendrix" from the list.
Step 5: Use the insert() method to add "Keith Richards" to the beginning of the list.
Step 6: Display the final list of band members'''

'''band_members =[]
print(band_members)

band_members.append("Alice Cooper")
band_members.append("Jim Morrison")
band_members.append("Jimi Hendrix")
print(band_members)

for i in range(1,2):
    band_members.append("Janis Joplin")
    band_members.append("Mick Jagger")
print(band_members)

del band_members[1]
del band_members[1]
print(band_members)

band_members.insert(0,"Keith Richards")
print(band_members)'''


#Write a Python program to find the second smallest number in a list. | List: [0, 3, 4, 7, 9]

'''list  = [0, 3, 4, 7, 9]

list.sort()
print(list)
second_smallest = list[1]
print(second_smallest)'''


#-Write a Python program to find the second largest number in a list. | [0, 3, 4, 7, 9]

'''numbers = [0, 3, 4, 7, 9]
numbers.sort()
print(numbers)
second_largest = numbers[-2]
print(second_largest)'''

#-Write a Python program to append a list to the second list. | List: [0, 3, 4, 7, 9], [3, 5, 7, 13]
'''num1 = [0, 3, 4, 7, 9]
num2 = [3, 5, 7, 13]
for i in num1:
    num2.append(i)
print(num2)'''






'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
● step 1: create an empty list named beatles;
● step 2: use the append() method to add the following members of the band to the list: John Lennon,
Paul McCartney, and George Harrison;
● step 3: use the for loop and the append() method to prompt the user to add the following members of
the band to the list: Stu Sutcliffe, and Pete Best;
● step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
● step 5: use the insert() method to add Ringo Starr to the beginning of the list.
 '''



'''beatles = []
print(beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for i in range(1,2):
    beatles.append(" Stu Sutcliffe")
    beatles.append("Pete Best")
    print(beatles)

del beatles[3]
del beatles[3]
print(beatles)

beatles.insert(0,"Ringo starr")
print(beatles)'''


#ascii value
#char = "a"
  
#print(ord(char))

#num = 66
#print(chr(num))

# write a program using loop to print 10 even numbers in reverse order:
# while loop
'''num = 20
while  num  > 0:
    print(num)
    num = num -2'''

# using for loop:
'''for i in range(20,0,-2):
    print(i)'''



# string is palindrome or not:
'''name = input("please enter name:")
reverse = ""
for char in name:
    reverse= char + reverse
if reverse == name:
    print("YES palindrome string")
else:
    print("NOT a palindrome string")'''




# function--
'''def message():
    print("Enter a value: ")
print("We start here.")
message()
print("We and here")'''


'''print("We start here.")
message()
print("We and here")
def message():
    print("Enter a value: ")
'''


'''def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())'''


'''def hello(name):
    print("Hello ", name)
name = input("Enter your name:")
hello(name)'''


#Write a Python program to find the sum of all elements in a 2D list.  [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]

'''numbers =  [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
total_sum = 0
for rows in numbers:
    for columns in rows:
        total_sum += columns
print("sum of all elements in a 2D list",total_sum)'''



'''def message(number):
    print("Enter a number:",number)
message(1)'''


'''def message(number):
    print("Enter a number:",number)

number  =1234
message(1)
print("number:",number)'''




'''def message(what,number):
    print("Enter",what,"number",number)

message("telephone",11)
message("price",5)
message("number","number")
'''


'''def introductions(first_name,last_name):
    print("Hello, my name is",first_name,last_name)

introductions(first_name = "James",last_name = "Bond")
introductions(last_name = "Skywalker",first_name = "Luke")'''


'''def adding(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)

#adding(1,2,3)
adding(c = 1,a= 2,b = 3)
adding(3,c = 1,b = 2)
adding(3,a = 1,b = 2)
'''



'''def add_numbers (a, c, b = 2):
    print(a+b+c)
add_numbers(a = 1, c = 3)'''



'''def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy new Year!")
#happy_new_year()
happy_new_year(False)'''



'''def boring_function():
    return 123
x = boring_function()
print("The boring_function has returned its result , It 's :",x)'''



'''def boring_function():
    print("'Boredom Mode' ON. ")
    return 123
print("The lesson is interesting")
boring_function()
print("This lesson is boring...")'''





#print(None + 2)




#None
'''value = None
if value is None:
    print("Sorry,you don't carry any value")'''


'''def list_sum(lst):
    s  = 0
    for elem in lst:
        s += elem

    return s
print(list_sum([5,4,3]))
#print(list_sum(5))
'''

'''def strange_list_fun(n):
    strange_list = []

    for i in range(0,n):
        strange_list.insert(0,i)
    return strange_list
print(strange_list_fun(5))
#print(strange_list_fun(50))
#print(strange_list_fun(100))'''



'''def hello():
    print("Namaste")

hello()'''



'''def greet_user(name):
    def say_hello():
        print(f"Namaste, {name}!")
    return say_hello

# Step 1: Naam lo
user_name = input("Apna naam daalein: ")

# Step 2: Function call karo aur greeting function lo
greeting = greet_user(user_name)

# Step 3: Jab chahein greet karo
print("Aapka welcome message:")
greeting()'''



# leap year

'''def is_year_leap(year):

    if year % 4 == 0  and  year % 100 != 0:
        return True

    elif year % 400 == 0:
        return True
    else:
        return False

test_data = [1900,2000,2016,1987]
test_results = [False,True,True,False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end = "")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")'''


'''def scope_test():
    x = 123
scope_test()

print(x)'''


'''def my_function():
    print("Do I know that variable?",var)
var  = 1
my_function()
print(var)'''


#Globle keyword:
'''def my_function():
    global var
    var = 2
    print("Do i know that variable?",var)
var= 1
my_function()
print(var)'''


#sum numbers;

'''def sum(n1,n2):
    add = n1 + n2
    print(add)
    return add
sum(2,3)'''

'''def print_hello():
    print("Hello World")
print_hello()'''


'''def scope_test():
    x = 123
scope_test()
print(x)'''


'''def message():
        alt = 1
        print("Hello, World!")
message()
print(alt)
'''
'''
def my_function(n):
    print("I got ",n)
    n += 1
    print("I have ",n)

var = 1
my_function(var)
print(var)'''


'''def my_function(my_list_1):
    print("print #1:",my_list_1)
    print("print #2:", my_list_2)
    my_list_1 = [0,1]
    print("print #3:",my_list_1)
    print("print #4:",my_list_2)

my_list_2 = [2,3]
my_function(my_list_2)
print("print #5:",my_list_2)'''



'''def my_function(my_list_1):
    print("print #1:",my_list_1)
    print("print #2:", my_list_2)
    del my_list_1[0]
    print("print #3:",my_list_1)
    print("print #4:",my_list_2)

my_list_2 = [2,3]
my_function(my_list_2)
print("print #5:",my_list_2)'''



# bmi calculate(user input)

'''Weight = float(input("Enter weight "))
Height = float(input("Enter a height; "))
def bmi(weight,height):
    return weight / height **2
print(bmi(Weight,Height))'''

# Evaluation BMI and converting imperial units to metric units:
'''def bmi(weight,height):
    if height < 1.0 or height > 2.5 or \
        weight < 20 or weight > 200:
        return None
    return weight / height **2
print(bmi(352.5 , 1.65))'''


# convert imperial unit to metric once(lb to kg )(364)

'''def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))'''


#-----ft and inch to meter
'''def ft_and_inch_to_m(ft,inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1,1))'''

#----
'''def ft_and_inch_to_m(ft,inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(6))'''



#---The code is able to answer the question: what is the BMI of a person 5'7" tall and weighing 176 lbs?
'''def ft_and_inch_to_m(ft, inch = 0.0):
          return ft * 0.3048 + inch * 0.0254
def lb_to_kg(lb):
          return lb * 0.4535923
def bmi(weight, height):
          if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
              return None
          return weight / height ** 2
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))'''


# factorial numbers:
'''
n = int(input("Enter number of n  :"))
def factorial_function(n):
    if n < 0:
        return None
    if n < 2 :
        return 1
    product = 1
    for i in range(2,n+1):
        product *= i
    return product

for n in range(1,6):
    print(n,factorial_function(n))
'''





# calculate geometric mean(by function)(formula = (a*b)/(b+a)

'''def calculate_geometric_mean(a,b):
    mean = (a*b)/(b+a)
    print(mean)
a = 5
b = 6
calculate_geometric_mean(a,b)

#c = 8
#d = 9
calculate_geometric_mean(8,9)

n1 = 12
n2 = 15
calculate_geometric_mean(n1,n2)

#by user input
num1 = int(input("Enter n:"))
num2 = int(input("Enter n:"))
calculate_geometric_mean(num1,num2)'''


# calculate greater number by function:
'''def calculate_greate(a,b):
    if (a>b):
        print("First number is greater")
    else:
        print("second number is greater of equal")

a = 5
b = 3
calculate_greate(a,b)

num1 = 10
num2 = 20
calculate_greate(num1,num2)'''


# calculate factorial number using for loop:
'''n = int(input("Enter a number :"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("factorial is ",fact)'''


# using while loop factorial number
'''n = int(input("Enter a number of n  :"))
fact = 1
i = 1
while i <= n :
    fact = fact * i
    i = i +1
print("factorial is ",fact)
'''



# Area calculation on Triangle:
'''a  = int(input("Enter a number of a :"))
b = int(input("Enter a number of b :"))
c = int(input("Enter a number pf c :"))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Triangle area of :",area)'''


#def function of area calculation
'''def area_of_triangle(a,b,c):
    s = (a +b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(area)

#a = int(input("Enter number a :"))
#b = int(input("Enter number b :"))
#c = int(input("Enter number c :"))


a = 50
b = 50
c = 18
area_of_triangle(a,b,c)'''




# def function factorial number calculate
'''def factorial_number(n):
    fact = 1

    for i in range(1,n+1):
        fact = fact * i
    print(fact)

factorial_number(5)'''

# fibonacci series by function:
'''n = int(input("Enter number n :"))
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        n = fib(n-1) + fib(n-2)
fib(n)
print(n)'''



#area calculation of square two side
'''def area_calculation(a,b):
    c = a * b
    print(c)

a = int(input("Enter a :"))
b = int(input("Enter b :"))
area_calculation(a,b)'''


'''
def cheak_Even_Odd(n):
    if n % 2 == 0:
        return "Even"

    else:
        return "Odd"


n = int(input("Enter number n:"))
# print(cheak_Even_Odd(n))
result = cheak_Even_Odd(n)
print(result'''



'''def fac(n):
    if n <= 1:
        print("n = ",n )
        print("returning 1 from less than equal to 1")
        return 1
    else:
        print("calling fac(",n-1,")")
        res = fac(n-1) * n
        print("finally returning res:",res)
        return res

print(fac(5))'''


'''def fibo(n):
    if n < 2:
        return 1
    else:
        result = fibo(n -1) + fibo(n-2)
        print(result)
        return result


n = int(input("enter n:"))
print(fibo(n))'''



# print fibonacci series using function  input number of n :

'''def fib(n):
    if n == 0  or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter a number of n :"))
i = 0
while i < n:
    print(fib(i),end = " ")
    i += 1'''


# tuple
'''tuple_1 = (1,2,3,4,5)
tuple_2 = 1,2,3,4,5
print(tuple_1)
print(tuple_2)
print(type(tuple_1))
print(type(tuple_2))



empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

new_tuple = 1,
print(new_tuple)
print(type(new_tuple))


my_tuple = (1,10,100,1000)
#my_tuple.append(10000)
#del my_tuple[0]
#my_tuple[1] = -10
print(len(my_tuple))


tuple_1 = (1,2,3,4,5)
tuple_2 = 6,7,8,9,10
tuple_3 = tuple_1+tuple_2
print(tuple_3)
tuple_4 = tuple_3 * 4
print(tuple_4)

#loop
tuple_1 = (1,2,3,4,5)
for element in tuple_1:
    print(element)

# convert list to tuple:
my_list = [2,4,6]
tup = tuple(my_list)
print(tup)
print(type(tup))

#swapping tuple:
var = 123
t1 = (1,)
t2 = (2,)
t3 = (3,var)
t1,t2,t3 = t2,t3,t1
print(t1,t2,t3)'''


# dictionary:
'''dictionary = {"cat": "chat", "dog": "chien","horse":"cheval"}
phone_numbers = {"boss": 5551234567, "suzy": 22657854310}
empty_dictionary = {}
print(dictionary)
print(type(dictionary))
print(phone_numbers)
print(type(phone_numbers))
print(empty_dictionary)
print(type(empty_dictionary))
print(dictionary["cat"])
#print(phone)numbers["suzy"])'''



'''dictionary = {"cat","chat","dog","chien","horse","cheval"}
words = {"cat","lion","horse"}
for word in words:
    if word in dictionary:
        print(word, "->", dictionary)
    else:
        print(word,"is not in dictionary")'''


'''
dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
for key in dictionary.keys():
    print(key, "->",dictionary[key])'''


'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
for french in dictionary .values():
    print(french)'''


'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
print(dictionary)
dict_2 = dictionary.copy()
print(dict_2)
'''

'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
dictionary["cat"] = "lock"
print(dictionary["cat"])
print(dictionary)'''

# add
'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
dictionary["adam"] = 123
print(dictionary)'''


#delete
'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval","Adam":"suraj"}
del dictionary["Adam"]
print(dictionary)'''


#popitem
'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
dictionary.popitem()
print(dictionary)'''

#delete dict...
'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
dictionary.clear()
print(dictionary)'''



'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
for i in dictionary:
    print(i , dictionary[i])'''

'''
dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
phone_numbers = {"boss": 5551234567, "suzy": 22657854310}
print(dictionary["cat"])
print(phone_numbers["suzy"])'''


''''dictionary ={"name": "suraj" , "num": 123}
dictionary["num"]  = 9753
print(dictionary)'''



'''dictionary ={"name": "suraj" , "num": 123}
dictionary["class"] = "5th"
print(dictionary)'''

# print fibonacci numbers using recursion:
'''def fib(n):
    if  n == 0 or n == 1:
        return n 
    else:
        return fib (n-1) + fib (n-2)
    
n = int(input("Enter a number of n :"))
i = 0
while i < n :
    print(fib(i),end = " ")
    i += 1'''


'''dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
for key ,value in dictionary.items():
    print(dictionary,"->",key, ":",value)
    '''

'''
dictionary = {"cat": "chat", "dog":"chien","horse":"cheval"}
print(dictionary)
dictionary.update({"zadam": "zadaam" })
print(dictionary)
'''


#---tuples dictionary can work together:
'''school_class = {}
while True:
    name = input("Enter the student's name:")
    if name == "":
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0,11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter  = 0
    for score in school_class[name]:
        adding += score
        counter = 1
    print(name,":",adding/counter)'''


#---
#my_tup = (1,2,3)
#print(my_tup[2])

'''tup = 1,2,3
a,b,c = tup
print(a*b*c)'''

#---count tup(duplicate number)
'''tup = (1,2,3,2,4,5,6,2,7,2,8,9)
duplicates = tup.count(2)
print(duplicates)'''


#--
'''d1 = {"Adam smith": "A","Judy Faxton": "B+"}
d2 = {"Mary louis": "A","Fatrick white": "C"}
d3 = {}
for item in (d1,d2):
    d3.update(item)
print(d3)'''

# convert list to tuple using tuple method
'''my_list = ["car","Ford","Flower","Tulip"]
t = tuple(my_list)
print(t)'''

#convert tuple to dictionary:
'''colors = (("green","#008000"),("blue","#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)'''



# reverse a tuple:
'''tuples = (5,4,3,2,1)
print(tuples)
for i in reversed(tuples):
    print(i,end = " ")'''


# reverse tuple:
'''tuples = (1,2,3,4,5,6)
list = []
for i in reversed(tuples):
    list.append(i)

output  = tuple(list)
print(output)'''


# set deta type:
'''name= {"john","marry","dav"}
print(name)
print(name)
print(name)'''


'''The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
● step 1: create an empty list named beatles;
● step 2: use the append() method to add the following members of the band to the list: John Lennon,
Paul McCartney, and George Harrison;
● step 3: use the for loop and the append() method to prompt the user to add the following members of
the band to the list: Stu Sutcliffe, and Pete Best;
● step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
● step 5: use the insert() method to add Ringo Starr to the beginning of the list.
 '''

'''beatles = []
print(beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)
for i in range(1,2):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
print(beatles)
del beatles[3]
print(beatles)
beatles.insert(0,"Ringo Starr")
print(beatles)'''

#--recursion using print fibonacci series :
'''def fib(n):
    if n == 0 or n == 1 :
        return n
    else:
        return fib(n-1)+fib(n-2)
n = int(input("Enter a number of n:"))
i = 0
while i < n:
    print(fib(i),end=" ")
    i += 1

# factorial using recursion:
def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)
n = int(input("Enter a number of n:"))
result = n * fact(n-1)
print(result)'''


#--factorial using recursion:
'''def fact(n):
    if n < 0:
        return "Negative numbers ka factorial nhi hota"
    elif n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)
n = int(input("Enter a number of n : "))
result = fact(n)
print(result)'''


#--fibonacci using recursion:
'''def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n = int(input("Enter a number of n : "))
i = 1
while i < n :
    print(fib(i),end = " ")
    i += 1
'''
'''
word = "hello"
print(len(word))

word = ""
print(len(word))

word = "A\"j"
print(len(word))

word = " "
print(len(word))

word = 

print(len(word))

word = "Suraj\nPatidar"
print(len(word))
print(word)

#string operation

StringOne = "ONE"
StringTwo = "TWO"

print(StringOne + StringTwo)
print(StringOne * 4)
print(4*StringTwo)

# ord function to print ascii value

print(ord("a"))
print(ord(" "))
#print(ord(""))

#chr function
print(chr(97))
print(chr(98))
print(chr(ord("A")))

#indexing string
word = "My string is awesome !"
print(word[5])
print(word[4])

for index in range(len(word)):
    if word[index] == "a" or \
        word[index] == "e" or\
        word[index] == "i" or\
        word[index] == "o" or\
        word[index] == "u":
        print("1",end = "")
    else:
        print(word[index],end = "")
print(word)


for char in word:
    print("char:", char)
'''

'''alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("f"  not in alphabet)
print("fab" in alphabet)

# string m word change to space
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet = alphabet[:12] +" "+ alphabet[13:]
print(alphabet)

#other way loop
result = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
for element in alphabet:
    if element == "m":
        result += " "
    else:
        result += element
print(result)

# min()  function using string

print(min("aAbByYzZ"))

t = 'The knight Who Say "Ni!"'
print('['+min(t)+']')


#maxxx

print(max("aAbByYzZ"))

t = 'The knight Who Say "Ni!"'
print('['+max(t)+']')

t = [0,1,2]
print(max(t))

#method index

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.index("y"))
print(alphabet.index("x"))
print(alphabet.index("c"))

#string convert to list or tuple

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(list(alphabet))

#count element in "string"
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.count("a"))

s1 = "where are the"
s2 = s1.split()
print(s2[-2])


'''
'''string = "TO be or not to be, that is the question"
s2 = string.split()
print(s2)'''
'''
def split(string):
    s2 = string.split()
    print(s2)

split("To be or not to be, that is the question")
split("To be or not to be, that is the question")
split(" ")
split("abc")
split("")'''

'''
def mySplit(str):
    result = []
    tempResult = ""
    for index in range(len(str)):
        if str[index] == " ":
            result.append(tempResult)
            tempResult = ""
        elif index == len(str)-1:
            result.append(tempResult+str[len(str)-1])
            tempResult = ""
        else:
            tempResult += str[index]
    return result

print(mySplit("To be or not to be , that is the question"))
print(mySplit("To be or not to be, that is the question"))
print(mySplit)'''


'''

num_patterns = [
     """
###
# #
# #
# #
###""",
 """
  #
  #
  #
  #
  #""",
 """
###
  #
###
#  
###""",
     """
###
  #
###
  #
###""",
"""
# #
# #
###
  #
  #""",
    """
###
#  
###
  #
###""",
   """
###
#  
###
# #
###""",
"""
###
  #
  #
  #
  #""",
"""
###
# #
###
# #
###""",
    """
###
# #
###
  #
###"""
    ]

number = input("Please enter a positive number :")

for i in number:
    digit = int(i)
    print(num_patterns[digit])'''


#endswith(methuds)
'''
t = "Zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#find()
t = "theta"
print(t.find("eta"))
print(t.find("et"))
print(t.find("the"))
print(t.find("ha"))


#find()
print('kappa'.find('a',1,4))
print('kappa'.find('a',2,4))

#isalnum()  methods

print('lamda30'.isalnum())
print('lamda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print(' '.isalnum())
print(' '.isalnum())'''

'''
#isalpha()

print("mooo".isalpha())
print("mu40".isalpha())

#isdigit()
print('2018'.isdigit())
print('Year2019'.isdigit())

#isupper()
print("mooo".isupper())
print('MOO'.isupper())

#islower()
print("mooo".islower())
print('MOO'.islower())

#join() methoud  --convert multi string to 1 string
print(",".join(["omicrone","pi","rho"]))

#lower()
print("SiGmA=50".lower())

#lstrip()
str = "  abc  ".lstrip()
print("["+str+"]")
print("www.cisco.com".lstrip("w."))
'''
#replace()
'''print("www.netacad.com".replace("netacad.com","pythoninstitute.ora)"))
print("this is it!".replace("is","are"))
print("apple juice".replace("juice"," "))
print("applejuice".replace("","-"))

#rfind()
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta",9))
print("tau tau tau".rfind("ta",3,9))

#rstrip
print("["+ "  upsilon  ".rstrip()+"]")
print("cisco.com".rstrip(".com"))'''



# comprssion string (ASCII value )

'''print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
print('10' < 10)
print('10' > 10)'''

#sorted strings
'''my_string_list = ['omega','alpha','pi','gamma']
my_string_list2 = sorted(my_string_list)
print(my_string_list)
print(my_string_list2)

#--
my_string_list = ['aaaaa','aaaa','abaa','aaaac']
print(my_string_list)

#sort(string/list)

my_string_list = ['omega','alpha','pi','gamma']
print(my_string_list)
my_string_list.sort()
print(my_string_list)

#int convert to (string)
number = 10
print(type(number))
string = str(number)
print(string)
print(type(string))

#float cov=nert to (str)

flot_num = 10.5
print(type(flot_num))
string = str(flot_num)
print(string)
print(type(string))'''


# THe caeser cyper: encription program
'''
text = input("Enter your massage:")
cipher = ' '
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char)+1
    if code > ord('Z'):
        code  = ord('A')
    cipher += chr(code)

print(cipher)'''

#decrypting a massage
'''cipher = input("Enter your massage:")
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char  =  char.upper()
    code = ord(char)-1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)'''

# THE NUMBER PROSESOR
'''line = input("Enter a line of numbers- separate them with spaces: ")
string = line.split()
total = 0

try:
    for substr in string:
        total += float(substr)
    print("The total is ",total)
except:
    print("substr,is not a number")'''

#exeptions
'''try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero divisible!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END")'''



'''try:
    y = 1 / 0

except ZeroDivisionError:
    print("Zero divisible!")

except ArithmeticError:
    print("Arithmetic problem!")

print("THE END")'''


#--
'''def bad_fun(n):
    try:
        return 1/ n
    except ArithmeticError:
        print("Arithmetic problem !")
        return None

bad_fun(0)
print("THE END.")'''

'''def bad_fun(n):
        return 1/n
    try:
        bad_fun(0)
    except ArithmeticError:
        print("What happend? An exception was raised")


print("THE END.")
'''

#--raise Exeption:
'''def bad_fun(n):
    if n == 0:
        print("Now i am going to raise an expetion manually")
        raise ZeroDivisionError
    return 1 / n


try:
    bad_fun(0)
except ArithmeticError:
    print("What happend? An exception was raised")

print("THE END.")'''





'''def bad_fun(n):
    if n == 0:
        print("Now i am going to raise an expetion manually")
        raise
    return 1 / n


try:
    bad_fun(0)
except ArithmeticError:
    print("What happend? An exception was raised")
except Exception:
    print("Exception problem!")
print("THE END.")'''


#assert--
'''
import math
x = float(input("Enter the value:"))
assert x >= 0.0

x = math.sqrt(x)
print(x)'''

# assertion error
"""from math import tan,radians
angel = int(input("Enter integral angel in degrees: "))

assert angel % 180 != 90
print(tan(radians(angle)))"""#----------------------------------------------------

#----
'''the_list = [1,2,3,4,5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False
print("Done")'''


#KeybordIntrupt ERROR

'''from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")'''


#--OverflowError

'''from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print("The number is too big")'''






#object oriented

'''class MyClass:
    pass

my_class_object = MyClass()
print(my_class_object)
print(type(my_class_object))'''

'''stack = []
def push(val):
    stack.append(val)
    print(stack)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)
print(pop())
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)

'''

'''class Stack:
    def __init__(self):
        print("Constructer running!")
        self.__stack = []

stack_object = Stack()
print(stack_object.stack)
print(len(stack_object.stack))
print(type(stack_object.stack))'''



#stack--
'''class Stack:
    def __init__(self):
        print("constructer Running!!")
        self.__stack = []

    def push(self,val):
        self.__stack.append(val)
        print(self.__stack)

    def  pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

    def traverse(self):
        print(self.__stack)

stack_object = Stack()
print(stack_object)
stack_object.push(1)
stack_object.push(2)
stack_object.push(3)
stack_object.push(4)
stack_object.push(5)
stack_object.push(6)
stack_object.push(7)
stack_object.pop()
stack_object.traverse()
stack_object.pop()
stack_object.traverse()
stack_object.pop()
stack_object.traverse()
stack_object.pop()
stack_object.traverse()
stack_object.pop()
stack_object.traverse()
'''


#assignment--
#reverse a string without using slice
#hello
'''def reverse_string(s):
    result = ""
    for i in s:
        result = i + result
    return result

print(reverse_string("hello"))'''


#swpping list elements:(swap index 1 to index 3)

# list = [10,30,90,40,20,]
#
# temp = list[1]
#
# list[1] = list[3]
# list[3] = temp
# print(list)


#
# dict ={
#     'a':12,
#     'b':10,
#     'c':5
# }
# print(sum(dict.values()))


#factorial using recursion
# def fact(n):
#     if n == 1 :
#         return 1
#     else:
#         result = n * fact(n-1)
#         return result
#
# print(fact(5))




# #fibonacci using recursion
# def fib(n):
#     if n <= 0 :
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = fib(n - 1) + fib(n - 2)
#         return result
#
#
# print(fib(n))


# pre define module:

# import calendar
# print(calendar.month(2080,7))

# import keyword
# print(keyword.kwlist)


# user difine module



#f"string"

# latter = "hello my name is suraj and i am from country"
# name = "suraj patidar"
# country = "india"
#
# print(f"hello my name is {{name}} and i am from {{country}}")
# print(f"hello my name is {name} and i am from {country}")






'''list = [1,2,3,4,5]
sum = 0
for i in list:
    sum += i
print(sum)'''



#-Write a Python function that takes two lists and returns True if they have at least one common member.


'''def common_member(list1,list2):
    for item in list1:
        if item in list2:
            return True

    return False

print(common_member(list1 = ["suraj","mayank","aabid"],list2 =["suraj","mayank","aabid"] ))'''




#--Write a Python program to get the smallest number from a list

# list = [1,4,2,3,6,1,2,3,1,3,4,2]
#
# smallest_number = list[0]
#
# for i in list:
#     if i <= smallest_number:
#         smallest_number = i
#
# print(smallest_number)



# fibonacci using reccursion
'''
def fib(n):
    if n == 0 :
        return 1

    elif n == 1:

        return 1
    else:
        total= fib(n-1)+fib(n-2)
        return total

n = int(input("Enter a number of n:"))
print("Fibonacci series")

for i in range(n):
    print(fib(i),end = " ")'''



#factorial using recursion

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#          return n * fact(n-1)
# n = int(input("Enter a number of n:"))
# print(fact(n))

# #oop(Class)
#
# class Faculty:
#     def put_data(self):
#         self.id = int(input("Enter faculty id:"))
#         self.name = input("Enter faculty name:")
#         self.salary = float(input("Enter faculty salary"))
#     def display(self):
#         print("faculty id",self.id)
#         print("faculty name",self.name)
#         print(" faculty salary",self.salary)
#
# a = Faculty()
# a.put_data()
# a.display()


#--Remove Even Numbers from List | List: [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
# List = [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
#
# new_list = []
#
# for i in List:
#
#     if i % 2 == 1:
#
#         new_list.append(i)
#
# print(new_list)


#-Write a Pvthon program to generate and print a list of the first 5 and last 5
# elements where the values are sauare numbers between 1 and 30(both included).
#
# square = []
#
# for i in range(1,31):
#     square.append(i*i)
#
# result = square[:5]+square[-5:]
#
# print(result)


#--Check If All Numbers Are Prime | Lists: [0, 3, 4, 7, 91, [3, 5, 7, 131, [1, 5, 31

'''list = [0, 3, 4, 7, 91, [3, 5, 7, 131, [1, 5, 3]]]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

List = [0, 3, 4, 7, 9]

all_prime = all(is_prime(i) for i in List)

print("All numbers are prime?" , all_prime)'''

#--count positive number in a list.

'''list = [1,-2,3,-4,5,6,-7,-8,9,10]

positive_list = []

for i in list:
    if i >= 1:
        positive_list.append(i)
print(positive_list)
print(len(positive_list))'''


#--sum of even number (n):

'''n = int(input("Enter a number n:"))
sum = 0
for i in range(n):
    if i % 2 == 0:
        sum += i

print(sum)
'''


#--multiplication table print 10\using continue stetement
'''n = 1

for i in range(1,11):
    if i == 5:
        continue
    result = n * i
    print(f"{n}x{i}= {result}")
'''

# using dual loop
'''n = 2

for i in range(1,5):

    result = n * i
    print(f"{n}x{i}= {result}")

for i in range(5,11):
    result = n * i
    print(f"{n}x{i}= {result}")'''

#Reverse a string using loop:

# my_string = "Suraj"
# reverse_string = ""
#
# for i in my_string :
#     reverse_string = i + reverse_string
#
#
#
# print(reverse_string)


#-find the first non reapetad character:
'''
string = "teeter"

for i in string:

    if string.count(i) == 1:
        print("char is:", i)
        break'''


#factorial  using while loop:

# num = 5
# fact = 1
#
# while num > 0 :
#
#     fact *= num
#     num -= 1
# print(fact)


#-valid loop (keep asking the user input until they enter number between 1 to 10:
'''
while True:
    num = int(input("Enter value below 1/10 mid::"))

    if 1 >= num <=10:
        print("Thanks ")

        break

    else:
        print("Invalid number please try again --")'''


#--prime number cheaker
'''
num = int(input("enter n:"))

is_prime = True

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            is_prime = False
            break'''


#
# str = "teeter"
#
# for i in str:
#     if str.count(i)==1:
#         print(i)

    
#--age group categorization:
# age = int(input("Enter age:"))
#
# if age < 13:
#     print("Child")
#
# elif 13<= age and age < 19:
#     print("Teenager")
#
# elif 20 <= age and age < 59:
#     print("Adult")
#
# else:
#     print("senior")


#--movi ticket pricing:
# age = int(input("Enter age:"))
# day = "wednesday"
# price = 12
# price = 12 if age >=18 else 8
#
# if day == "wednesday":
#     price = price - 2
#     print(price)

#-grade calculator:
# score  = int(input("Enter score:"))
#
# if score >= 101:
#     print("Please enter valid score:")
#     exit()
#
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >=70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
#
# else:
#     grade = "F"
# print("grade",grade)


#--Fruit ripeness checker:

# fruit = "Banana"
# colour ="Green"
#
# if fruit == "Banana":
#     if colour == "Green":
#
#         print("Unripe")
#
#     elif colour == "Yellow":
#         print("Ripe")
#
#     elif colour == "Brown":
#         print("OverRipe")
#
# else:
#     print("Not in my fruit list")



 #---Weather activity suggestion:
# weather = "snowy"
#
#
# if weather == "Sunny":
#     print("Go for a walk")
#
# elif weather == "Rainy":
#     print("read a book")
#
# elif weather == "snowy":
#     print("Build a snow man")


#--Transportation Mode selection:

# distance = int(input("Enter distance:"))
#
# if distance  < 3:
#     print("walk")
# elif 3 < distance <15:
#     print("bike")
#
# else:
#     print("car")


#--Coffe customization:
#
# order_size = "Medium"
# extra_shot = True
#
# if extra_shot:
#     coffe  = order_size + "Coff with an extra shot  "
#
# else:
#     coffe = order_size + "coffe"
#
#
# print("order:",coffe)


#function--

#--Besic function syntax:(write a function to calculate Square of a number:

# def square_of_num(num):
#     return num ** 2
#
# n = int(input("Enter n num:"))
# result = n ** 2
# print(result)


#--Function with multiple parameter:(Create a function that takes two number as parameter and returnn sum:

# def sum_of_two_num(n1,n2):
#     return n1 + n2
#
# n1 = int(input("Enter n1:"))
# n2 = int(input("Enter n2:"))
# print(sum_of_two_num(n1,n2))


#-Polymorphism in function:(Write a function multiply that multiplies two number, but can also accept and multiply string:

# def multiply(p1,p2):
#      return p1 * p2
#
# print(multiply(5,5))
# print(multiply("suraj",5))


#--Function returning Multiple Values:(Create a function that return both the are and Circumference of a circle given its radius:

# import math
#
# def circle_states(radius):
#     area =  math.pi * radius ** 2
#     circumference = 2 * math.pi ** radius
#     return area, circumference
#
#
# a,b = circle_states(4)
# a = round(a,2)   # round use for decimal value less:
# b = round(b,2)     # round use for decimal value less:
# print("Area:", a , "circumference", b)


#--Default parameter value:(Write a function that greet the user . if no name is provide, it should greet with a default name:)

# def greet(name = "suraj"):
#     return "hello, " +name+ " !"
#
#
# print(greet("python"))
# print(greet())



#-- Lamda Function:(Create a Lamda function to compute the cube of a number:

# cube = lambda x: x ** 3
# print(cube(3))



#--Function with *args:(write a function that takes variable numbers of argument and return their sum:

# def total(*args):
#      return sum(args)
#
# print(total(1,2,3))
# print(total(1,2,3,4,5,6,7))
# print(total(1,2,3,4,32,24,3,2,3,))


#--Function with **Kwargs:(Crate a function that accept any number of keyword arguments and print them in the formate key value):






#--Generator function with yield:(Write a Generator function that yield even numbers up to a specified limit):

# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i    # return or print ki jgh yield keyword ka use hua
#
# for num in even_generator(10):
#     print(num)


#--Recursive Function:(Create a recursive function to calculate the factorial of a number:

# def fact(n):
#     if n == 1 or n == 0 :
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(5))




#-write  a program using recursion print number   n to 1:

# def n_to_1(n):
#     if n == 0 :
#         return
#     print(n)
#     #recursive cace
#     print(n_to_1(n-1))
#
# print(n_to_1(5))




# Write a program to print sum to 1 to n : (using recursion):
#
# def sum_1_to_n(n):
#     if n ==1:
#         return 1
#
#     else:
#         result = n + sum_1_to_n(n-1)
#         return result
#
# print(sum_1_to_n(5))


#--write a python function that checks if the given string is a palindrome or not :

'''def check_palindrome(str):

    clean_str =  str.replace(" ","").lower()

    reverse_str = clean_str[::-1]

    return clean_str == reverse_str

str = input("Enter string:")

if check_palindrome(str):
    print("its a palindrome string:")
else:
    print("not a palindrome string")'''




































