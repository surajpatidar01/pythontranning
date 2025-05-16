'''from math import *
print(sin(pi/2))
print(exp(2))

#aliasing
import math as ganit
print(ganit.sin(ganit.pi/2))
print(ganit.exp(2))

from math import sin as si, exp as e,pi as p
print(si(p/2))
print(e(2))

#dir()
import math
print(math.sin(math.pi/2))
print(dir(math))
print("asinh" in dir(math))'''


'''from math import pi,radians,degrees,sin,cos,tan,asin
ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi/2.)
print(sin(ar)/cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)'''

'''from random import random
for i in range(5):
    print(random())'''

'''from random import random, seed ,randrange
seed(0)
for i in range(5):
    print(randrange(4)+1)'''

'''from random import random, seed ,randrange,randint
seed()
for i in range(5):
    #print(randrange(1,101,5))
    print(randint(1,10),end=",")
'''

'''from random import random, seed ,randrange,randint,choice, sample
my_list= [1,2,3,4,5,6,7,8,9,10]
for i in range(5):
    print(choice(my_list))
    print(sample(my_list,4))
    print(sample(my_list,7))'''

from platform import platform ,machine,processor,system,version,python_implementation
#print(platform())
#print(platform(1))
#print(platform(0,1))

#--os
print(machine())
print(processor())
print(system())
print(version())

#--python
print(python_implementation())


