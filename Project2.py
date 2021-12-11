import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("500x500")
root.title('CS Jeopardy!')
root.resizable(False, False)

finishScreen=tk.Frame(root, bg="#00008b", padx=5, pady=5)
finishScreen.place(x=0, y=0, relwidth=1.0, relheight=1.0)
question = tk.Frame(root, bg="#00008b", padx=5, pady=5)
question.place(x=0, y=0, relwidth=1.0, relheight=1.0)
board = tk.Frame(root, bg="#00008b", padx=5, pady=5)
board.place(x=0, y=0, relwidth=1.0, relheight=1.0)


multipleChoice=0
playerAnswer=""
score=0
correct=1

questionsAnswered=0


# configure the grid
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=0)


continueButton=tk.Button(question, text="Press to continue",command=board.tkraise)

scoreLabel=tk.Label(question,text=("Your score is: "+str(score)))
scoreLabel.pack(side=tk.BOTTOM)
scoreLabel1=tk.Label(board,text=("Your score is: "+str(score)))
scoreLabel1.grid(row=8,column=0)

add=1

        

def twoChoices():
    question.tkraise()
    aButton.place(x=200, y=425)
    bButton.place(x=250, y=425)
    cButton.place_forget()
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def threeChoices():
    question.tkraise()
    aButton.place(x=175, y=425)
    bButton.place(x=225, y=425)
    cButton.place(x=275, y=425)
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def fourChoices():
    question.tkraise()
    aButton.place(x=150, y=425)
    bButton.place(x=200, y=425)
    cButton.place(x=250, y=425)
    dButton.place(x=300, y=425)
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def fiveChoices():
    question.tkraise()
    aButton.place(x=125, y=425)
    bButton.place(x=175, y=425)
    cButton.place(x=225, y=425)
    dButton.place(x=275, y=425)
    eButton.place(x=325, y=425)
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
def sixChoices():
    question.tkraise()
    aButton.place(x=50, y=425)
    bButton.place(x=100, y=425)
    cButton.place(x=150, y=425)
    dButton.place(x=200, y=425)
    eButton.place(x=250, y=425)
    fButton.place(x=300, y=425)
    gButton.place_forget()
    hButton.place_forget()
def sevenChoices():
    question.tkraise()
    aButton.place(x=75, y=425)
    bButton.place(x=125, y=425)
    cButton.place(x=175, y=425)
    dButton.place(x=225, y=425)
    eButton.place(x=275, y=425)
    fButton.place(x=325, y=425)
    gButton.place(x=375, y=425)
    hButton.place_forget()
def eightChoices():
    question.tkraise()
    aButton.place(x=0, y=425)
    bButton.place(x=50, y=425)
    cButton.place(x=100, y=425)
    dButton.place(x=150, y=425)
    eButton.place(x=200, y=425)
    fButton.place(x=250, y=425)
    gButton.place(x=300, y=425)
    hButton.place(x=350, y=425)


optionAnswers=0
aButton = tk.Button(question, text="a")
bButton =tk.Button(question,text="b")
cButton =tk.Button(question,text="c")
dButton =tk.Button(question,text="d")
eButton=tk.Button(question,text="e")
fButton = tk.Button(question, text="f")
gButton =tk.Button(question,text="g")
hButton =tk.Button(question,text="h")
correctOrWrong=tk.Label(question,text="")
correctOrWrong.pack(side=tk.TOP)


def rightAnswer():
    correctOrWrong.configure(text=" Correct ")
    aButton.place_forget()
    bButton.place_forget()
    cButton.place_forget()
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
    continueButton.place(x=175,y=425)
    scoreLabel.config(text="Your score is: "+str(score))
    scoreLabel1.config(text="Your score is: "+str(score))
def wrongAnswer():
    correctOrWrong.configure(text="Incorrect")
    aButton.place_forget()
    bButton.place_forget()
    cButton.place_forget()
    dButton.place_forget()
    eButton.place_forget()
    fButton.place_forget()
    gButton.place_forget()
    hButton.place_forget()
    continueButton.place(x=175,y=425)
