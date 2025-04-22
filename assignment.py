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

'''numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in  numbers:
    sum += i
print("Sum of all list element is",sum)
'''


'''Q2-Write a Python program to multiply all the items in a list'''
'''numbers = [1,2,3,4,5,6,7,8,9,10]
multiply = 1
for i in numbers :
    multiply *= i
print("Multiplication result of list is",multiply)'''


'''Q 3 Write a Python program to get the largest number from a list'''

'''numbers = [1,2,3,4,5,6,7,8,9,10]
largest_number  = 0
for i in numbers:
    if i > largest_number:
        largest_number = i
print("largest number is ", largest_number)
'''


'''Q4-Write a Python program to get the smallest number from a list'''

'''numbers = [1,2,3,4,5,6,7,8,9,10]
smallest_number = numbers[0]
for i in numbers:
    if i < smallest_number:
        smallest_number = i
    print("Smallest number of list is", smallest_number)
'''



'''Q5--Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.'''

'''sample_list = ["aba","abc",1221, "add"]
count = 0
for i in sample_list:
    if str(i)[0] == str(i)[-1]:
        count += 1
print(count)'''


'''Q6-Write a Python program to remove duplicate from a list.'''

'''number = [1,2,7,2,4,1,4,8,6,4,4,5,9,10]
duplicate_number = []
for i in number:
    if i not in duplicate_number:
        duplicate_number.append(i)
print(duplicate_number)'''



'''Q7-Write a Python program to check if a list is empty or not.'''

'''my_list = []
if not my_list:
    print("empty my list")
else:
    print("not empty ,my list")'''

'''Q 8-Write a Python program to clone or copy a list.'''
'''number = [1,2,3,4,5,6,7,8,9 ]
print(number)
clone = number.copy()
print(clone)'''



'''Q 9-Write a Python program to find the list of words that are longer than n from a given list of words.'''

'''fruits = ["apple","banana","cherry","grapes"]
new_fruits = []
n = 5
for i in fruits:
    if (len(i) > n):
        new_fruits.append(i)
print(new_fruits)'''





'''Q10-Write a Python function that takes two lists and returns True if they have at least one common member.'''






#Q1--Remove Even Numbers from List | List: [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]

'''List = [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
odd_numbers = []
for  element in List:
    if element % 2 != 0:
       odd_numbers.append(element)
print(odd_numbers)'''

#Q2-Write a Python program to generate and print a list of the first 5 and last
# 5 elements where the values are square numbers between 1 and 30 (both included).

'''square_numbers = []
for i in range(1,31):
    square  =  i ** 2
    if square < 30:
        square_numbers.append(square)
first5 = square_numbers[:5]
last5 = square_numbers[-5:]
print("First 5 square numbers:", first5)
print("Last 5 square numbers:", last5)
'''

#Q3--Check If All Numbers Are Prime | Lists: [0, 3, 4, 7, 9], [3, 5, 7, 13], [1, 5, 3]
'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

List = [0, 3, 4, 7, 9]

all_prime = all(is_prime(i) for i in List)

print("All numbers are prime?" , all_prime)'''


#Q4--Write a Python program to convert a list of characters into a string

'''character_list = ["H","e","L","L","O"]
result_list = " "

for character in character_list:
    result_list += character
print(result_list)'''

#Q5--Write a Python program to find the index of an item in a specified list.
# | List: [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7], find index of element 0

'''List =  [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
element = 0
for i in range(len(List)):
    if List[i] == element:

        print("index of 0 element is",i)'''


#Q6_-Write a Python program to append a list to the second list. | List: [0, 3, 4, 7, 9], [3, 5, 7, 13]

'''List1 = [0, 3, 4, 7, 9]
List2 = [0, 3, 4, 7, 9]3

list2 += List1
print("Update result",list2)'''



'''List1 = [0, 3, 4, 7, 9]
List2 = [0, 3, 4, 7, 9]

for i in List1:
    List2.append(i)
print(List2)'''


#Q7--Write a Python program to find the second smallest number in a list. | List: [0, 3, 4, 7, 9]
'''List = [0, 3, 4, 7, 9]
List.sort()
print(List)
second_smallest = List[1]
print(second_smallest)'''

#Q8--Write a Python program to find the second largest number in a list. | [0, 3, 4, 7, 9
'''numbers = [0, 3, 4, 7, 9]
numbers.sort()
print(numbers)
second_largest = numbers[-2]
print(second_largest)'''

#Q9--Write a Python program to get the frequency of elements in a list. | List: [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]

'''List = [6, 2, 7, 1, 3, 2, 7, 9, 0, 4, 5, 1, 6, 7]
for i in List:
    if i'''





#Q10--Write a Python program to check whether a list contains a sublist. | Lists: [0, 3, 4, [3, 5, 7, 13], 7, 9], [3, 5, 7, 13]
'''
List1 =  [0, 3, 4, [3, 5, 7, 13], 7, 9]
List2 =  [3, 5, 7, 13]
if List2 in List1:
    print("List 1 contains List 2 as a sublist.")
else:
    print("List 1 contains List 2 as a sublist.")'''













