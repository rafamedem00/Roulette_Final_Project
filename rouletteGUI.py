from tkinter import *
import random

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
c2to1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
b2to1 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
a2to1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
num_history = []
num_history2 = ["History: "]

money = [500]

root = Tk()

canvas = Canvas(root, height=600, width=1005, bg='#003300')
canvas.pack()

frame = Frame(canvas, bg='#003300')
frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

b0 = Button(frame, text="0", fg='green', padx=20, pady=20, command=lambda: bet(0))
b1 = Button(frame, text="01", fg='red', padx=20, pady=20, command=lambda: bet(1))
b2 = Button(frame, text="02", fg='black', padx=20, pady=20, command=lambda: bet(2))
b3 = Button(frame, text="03", fg='red', padx=20, pady=20, command=lambda: bet(3))
b4 = Button(frame, text="04", fg='black', padx=20, pady=20, command=lambda: bet(4))
b5 = Button(frame, text="05", fg='red', padx=20, pady=20, command=lambda: bet(5))
b6 = Button(frame, text="06", fg='black', padx=20, pady=20, command=lambda: bet(6))
b7 = Button(frame, text="07", fg='red', padx=20, pady=20, command=lambda: bet(7))
b8 = Button(frame, text="08", fg='black', padx=20, pady=20, command=lambda: bet(8))
b9 = Button(frame, text="09", fg='red', padx=20, pady=20, command=lambda: bet(9))
b10 = Button(frame, text="10", fg='black', padx=20, pady=20, command=lambda: bet(10))
b11 = Button(frame, text="11", fg='black', padx=20, pady=20, command=lambda: bet(11))
b12 = Button(frame, text="12", fg='red', padx=20, pady=20, command=lambda: bet(12))
b13 = Button(frame, text="13", fg='black', padx=20, pady=20, command=lambda: bet(13))
b14 = Button(frame, text="14", fg='red', padx=20, pady=20, command=lambda: bet(14))
b15 = Button(frame, text="15", fg='black', padx=20, pady=20, command=lambda: bet(15))
b16 = Button(frame, text="16", fg='red', padx=20, pady=20, command=lambda: bet(16))
b17 = Button(frame, text="17", fg='black', padx=20, pady=20, command=lambda: bet(17))
b18 = Button(frame, text="18", fg='red', padx=20, pady=20, command=lambda: bet(18))
b19 = Button(frame, text="19", fg='red', padx=20, pady=20, command=lambda: bet(19))
b20 = Button(frame, text="20", fg='black', padx=20, pady=20, command=lambda: bet(20))
b21 = Button(frame, text="21", fg='red', padx=20, pady=20, command=lambda: bet(21))
b22 = Button(frame, text="22", fg='black', padx=20, pady=20, command=lambda: bet(22))
b23 = Button(frame, text="23", fg='red', padx=20, pady=20, command=lambda: bet(23))
b24 = Button(frame, text="24", fg='black', padx=20, pady=20, command=lambda: bet(24))
b25 = Button(frame, text="25", fg='red', padx=20, pady=20, command=lambda: bet(25))
b26 = Button(frame, text="26", fg='black', padx=20, pady=20, command=lambda: bet(26))
b27 = Button(frame, text="27", fg='red', padx=20, pady=20, command=lambda: bet(27))
b28 = Button(frame, text="28", fg='black', padx=20, pady=20, command=lambda: bet(28))
b29 = Button(frame, text="29", fg='black', padx=20, pady=20, command=lambda: bet(29))
b30 = Button(frame, text="30", fg='red', padx=20, pady=20, command=lambda: bet(30))
b31 = Button(frame, text="31", fg='black', padx=20, pady=20, command=lambda: bet(31))
b32 = Button(frame, text="32", fg='red', padx=20, pady=20, command=lambda: bet(32))
b33 = Button(frame, text="33", fg='black', padx=20, pady=20, command=lambda: bet(33))
b34 = Button(frame, text="34", fg='red', padx=20, pady=20, command=lambda: bet(34))
b35 = Button(frame, text="35", fg='black', padx=20, pady=20, command=lambda: bet(35))
b36 = Button(frame, text="36", fg='red', padx=20, pady=20, command=lambda: bet(36))
b_a2to1 = Button(frame, text="2 to 1", fg='green', padx=20, pady=20, command=lambda: bet("a2to1"))
b_b2to1 = Button(frame, text="2 to 1", fg='green', padx=20, pady=20, command=lambda: bet("b2to1"))
b_c2to1 = Button(frame, text="2 to 1", fg='green', padx=20, pady=20, command=lambda: bet("c2to1"))
b_1st12 = Button(frame, text="1st 12", fg='green', command=lambda: bet("1st12"))
b_2nd12 = Button(frame, text="2nd 12", fg='green', command=lambda: bet("2nd12"))
b_3rd12 = Button(frame, text="3rd 12", fg='green', command=lambda: bet("3rd12"))
b_1to18 = Button(frame, text="1-18", fg='green', command=lambda: bet("1-18"))
b_even = Button(frame, text="EVEN", fg='green', command=lambda: bet("even"))
b_red = Button(frame, text="RED", fg='red', command=lambda: bet("red"))
b_black = Button(frame, text="BLACK", fg='black', command=lambda: bet("black"))
b_odd = Button(frame, text="ODD", fg='green', command=lambda: bet("odd"))
b_19to36 = Button(frame, text="19-36", fg='green', command=lambda: bet("19-36"))

