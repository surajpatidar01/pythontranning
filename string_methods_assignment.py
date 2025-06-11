#-Use .upper() to convert a string to uppercase.
text = "hello world"
print(text.upper())

#-Use .lower() to convert a string to lowercase.text = "HELLO WORLD"
text = "HELLO WORLD"
print(text.lower())

#-Use .capitalize() to make the first letter of a string uppercase.
text = "hello world"
print(text.capitalize())


#-Use .title() to capitalize the first letter of every word.
text = "hello world from python"
print(text.title())

#-Use .strip() to remove whitespace from both ends of a string.
text = "   hello world   "
print(text.strip())

#-Use .replace() to replace all instances of "Python" with "JavaScript".
text = "I love Python. Python is powerful!"
new_text = text.replace("Python", "JavaScript")
print(new_text)

#-Use .count() to count how many times "a" appears in a string.Use .count() to count how many times "a" appears in a string.text = "banana has a lot of a's"
text = "banana has a lot of a's"
count_a = text.count("a")
print("Number of 'a':", count_a)

#-Use .find() and .index() to find the position of "@" in an email string.
email = "ptdrsuraj@gmail.com"
position = email.find("@")
print("Position using find():", position)

#-Use .startswith() and .endswith() to check if a string starts or ends with certain words.

#startwith()
text = "Hello, welcome to Python programming."
print(text.startswith("Hello"))
print(text.startswith("welcome"))

#endwith()
text = "Hello, welcome to Python programming."
print(text.endswith("programming."))
print(text.endswith("Python"))


#-Use .split() to split a sentence into a list of words.sentence = "Python is a powerful language"
sentence = "Python is a powerful language"
words = sentence.split()
print(words)

#-Use .join() to join a list of words with hyphens.words = ['Python', 'is', 'awesome']
words = ['Python', 'is', 'awesome']

sentence = '-'.join(words)
print(sentence)

#-Use .isalpha() to check if the string contains only letters.
text1 = "HelloWorld"
text2 = "Hello123"

print(text1.isalpha())
print(text2.isalpha())



#-Use .isdigit() to check if the string contains only digits.
text1 = "123456"
text2 = "123abc"

print(text1.isdigit())
print(text2.isdigit())


#-Use .isalnum() to check if the string contains only letters and numbers.

text1 = "Python123"
text2 = "Python 123"
text3 = "123"

print(text1.isalnum())
print(text2.isalnum())
print(text3.isalnum())

#-Use .zfill() to pad a number string with leading zeros to make it 5 digits.

num = "42"
padded = num.zfill(5)
print(padded)

#-Use .partition() to split a string at the first occurrence of ":".
text = "name:Suraj:"
result = text.partition(":")
print(result)


#-Use .rfind() to find the last occurrence of a character in a string.
text = "banana"
position = text.rfind("a")
print("Last 'a' found at index:", position)



#-Use .swapcase() to flip the case of every character.

text = "Hello World"
flipped = text.swapcase()
print(flipped)


#-Use .center(width, char) to center-align a string padded with *.
text = "Python"
centered = text.center(20, "*")
print(centered)


#-Use .ljust() and .rjust() to left- and right-align strings.
text = "Python"

left = text.ljust(15, "*")
right = text.rjust(15, "*")

print("Left Aligned :", left)
print("Right Aligned:", right)



















