# Write a program that handles division by zero using try and except.

# a = int(input("Enter a number a:"))
# b = int(input("Enter a number b:"))
#
# try:
#     c = a/b
#     print("result--",c)
# except ZeroDivisionError:
#
#     print("Can't divide by Zero")



#-Catch an exception when trying to convert a string like "abc" to an integer.

# try:
#     x = int("abc")
#
# except:
#     print("Can't convert to int")


#-Handle an exception when trying to open a file that doesn’t exist.

# try:
#     file = open("file.txt","r")
# except FileNotFoundError:
#     print("File not found!")

#-Use finally to print “Done” whether or not an exception occurs.try:
# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("Done")

#-Use multiple except blocks to catch ValueError and ZeroDivisionError separately.try:
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print("Result:", result)
#
# except ValueError:
#     print("Invalid input! Please enter numbers only.")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


#-Use a generic except block to catch any exception and print the error message.try:

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except Exception as e:
#     print("An error occurred:", e)

#-Catch a TypeError when trying to add an int and a string.try:

# try:
#     result = 5 + "hello"
# except TypeError:
#     print("Error: Cannot add an integer and a string!")

#-Write a function that asks for user input and keeps prompting until a valid integer is entered.def get_valid_integer():

# def get_valid_integer():
#     while True:
#         try:
#             num = int(input("Enter a valid integer: "))
#             return num
#         except ValueError:
#             print("Invalid input! Please enter a valid integer.")
#
# # Example usage
# number = get_valid_integer()
# print("You entered:", number)



#Handle an exception when accessing a non-existent key in a dictionary.
# my_dict = {"name": "Alice", "age": 25}
#
# try:
#     print(my_dict["city"])
# except KeyError:
#     print("Error: Key 'city' not found in the dictionary.")

#-Catch an IndexError when accessing an out-of-bounds index in a list.my_list = [10, 20, 30]

# my_list = [10, 20, 30]
#
# try:
#     print(my_list[5])  # This index does not exist
# except IndexError:
#     print("Error: Index out of range!")


#-Use try...except...else to run code only if no exception occurs.

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter valid numbers.")
# else:
#     print("Division successful. Result:", result)

#-Wrap a function call with try-except and log errors to a file.

# def divide(a, b):
#     return a / b
#
# try:
#     result = divide(10, 0)  # This will raise ZeroDivisionError
#     print("Result:", result)
# except Exception as e:
#     with open("error_log.txt", "a") as log_file:
#         log_file.write(f"Error occurred: {e}\n")
#     print("An error occurred. Check error_log.txt for details.")


#-Raise a ValueError manually if a function receives a negative number.def square_root(x):
# def square_root(x):
#
#     if x < 0:
#         raise ValueError("Negative number not allowed!")
#     return x ** 0.5
#
# # Example usage
# try:
#     result = square_root(-9)
#     print("Result:", result)
# except ValueError as e:
#     print("Error:", e)

#-Catch exceptions when parsing JSON using json.loads().

# import json
#
# data = '{"name": "Alice", "age": 25}'  # Valid JSON
# # data = '{"name": "Alice", "age": 25'   # Uncomment for invalid JSON
#
# try:
#     parsed = json.loads(data)
#     print("Parsed JSON:", parsed)
# except json.JSONDecodeError as e:
#     print("Failed to parse JSON:", e)