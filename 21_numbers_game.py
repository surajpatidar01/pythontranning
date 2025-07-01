
import random

while True:
    print("WELCOME TO PYTHON 21 NUMBER GAME:")
    print(    "    -------------      ")
    print("Each time you can say 1,2 or 3 number, whoever say 21 lose:")



    while True:
            choice = input("Enter 1 for user first or 2 for comp first-:")

            if choice =="1":
                print("User goes first")
                user_turn = True
                break
            elif  choice == "2":
                print("computer goes first ")
                user_turn = False
                break
            else:
                print("invalid input!,please enter 1 or 2")
 

    current_number = 0

    while current_number < 21:
        user_input = int(input("Enter a  1-3 min number ",))
        if user_input<  1 or user_input > 3:
            print("Wrong input please enter a 1-3 mid number")

            continue

        for i in range(1, user_input + 1):
            current_number += 1
            print("You said " , current_number )
        if current_number == 21:
            print("You said 21","you lose")

        comp_input = random.randint(1, 3)
        while current_number + comp_input > 21:
            comp_input = random.randint(1, 3)

        for i in range(comp_input):
            current_number += 1
            print("Computer said:", current_number)
            if current_number == 21:
                print("Computer said 21. You win!")

    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
       print("Thanks for playing ")
       break



