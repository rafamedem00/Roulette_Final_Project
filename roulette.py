import random

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

bet_amount = 0
num_history = []
color_history = []
options = ['red', 'black', 'green', 'even', 'odd', '1-18', '19-36', '1st12', '2nd12', '3rd12', 'straight', 'split',
           'corner']

print("Welcome to Rafa's Roulette!")

budget = float(input("How much money do you want to start with? "))
if budget > 500:
    print("Sorry the maximum limit is 500€")
    budget = float(input("Enter a valid amount >> "))
elif budget < 1:
    print("Sorry the minimum limit is 1€")
    budget = float(input("Enter a valid amount >> "))

input("Press enter to view the bet options list")
print(options)

flag = True
while flag:
    winner_num = random.randint(0, 36)
    color = ""
    bet_pick = input("Place your bet: ")
    while bet_pick not in options:
        print("Invalid option. Please choose a valid type of bet >> ")
        bet_pick = input("Place your bet: ")

    bet_amount = float(input("How much do you want to bet? "))
    while bet_amount > budget:
        print("Sorry, you cannot place that bet because it is bigger than your budget.")
        bet_amount = float(input("Please enter a valid amount to bet >> "))

    if bet_pick == 'even':
        if winner_num in even:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 2
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'odd':
        if winner_num in odd:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 2
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'red':
        if winner_num in red:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 2
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'black':
        if winner_num in black:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 2
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'green':
        if winner_num in green:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 36
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == '1-18':
        if winner_num in range(1, 19):
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 2
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == '19-36':
        if winner_num in range(19, 37):
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 2
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == '1st12':
        if winner_num in range(1, 13):
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 3
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == '2nd12':
        if winner_num in range(13, 25):
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 3
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == '3rd12':
        if winner_num in range(25, 37):
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 3
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'straight':
        n1 = int(input("choose a number >> "))
        if n1 == winner_num:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 36
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'split':
        n1 = int(input("choose number1 >> "))
        n2 = int(input("choose number2 >> "))
        if n1 == winner_num or n2 == winner_num:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 18
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    elif bet_pick == 'corner':
        n1 = int(input("choose number1 >> "))
        n2 = int(input("choose number2 >> "))
        n3 = int(input("choose number3 >> "))
        n4 = int(input("choose number4 >> "))
        if n1 == winner_num or n2 == winner_num or winner_num == n3 or winner_num == n4:
            print("WINNER WINNER CHICKEN DINNER!")
            prize = bet_amount * 9
            print("You won", str(prize) + "€")
            budget += prize - bet_amount
            print("You have", str(budget) + "€")
        else:
            print("You lost", str(bet_amount) + "€. Better luck next time!")
            budget -= bet_amount
            print("You have", str(budget) + "€")

    num_history.append(winner_num)

    if winner_num in red:
        color = "red"
        color_history.append(color)
    elif winner_num in black:
        color = "black"
        color_history.append(color)
    else:
        color = "green"
        color_history.append(color)

    print("The ball landed on number", winner_num, color)
    print("The number history is: ", num_history, color_history)

    if budget == 0:
        print("You ran out of money! Better luck next time!")
        break

    flag2 = True
    while flag2:
        try_again = input("Do you want to play again? (Y/N)")
        if try_again == "N" or try_again == "n":
            flag = False
            flag2 = False
            print("Thank you for playing! See you next time!")
        elif try_again == "Y" or try_again == "y":
            flag2 = False
        else:
            print("Please give me a valid response.")
            flag2 = True
            continue
