'''Q1--Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
def is_year_leap(year):
    #
    # Write your code here.
    #
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")'''

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
        print("Failed")
'''




'''Q2--Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).
The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.
def is_year_leap(year):
    #
    # Your code from the Practice Question .
    #
def days_in_month(year, month):
    #
    # Write your new code here.
    #
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
'''


