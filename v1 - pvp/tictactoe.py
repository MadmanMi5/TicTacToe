from tkinter import *
import random


# resets all the buttons and randomises the player, for a new game to be played
def new_game():
    global currentPlayer

    currentPlayer = random.choice(players)

    label.config(text=currentPlayer + " turn")

    for buttonRow in range(3):
        for buttonColumn in range(3):
            buttons[buttonRow][buttonColumn].config(text="", bg="#F0F0F0")


# check to see if there is a winner or a tie
def check_winner():
    for buttonRow in range(3):
        if buttons[buttonRow][0]['text'] == buttons[buttonRow][1]['text'] == buttons[buttonRow][2]['text'] != "":
            buttons[buttonRow][0].config(bg="green")
            buttons[buttonRow][1].config(bg="green")
            buttons[buttonRow][2].config(bg="green")
            return True

    for buttonColumn in range(3):
        if buttons[0][buttonColumn]['text'] == buttons[1][buttonColumn]['text'] == \
                buttons[2][buttonColumn]['text'] != "":
            buttons[0][buttonColumn].config(bg="green")
            buttons[1][buttonColumn].config(bg="green")
            buttons[2][buttonColumn].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_space() is False:

        for buttonRow in range(3):
            for buttonColumn in range(3):
                buttons[buttonRow][buttonColumn].config(bg="yellow")

        return "Tie"
    else:
        return False


# switching between the players so each player can play their turn
# stating the status of the game on board (label), showing who's playing, winner or tie
def player_turn(buttonRow, buttonColumn):
    global currentPlayer

    if buttons[buttonRow][buttonColumn]['text'] == "" and check_winner() is False:

        buttons[buttonRow][buttonColumn]['text'] = currentPlayer

        i = 0
        while currentPlayer != players[i]:
            i = 1
        else:
            if check_winner() is False:
                currentPlayer = players[i == 0]
                label.config(text=(currentPlayer + " turn"))

            elif check_winner() is True:
                label.config(text=(players[i] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")


# the maximum number of moves that can be made in the game
def empty_space():
    spaces = 9

    for buttonRow in range(3):
        for buttonColumn in range(3):
            if buttons[buttonRow][buttonColumn]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


# Build the Window and setting the title
window = Tk()
window.title("Tic-Tac-Toe")

# Setting up the player
players = ["X", "O"]
currentPlayer = random.choice(players)

# Organise the layout for the buttons
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# showing the state of the game or the current player
label = Label(text=currentPlayer + " turn", font=('consoles', 40))
label.pack(side="top")

# resets the game by calling the new_game function
reset_button = Button(text="Restart", font=('consoles', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

# Build the grid and the buttons
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consoles', 20), width=5, height=2,
                                      command=lambda buttonRow=row, buttonColumn=column: player_turn(buttonRow,
                                                                                                     buttonColumn))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
