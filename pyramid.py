# while loop
'''Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are
building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according
to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
Your task is to write a program which reads the number of blocks
the builders have, and outputs the height of the pyramid that can
be built using these blocks.
Note: the height is measured by the number of fully completed layers –
if the builders don't have a sufficient number of blocks and cannot
complete the next layer, they finish their work immediately.'''


'''blocks = int(input("enter a number of blocks:"))
height = 0
layer = 0
while blocks>=layer:
    blocks -= layer
    height += 1
    layer +=1
print("The height of pyramid is:",height )'''


# Step 1: Take input from user
'''In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains
unproven) which can be described in the following way:
1. take any non-negative and non-zero integer number and name it c0;
2. if it's even, evaluate a new c0 as c0 ÷ 2;
3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4. if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural
number (it may even require artificial intelligence), but you can use Python to check some individual numbers.
Maybe you'll even find the one which would disprove the hypothesis.
Write a program which reads one natural number and executes the above steps as long as c0 remains different
from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the
intermediate values of c0, too.
Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the
key to success.'''


'''c0 = int(input("Enter a natural number: "))

# Step 2: Validate input (it must be positive)
if c0 <= 0:
    print("Please enter a natural number greater than zero.")
else:
    steps = 0  # Initialize step counter

    # Step 3: Apply Collatz sequence
    while c0 != 1:
        print(c0, end=" ")  # Print the current value
        if c0 % 2 == 0:
            c0 = c0 // 2  # Even case
        else:
            c0 = 3 * c0 + 1  # Odd case
        steps += 1  # Increment step count

    print(1)  # Print final 1
    print("Total steps:", steps)  # Step 4: Output total steps'''