b0.grid(row=2, column=0)
b1.grid(row=3, column=1)
b2.grid(row=2, column=1)
b3.grid(row=1, column=1)
b4.grid(row=3, column=2)
b5.grid(row=2, column=2)
b6.grid(row=1, column=2)
b7.grid(row=3, column=3)
b8.grid(row=2, column=3)
b9.grid(row=1, column=3)
b10.grid(row=3, column=4)
b11.grid(row=2, column=4)
b12.grid(row=1, column=4)
b13.grid(row=3, column=5)
b14.grid(row=2, column=5)
b15.grid(row=1, column=5)
b16.grid(row=3, column=6)
b17.grid(row=2, column=6)
b18.grid(row=1, column=6)
b19.grid(row=3, column=7)
b20.grid(row=2, column=7)
b21.grid(row=1, column=7)
b22.grid(row=3, column=8)
b23.grid(row=2, column=8)
b24.grid(row=1, column=8)
b25.grid(row=3, column=9)
b26.grid(row=2, column=9)
b27.grid(row=1, column=9)
b28.grid(row=3, column=10)
b29.grid(row=2, column=10)
b30.grid(row=1, column=10)
b31.grid(row=3, column=11)
b32.grid(row=2, column=11)
b33.grid(row=1, column=11)
b34.grid(row=3, column=12)
b35.grid(row=2, column=12)
b36.grid(row=1, column=12)
b_a2to1.grid(row=3, column=13)
b_b2to1.grid(row=2, column=13)
b_c2to1.grid(row=1, column=13)
b_1st12.place(relheight=0.1, relwidth=0.281, relx=0.061, rely=0.33)
b_2nd12.place(relheight=0.1, relwidth=0.2815, relx=0.342, rely=0.33)
b_3rd12.place(relheight=0.1, relwidth=0.281, relx=0.624, rely=0.33)
b_1to18.place(relheight=0.1, relwidth=0.1405, relx=0.061, rely=0.43)
b_even.place(relheight=0.1, relwidth=0.1407, relx=0.201, rely=0.43)
b_red.place(relheight=0.1, relwidth=0.1405, relx=0.342, rely=0.43)
b_black.place(relheight=0.1, relwidth=0.1405, relx=0.483, rely=0.43)
b_odd.place(relheight=0.1, relwidth=0.1405, relx=0.624, rely=0.43)
b_19to36.place(relheight=0.1, relwidth=0.1405, relx=0.765, rely=0.43)