def rightAnswerA():
    aButton.config(command=rightAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerB():
    aButton.config(command=wrongAnswer)
    bButton.config(command=rightAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerC():
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=rightAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerD():
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=rightAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerE():
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=rightAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerF():
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=rightAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerG():
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=rightAnswer)
    hButton.config(command=wrongAnswer)
def rightAnswerH():
    aButton.config(command=wrongAnswer)
    bButton.config(command=wrongAnswer)
    cButton.config(command=wrongAnswer)
    dButton.config(command=wrongAnswer)
    eButton.config(command=wrongAnswer)
    fButton.config(command=wrongAnswer)
    gButton.config(command=wrongAnswer)
    hButton.config(command=rightAnswer)






img01 = tk.PhotoImage(file="IfElse200.png")
img01_fit = img01.subsample(2)
img02 = tk.PhotoImage(file="IfElse400.png")
img02_fit = img02.subsample(2)
img03 = tk.PhotoImage(file="IfElse600.png")
img03_fit = img03.subsample(2)
img04 = tk.PhotoImage(file="IfElse800.png")
img04_fit = img04.subsample(2)
img05 = tk.PhotoImage(file="IfElse1000.png")
img05_fit = img05.subsample(2)
img06 = tk.PhotoImage(file="while200.png")
img06_fit = img06.subsample(2)
img07 = tk.PhotoImage(file="while400.png")
img07_fit = img07.subsample(2)
img08 = tk.PhotoImage(file="while600.png")
img08_fit = img08.subsample(2)
img09 = tk.PhotoImage(file="while800.png")
img09_fit = img09.subsample(2)
img10 = tk.PhotoImage(file="while1000.png")
img10_fit = img10.subsample(2)
img11 = tk.PhotoImage(file="ListsAndCollections200.png")
img11_fit = img11.subsample(2)
img12 = tk.PhotoImage(file="ListsAndCollections400.png")
img12_fit = img12.subsample(2)
img13 = tk.PhotoImage(file="ListsAndCollections600.png")
img13_fit = img13.subsample(2)
img14 = tk.PhotoImage(file="ListsAndCollections800.png")
img14_fit = img14.subsample(2)
img15 = tk.PhotoImage(file="ListsAndCollections1000.png")
img15_fit = img15.subsample(2)
img16 = tk.PhotoImage(file="functions200.png")
img16_fit = img16.subsample(2)
img17 = tk.PhotoImage(file="functions400.png")
img17_fit = img17.subsample(2)
img18 = tk.PhotoImage(file="functions600.png")
img18_fit = img18.subsample(2)
img19 = tk.PhotoImage(file="functions800.png")
img19_fit = img19.subsample(2)
img20 = tk.PhotoImage(file="functions1000.png")
img20_fit = img20.subsample(3)



pictureLabel = tk.Label(question, font = "50") 
pictureLabel.pack()

y=0





#IfElse Loops
def ifElseStat200():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img01_fit)
    fourChoices()
    rightAnswerD()
    ifElse200.grid_forget()
    print(y)
def ifElseStat400():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img02_fit)
    fiveChoices()
    rightAnswerC()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    ifElse400.grid_forget()
    print(y)
def ifElseStat600():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img03_fit)
    sevenChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ifElse600.grid_forget()
    
def ifElseStat800():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img04_fit)
    twoChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ifElse800.grid_forget()
    
def ifElseStat1000():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img05_fit)
    eightChoices()
    rightAnswerD()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ifElse1000.grid_forget()
    
#while loops
def while200():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img06_fit)
    twoChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    whileLoop200.grid_forget()
    
def while400():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img07_fit)
    fourChoices()
    rightAnswerC()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    whileLoop400.grid_forget()
def while600():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img08_fit)
    fiveChoices()
    rightAnswerE()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    whileLoop600.grid_forget()
def while800():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img09_fit)
    fiveChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    whileLoop800.grid_forget()
def while1000():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img10_fit)
    fiveChoices()
    rightAnswerC()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    whileLoop1000.grid_forget()
#lists and collections
def listsAndCollect200():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img11_fit)
    threeChoices()
    rightAnswerA()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ListsAndCollections200.grid_forget()
def listsAndCollect400():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img12_fit)
    sixChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ListsAndCollections400.grid_forget()
def listsAndCollect600():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img13_fit)
    threeChoices()
    rightAnswerA()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ListsAndCollections600.grid_forget()
def listsAndCollect800():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img14_fit)
    eightChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ListsAndCollections800.grid_forget()
def listsAndCollect1000():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img15_fit)
    sixChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    ListsAndCollections1000.grid_forget()
#functions
def function200():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img16_fit)
    sixChoices()
    rightAnswerF()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    Functions200.grid_forget()
def function400():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img17_fit)
    twoChoices()
    rightAnswerB()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    Functions400.grid_forget()
