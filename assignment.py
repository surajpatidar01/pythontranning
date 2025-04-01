#Q1--Write a program to print the first 10 natural numbers using for loop.

#for i in range(1,11):
#   print(i)

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

'''num = 15
sum_odds = 0

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

#Q8--Write a program to check if the given string is a palindrome - madam(user input)

'''name = input("Enter a name:")
reverse=""
for char in name:
    reverse = char  + reverse
if name == reverse :
    print("Yes , string is palindrome")
else:
    print("No, string is not palindrome")'''



#Q9--Write a program that accepts a word from the user and reverses it.
'''word= input("enter n:")
reversed_word = word[::-1]
print("",reversed_word)'''


#Q10--Write a program to check if a given number is an Armstrong number 153.'





#list assignment;
'''Q1Write a Python program to sum all the items in a list'''

'''num = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in num:
    sum += i
print(sum)'''

'''Q2-Write a Python program to multiply all the items in a list'''

'''num = [1,2,3,4]
multiplication = 1
for i in num:
    multiplication *= i
print("multiplication of all iten of list is",multiplication)'''

'''Q 3 Write a Python program to get the largest number from a list'''

'''num = [20,10,40,66,1,77,100,120,2100,40,20,42]
largest_number  = 0
for i in num:
    if i > largest_number:
        largest_number = i
print("largest number is",largest_number)'''

'''Q4-Write a Python program to get the smallest number from a list'''

'''num = [20,10,40,66,1,77,100,120,2100,40,20,42]
smallest_number = num[0]
for i in num:
    if i < smallest_number:
        smallest_number = i
print("smallest number is ",smallest_number)'''



'''Q5 - Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2'''

sample_list = ['abc', 'xyz', 'aba', '1221']


'''Q6-Write a Python program to remove duplicates from a list.'''
number = [1,2,8,0,3,6,5,1,2]
print(number)




'''Q7-Write a Python program to check if a list is empty or not.'''




'''Q 8-Write a Python program to clone or copy a list.'''

'''list = [1,2,3,4,5,6,7,8,9]
print(list)
copy_list = list[:]
print(copy_list)
'''


'''Q 9-Write a Python program to find the list of words that are longer than n from a given list of words.'''


'''Q10-Write a Python function that takes two lists and returns True if they have at least one common member.'''