budget = Label(frame, text="Money in Bank: " + str(money[0]) + "€", bg='#003300', fg='white', font=("Courier", 20))
budget.place(relheight=0.1, relwidth=0.2815, relx=0.061, rely=0.83)

bet_amount = Entry(frame, font=("Courier", 15))
bet_amount.place(relheight=0.08, relwidth=0.1405, relx=0.201, rely=0.63)

betlbl = Label(frame, text="Bet(€): ", bg='#003300', fg='white', font=("Courier", 20))
betlbl.place(relheight=0.1, relwidth=0.1405, relx=0.061, rely=0.63)

win_label = Label(frame, text="", bg='white', font=('fixedsys', 30))
win_label.place(relheight=0.1, relwidth=0.1, relx=0.483, rely=0.63)

landonlbl = Label(frame, text="The Ball Landed On: ", bg='#003300', fg='white', font=("Courier", 20))
landonlbl.place(relheight=0.1, relwidth=0.4, relx=0.343, rely=0.53)

win_message = Label(frame, text="", bg='#003300', fg='white', font=("Courier", 20))
win_message.place(relheight=0.1, relwidth=0.4, relx=0.6, rely=0.63)

history = Label(frame, text=num_history2 + num_history, bg='#003300', fg='white', font=("Courier", 20))
history.place(relheight=0.1, relwidth=0.7, relx=0.343, rely=0.83)


def bet(input):
    win_message.config(text="")
    win_message.place(relheight=0.1, relwidth=0.4, relx=0.6, rely=0.63)
    current_bet = int(bet_amount.get())
    if money[0] >= current_bet:
        money[0] -= current_bet
        budget.config(text="Money in Bank: " + str(money[0]) + "€")
        history.config(text=num_history2 + num_history)
        create_win_num()
        if input == 'even':
            if num_history[0] in even:
                money[0] += current_bet * 2
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'odd':
            if num_history[0] in odd:
                money[0] += current_bet * 2
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'red':
            if num_history[0] in red:
                money[0] += current_bet * 2
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'black':
            if num_history[0] in black:
                money[0] += current_bet * 2
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'green':
            if num_history[0] in green:
                money[0] += current_bet * 36
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == '1-18':
            if num_history[0] in range(1, 19):
                money[0] += current_bet * 2
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == '19-36':
            if num_history[0] in range(19, 37):
                money[0] += current_bet * 2
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == '1st12':
            if num_history[0] in range(1, 13):
                money[0] += current_bet * 3
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == '2nd12':
            if num_history[0] in range(13, 25):
                money[0] += current_bet * 3
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == '3rd12':
            if num_history[0] in range(25, 37):
                money[0] += current_bet * 3
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'a2to1':
            if num_history[0] in a2to1:
                money[0] += current_bet * 3
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'b2to1':
            if num_history[0] in b2to1:
                money[0] += current_bet * 3
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == 'c2to1':
            if num_history[0] in c2to1:
                money[0] += current_bet * 3
                budget.config(text="Money in Bank: " + str(money[0]) + "€")
                win_message.config(text="WINNER WINNER CHICKEN DINNER!")

        elif input == num_history[0]:
            money[0] += current_bet * 36
            budget.config(text="Money in Bank: " + str(money[0]) + "€")
            win_message.config(text="WINNER WINNER CHICKEN DINNER!")
    else:
        win_message.config(text="You don't have enough money!")


def create_win_num():
    win_num = random.randint(0, 36)
    num_history.insert(0, win_num)
    if len(num_history) > 10:
        num_history.pop(10)
    if win_num in red:
        win_label.config(text=str(win_num), fg='red')
    elif win_num in black:
        win_label.config(text=str(win_num), fg='black')
    else:
        win_label.config(text=str(win_num), fg='green')


root.mainloop()
