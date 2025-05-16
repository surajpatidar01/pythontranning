
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
    print(num_patterns[digit])
    print()

