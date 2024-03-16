from tkinter import *
import random

def new_turn(row,column):
    global player

    if buttons[row][column]['text']=="" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+"->" + " win"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] +"->" + " win"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")






def check_winner():
# entha loop vanthu rows elam check pannum like row 1->[0,0][0,1][0,2]
                                               #row 2->[1,0][1,1][1,2]
                                               #row 3->[2,0][2,1][2,2]
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text'] != "":
            #row win pana blue colour varum
            buttons[row][0].config(bg="orange")
            buttons[row][1].config(bg="white")
            buttons[row][2].config(bg="green")
            return True
#entha loop vanthu column elam check pannum line column 1->[0,0] column 4->[0,1] column 7->[0,2]
                                               # column 2->[1,0] column 5->[1,1] column 8->[1,2]
                                               # column 3->[2,0] column 6->[2,1] column 9->[2,2]
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text'] != "":
            #column win pana yellow color varum
            buttons[0][column].config(bg="orange")
            buttons[1][column].config(bg="white")
            buttons[2][column].config(bg="green")
            return True
#next diagonal same ha erka nu check pannum right to left
    if buttons[0][0]['text'] == buttons[1][1]['text']==buttons[2][2]['text'] !="":
        #right to left diagaonal win pana green colour varum
        buttons[0][0].config(bg="orange")
        buttons[1][1].config(bg="white")
        buttons[2][2].config(bg="green")
        return True
#opposite diaganol same ha erkum nu check pannum left to right
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text'] !="":
        #left to right diagonal win pana green color varum
        buttons[0][2].config(bg="orange")
        buttons[1][1].config(bg="white")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        #elam tie vantha apo elam orange color maridunum
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces=9 #declaring a spaces

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces = spaces-1

    if spaces ==0 :
        return False
    else:
        return True

def new_game():
    global player

    player=random.choice(players)

    label.config(text=(player + " turn"))

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0f0")#this is previews background



window=Tk()
window.title("Tic-Tac-Toe")
logo=PhotoImage(file="game.png")
window.iconphoto(True,logo)
window.geometry("500x500")

players=["X","O"]
player=random.choice(players)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]#2D list buttons

#creating label to display

label=Label(window,text=(player + " turn"),font=("Arial black",25),height=1,width=6,bg="red")
label.pack(side="top")

#reset button to start new_game

reset_button=Button(window,text="Reset",font=("Arial black",20),height=1,width=8,relief=RAISED,bd=4,bg="blue",
                    activebackground="blue",command=new_game)
reset_button.pack(side="top")

#creating frames for buttons

frame=Frame(window,relief=RAISED,bd=4)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font=("Arial black",25),height=1,width=3,
                                    relief=RAISED,bd=5,command=lambda row=row,column=column : new_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()