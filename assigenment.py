'''Write a program to calculate the sum of all the elements in the list:
list=> my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''




'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

total_sum  = sum(my_list)
print("sum of element in the list",total_sum)'''


'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list.insert(1,5)
print(my_list)'''


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

beatles.insert(0,"Ringo Starr")
print(beatles)'''


'''Imagine you are creating a list to track the members of a fictional rock band. The band started with three members and later had some changes in the lineup.

Your task is to write a program that performs the following steps:

Step 1: Create an empty list named band_members.
Step 2: Use the append() method to add the following members to the band: "Alice Cooper", "Jim Morrison", and "Jimi Hendrix".
Step 3: Use a for loop and the append() method to prompt the user to add two more members of the band: "Janis Joplin" and "Mick Jagger".
Step 4: Use the del instruction to remove "Jim Morrison" and "Jimi Hendrix" from the list.
Step 5: Use the insert() method to add "Keith Richards" to the beginning of the list.
Step 6: Display the final list of band members'''

'''band_members = []
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

'''lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))'''















