

'''Q1--Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.'''

'''m = int(input("Enter a number of rows(m):"))
n = int(input("Enter a number of columns(n):"))
list = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
    for j in range(n):
        list[i][j] = i * j  

print(list)'''




'''Q2--j = 0,1, n-1.
Write a Python program to find nested list elements that are present in another list.
Original lists:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
Intersection of said nested lists: OUTPUT
[[12], [7, 11], [1, 5, 8]]'''

'''list1=[1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12,13, 14]
list2=[[12, 18, 23, 25, 45],[7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
list3=[]
for i in list2:
    for j in list1:
        if j in i:
            list3.append(j)
print(list3)'''




'''Q3--Write a Python program to find common elements in a nested list.
Original lists:
[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
Common element(s) in nested lists:
[18, 12]'''

'''List1 = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
List2 = []
for i in List1:
    for j in List1[0]:
        if j in i:
            List2.append(j)
    print(List2)'''





'''Q4--Write a program that creates a nested list from two user inputted lists of integers. The resulting nested list should contain each element of the first list paired with the corresponding element of the second list.
Example input: [1, 2, 3], [4, 5, 6]
Example output: [[1, 4], [2, 5], [3, 6]]'''




'''Q5--Write a program that creates a nested list of strings from a user inputted list of strings. The resulting nested list should contain each string split into its individual characters.
Example input: ['hello', 'world']
Example output: [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]'''

'''list1 = input("Enter the list of strings: ")
list2=[]
for i in list1:
    list2.append(list(i))
print(list2)'''



'''Q6--Write a program that creates a nested list of integers from a user inputted list of integers. The resulting nested list should contain each integer along with its square.
Example input: [1, 2, 3, 4, 5]
Example output: [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]'''

'''list1 = int(input("Enter the list of integers: "))
list2=[]
for i in list1:
    list2.append([int(i), int(i) ** 2])

print(list2)'''


'''Q7--Write a program that creates a nested list from a user inputted list of strings. The resulting nested list should contain the unique characters from each string.
Example input: ['apple', 'banana', 'cherry']
Example output: [['a', 'p', 'l', 'e'], ['b', 'a', 'n'], ['c', 'h', 'e', 'r', 'y']]'''

'''list1 = input("Enter the list of strings: ")
list2=[]
for i in list1:
     list2.append(list(set(i)))
print(list2)'''



'''Q8--Write a program that creates a nested list of integers from a user inputted list of integers. The resulting nested list should contain each integer along with all of its divisors.
Example input: [2, 3, 4, 5]
Example output: [[2, [1, 2]], [3, [1, 3]], [4, [1, 2, 4]], [5, [1, 5]]]'''

'''list1 = input("Enter the list of strings: ")
list2=[]
for i in list1:
    list2.append(list(i))
print(list2)'''


'''Q9--Write a Python program to find the sum of all elements in a 2D list.  [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]'''
'''list1=[[1, 1], [2, 4], [3, 9],[4, 16], [5, 25]]
sum=0
for i in list1:
    for j in i:
        sum += j
print(sum)'''

