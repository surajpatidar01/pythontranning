#Q1--Write a program to print the first 10 natural numbers using for loop.

#for i in range(1,11):
#   print(i)'''

#Q2--Write a program to print all the even numbers within the range of 10

'''for i in range(1,10):
    if  i % 2 == 0:
        print(i)'''

#Q3--Write a program to calculate the sum of all numbers from 1 to a given number - 15.

'''n = 15
sum_n = 0

for i in range(1, n + 1):
    sum_n += i
print("Sum of numbers from 1 to 15 is:", sum_n)'''

#Q4--Write a program to calculate the sum of all the odd numbers within the given range of 15.
'''sum_odds = 0

for num in range(1, 16):
    if num % 2 != 0:
        sum_odds += num

print("sum of 1 to 15 odd num is", sum_odds)'''

#Q5--Write a program to print a multiplication table of a given number 15.

'''n = 15
for i in range(1, 11):
    print(n * i)'''


#Q6---Write a program to display numbers from a list using a for the loop [1,2,4,6,88,125]

'''num = [1,2,4,6,88,125]
for i in num:
    print(i)'''

#Q7--Write a program to count the total number of digits in a number 129475

'''num = 129475
count = len(str(num))
print(count)'''

#Q8--Write a program to check if the given string is a palindrome - madam

'''n = "madam"

if n == n[::-1]:
    print("its palindrome")
else:
    print("its not palindrome")'''

#Q9--Write a program that accepts a word from the user and reverses it.
'''word= input("enter n:")
reversed_word = word[::-1]
print("",reversed_word)'''


#Q10--Write a program to check if a given number is an Armstrong number 153.'



