
# BITWISE OPERATOR :

#1---bitwise (AND)
a = 0b1010
b = 0b1100

c = a & b
print(bin(c))

#2---bitwise (OR)
a = 0b1010
b = 0b1100

c = a | b
print(bin(c))

#3---bitwise (XOR)
a = 0b1010
b = 0b1100

c = a ^ b
print(bin(c))

#4---(NOT)
a = 0b1010

c = ~a
print(bin(c))

#5---bitwise  (LEFT SHIFT)
a = 0b1010

c = a << 2
print(bin(c))

#6---bitwise (RIGHT SHIFT)
a = 0b1010

c = a >> 1
print(bin(c))