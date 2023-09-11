
import tkinter
from tkinter import*
import random

questions=[]
answers=[]
correctAnswer =[]
with open(file=r'Questions.txt')as f:
    content=f.readlines()
    #print(content)
    for line in content:
        questions.append(line.strip())

f.close()
#print(questions)

with open(file= r'correctAns.txt') as correct:
    correctChoice=correct.readlines()
    for ln in correctChoice:
        correctAnswer.append(ln.strip())
correct.close()

#print(correctAnswer)

with open("Answers.txt") as textFile:
    for line in textFile:
        answer = [item.strip() for item in line.split(',')]
        answers.append(answer)

textFile.close()
indexes =[]
user_choice = []

def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
     #print(indexes)
#print(answers)  

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#18141D",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Verdana",20),
        background = "#18141D",
        foreground = "#fff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="YOU ARE ABSOLUTELY AMAZING!!!!!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="you did okay, try harder next time")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="WORK HARDER!!!")





def calculateScore():
    global indexes, user_choice,correctAnswer
    m = 0
    score  = 0
    for i in indexes:
        uc = str(user_choice[m])
        ca = correctAnswer[i]
        if uc == ca:
            score = score + 5
        m += 1 
    print(score)
    showresult(score)
         


ques = 1
def selected():
    global radioBtn,user_choice
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radioBtn.get()
    user_choice.append(x)
    radioBtn.set(-1)
    #print(x)
    
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers[indexes[ques]][0]
        r2['text'] = answers[indexes[ques]][1]
        r3['text'] = answers[indexes[ques]][2]
        r4['text'] = answers[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_choice)
        calculateScore()


def startQuiz():
    global lblQuestion,r1,r2,r3,r4

    lblQuestion = Label(
        root, 
        text= questions[indexes[0]],
        font=("Verdana", 16),
        background = "#18141D",
        foreground=("#fff"),
        width=500,
        justify="center",
        wraplength=400,
    )
    lblQuestion.pack(pady=(100,30))

    global radioBtn
    radioBtn =IntVar()
    radioBtn.set(-1)
    r1=Radiobutton(
        root,
        text = answers[indexes[0]][0],
        font=("Verdana",12),
        background = "#18141D",
        foreground=("#fff"),
        value=0,
        variable = radioBtn,
        command = selected,
    )
    r1.pack(pady=5) 

    r2=Radiobutton(
        root,
        text = answers[indexes[0]][1],
        font=("Verdana",12),
        background = "#18141D",
        foreground=("#fff"),
        value=1,
        variable = radioBtn,
        command = selected,
    )
    r2.pack(pady=5) 

    r3=Radiobutton(
        root,
        text = answers[indexes[0]][2],
        font=("Verdana",12),
        background = "#18141D",
        foreground=("#fff"),
        value=2,
        variable = radioBtn,
        command = selected,
    )
    r3.pack(pady=5) 
    r4=Radiobutton(
        root,
        text = answers[indexes[0]][3],
        font=("Verdana",12),
        background = "#18141D",
        foreground=("#fff"),
        value = 3,
        variable = radioBtn,
        command = selected,
    )
    r4.pack(pady=5) 


def startIspressed():
    Title.destroy()
    lblRules.destroy()
    labelInstructions.destroy()
    btnStart.destroy()
    gen()
    startQuiz()
    


root=tkinter.Tk()
root.geometry('700x600')
root.title('MCQ ')
root.config(background="#18141D")
root.resizable(0,0)



         
Title =Label(
    root,
    text="Welcome to my Quiz", 
    font=("Verdana", "25","bold"),
    background="#18141D",
    foreground="#FFF"
    )
Title.pack(pady=(180,20))

btnStart =Button(
    root, text="Start", 
    background="#18141D",
    foreground='#fff',
    relief="raised",
    border=1, font=("Verdana", 20),
    command= startIspressed,
    )
btnStart.pack(pady=(50,0))

labelInstructions=Label(
    root,
    text="Read the rules and \n Click Start",
    background="#18141D",
    foreground="#fff"
)
labelInstructions.pack(pady=(10,100))
 
lblRules=Label(
    root,
    text="\nRULES: \nThis quiz contains 10 questions \nOnce you select the radio button then \nit will take you to the next question\n",
    width = 100,
    font=("Verdana", 12),
    justify="left",
    background="#000000",
    foreground="#fff",

)

lblRules.pack()


mainloop() 