from tkinter import *
from PIL import Image,ImageTk
from random import randint


#main window
root=Tk()
root.title("ROCK PAPER SCISSORS")
root.configure(background="#6868AC")

#Pictures
rock_img=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissors_img=ImageTk.PhotoImage(Image.open("scissors.jpg"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock-comp.jpg"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper-comp.jpg"))
scissors_img_comp=ImageTk.PhotoImage(Image.open("scissors-comp.jpg"))

#Insert Pictures
user_label=Label(root,image=rock_img, bg="#6868AC")
comp_label=Label(root,image=rock_img_comp,bg="#6868AC")
comp_label.grid(row=1,   column=4)
user_label.grid(row=1,   column=0)

#indicators
User_indicator=Label(root,font=50,text="USER",bg="#6868AC")
Computer_indicator=Label(root,font=50,text="COMPUTER",bg="#6868AC")
User_indicator.grid(row=0,column=1)
Computer_indicator.grid(row=0,column=3)

#Scores
PlayerScore=Label(root,text=0,bg="#6868AC",fg="white")
ComputerScore=Label(root,text=0,bg="#6868AC",fg="white")
ComputerScore.grid(row=1, column=3)
PlayerScore.grid(row=1, column=1)

#Buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="blue",fg="white",command=lambda :UpdateChoice("rock")).grid(row=2, column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="green",fg="white",command=lambda :UpdateChoice("paper")).grid(row=2,column=2)
scissors=Button(root,width=20,height=2,text="SCISSORS",bg="Red",fg="white",command=lambda :UpdateChoice("scissors")).grid(row=2,column=3)

#UpdateChoice

choices=["rock","paper","scissors"]
def UpdateChoice(x):

#Computerchoices
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissors_img)

#Userchoice
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checkWinner(x,compChoice)

#messages
msg=Label(root,font=50,bg="#6868AC")
msg.grid(row=3,column=2)

#UpdateMessage
def updateMessage(x):
    msg["text"]= x

#Update User score
def updateUserScore():
    score=int(PlayerScore["text"])
    score+=1
    PlayerScore["text"]=str(score)

#Update Computer Score
def updateComputerScore():

    score=int(ComputerScore["text"])
    score+=1
    ComputerScore["text"]=str(score)

#Checkwinner

def checkWinner(player,computer):
    if player==computer:
        updateMessage("IT'S A TIE!!")
    elif player=="rock":
        if computer=="paper":
            updateMessage("YOU LOOSE!!")
            updateComputerScore()
        else:
            updateMessage("YOU WIN!!")
            updateUserScore()
    elif player=="paper":
        if computer=="rock":
            updateMessage("YOU WIN!!")
            updateUserScore()
        else:
            updateMessage("YOU LOOSE!!")
            updateComputerScore()
    elif player=="scissors":
        if computer=="rock":
            updateMessage("YOU LOOSE!!")
        else:
            updateMessage("YOU WIN!!")
            updateUserScore()
    else:
        pass

root.mainloop()