def function600():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img18_fit)
    twoChoices()
    rightAnswerA()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    Functions600.grid_forget()
def function800():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img19_fit)
    fourChoices()
    rightAnswerD()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    
    
    Functions800.grid_forget()
def function1000():
    correct==0
    correctOrWrong.config(text="")
    continueButton.place_forget()
    question.tkraise()
    pictureLabel.configure(image=img20_fit)
    sixChoices()
    rightAnswerE()
    if(correct==1):
        global score
        score=score+200
    if(correct==0):
        score=score+0
    Functions1000.grid_forget()

ifElseLabel=tk.Label(board, text="If-Else \n Statements").grid(row=0,column=0)
ifElse200=tk.Button(board,text="200",height = 2, width = 6,command=ifElseStat200)
ifElse200.grid(row=1,column=0,padx=10,pady=5)
ifElse400=tk.Button(board,text="400",height = 2, width = 6,command=ifElseStat400)
ifElse400.grid(row=2,column=0,padx=10,pady=5)
ifElse600=tk.Button(board,text="600",height = 2, width = 6,command=ifElseStat600)
ifElse600.grid(row=3,column=0,padx=10,pady=5)
ifElse800=tk.Button(board,text="800",height = 2, width = 6,command=ifElseStat800)
ifElse800.grid(row=4,column=0,padx=10,pady=5)
ifElse1000=tk.Button(board,text="1000",height = 2, width = 6,command=ifElseStat1000)
ifElse1000.grid(row=5,column=0,padx=10,pady=5)

whileLabel=tk.Label(board,text="While \n Loops").grid(row=0,column=1,padx=10,pady=5)
whileLoop200=tk.Button(board,text="200",height = 2, width = 6,command=while200)
whileLoop200.grid(row=1,column=1,padx=10,pady=5)
whileLoop400=tk.Button(board,text="400",height = 2, width = 6,command=while400)
whileLoop400.grid(row=2,column=1,padx=10,pady=5)
whileLoop600=tk.Button(board,text="600",height = 2, width = 6,command=while600)
whileLoop600.grid(row=3,column=1,padx=10,pady=5)
whileLoop800=tk.Button(board,text="800",height = 2, width = 6,command=while800)
whileLoop800.grid(row=4,column=1,padx=10,pady=5)
whileLoop1000=tk.Button(board,text="1000",height = 2, width = 6,command=while1000)
whileLoop1000.grid(row=5,column=1,padx=10,pady=5)

ListsAndCollectionsLabel=tk.Label(board,text="List and \n Collections").grid(row=0,column=2,padx=10,pady=5)
ListsAndCollections200=tk.Button(board,text="200",height = 2, width = 6,command=listsAndCollect200)
ListsAndCollections200.grid(row=1,column=2,padx=10,pady=5)
ListsAndCollections400=tk.Button(board,text="400",height = 2, width = 6,command=listsAndCollect400)
ListsAndCollections400.grid(row=2,column=2,padx=10,pady=5)
ListsAndCollections600=tk.Button(board,text="600",height = 2, width = 6,command=listsAndCollect600)
ListsAndCollections600.grid(row=3,column=2,padx=10,pady=5)
ListsAndCollections800=tk.Button(board,text="800",height = 2, width = 6,command=listsAndCollect800)
ListsAndCollections800.grid(row=4,column=2,padx=10,pady=5)
ListsAndCollections1000=tk.Button(board,text="1000",height = 2, width = 6,command=listsAndCollect1000)
ListsAndCollections1000.grid(row=5,column=2,padx=10,pady=5)

FunctionsLabel=tk.Label(board,text="Functions").grid(row=0,column=3,padx=10,pady=5)
Functions200=tk.Button(board,text="200",height = 2, width = 6,command=function200)
Functions200.grid(row=1,column=3,padx=10,pady=5)
Functions400=tk.Button(board,text="400",height = 2, width = 6,command=function400)
Functions400.grid(row=2,column=3,padx=10,pady=5)
Functions600=tk.Button(board,text="600",height = 2, width = 6,command=function600)
Functions600.grid(row=3,column=3,padx=10,pady=5)
Functions800=tk.Button(board,text="800",height = 2, width = 6,command=function800)
Functions800.grid(row=4,column=3,padx=10,pady=5)
Functions1000=tk.Button(board,text="1000",height = 2, width = 6,command=function1000)
Functions1000.grid(row=5,column=3,padx=10,pady=5)



root.mainloop()
