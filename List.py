# List   (mutable)
fruits = ["Apple","banana","cherry","Kiwi"]
#fruits[0] = 1
#print(fruits)              # print a list

#print(type(fruits))       #cheak type of list

#print(len(fruits))         #  how to cheak lenth of  list

#----checking if item is present  in a list.
'''if "banana" in  fruits:
    print("banana  is part of list:")
'''

#----checking if item is not present  in a list.
'''if "grapes" not in fruits:
    print("grapes is not part of list:")
'''

#------indexing in list

#print(fruits[1])      #(indexing strat front)
#print(fruits[-3])      #(indexing strat back)

#----printing sublist

#print(fruits[1:3])      #(indexing strat front)
#print(fruits[-3:-1])     #(indexing strat back)



#List
#numbers = [70,20,40,10,90,30,100,50]





#------adding elements to a list.(append)

#numbers.append(60)
#print(numbers)

#------insert element to a list(insert).
#numbers.insert(1,100000)
#print(numbers)

#------Extend  the list(extend).
#fruits.extend(numbers)
#print(fruits)

#-----Remove element from list.(remove.)
#numbers.remove(20)
#print(numbers)

#-----Remove element from  (pop--- function)

#numbers.pop(1)         #remove first index item
#numbers.pop()          # remove last item


#------changing(updating) item in a list.
#numbers[2] = 100000
#print(numbers)
#------changing (range) list.
#numbers[1:3] = [100,200]
#print(numbers)

#-------(Sort)  sorting a list.

#-(ascending)
#numbers.sort()     # by default ascending.
#print(numbers)

#-descending.
#numbers.sort(reverse = True)       # descending way.
#print(numbers)

#-reverse list.
#numbers.reverse()
#print(numbers)


# List comprehension.

#fruits = ["apple","banana","cherry","mango","kiwi"]

#new_fruits = [fruits for fruits in fruits if "a" in fruits]
#print(new_fruits)

#----copy a list
'''fruits = ["apple","banana","cherry","mango","kiwi"]
new_fruits = fruits.copy()
print(new_fruits)'''

#----concetinate 2 list.
'''fruits = ["apple","banana","cherry","mango","kiwi"]
new_fruits = ["grapes","papaya","watermelon"]

n = fruits + new_fruits
print(n)'''

#----nested list.
#numbers  = [10,20,[30,40],50]
#print(numbers[2])
#print(numbers[2][0])

# list traverse.
'''numbers = [10,40,60,90,20,30,50,70]
for i in numbers:
    print(i)'''




