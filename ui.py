from tkinter import *
from quiz import Quiz
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.quiz = Quiz()
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(text=f'Score: {self.quiz.score}',bg=THEME_COLOR,fg='white',anchor='center')
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150,125,text=f'{self.quiz.current_question}',font=('Arial',12,'italic'),width=250)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.tick = PhotoImage(file='images\\true.png')
        self.cross = PhotoImage(file='images\\false.png')

        self.right = Button(image=self.tick,width=100,height=97,highlightthickness=0,command=self.yes)
        self.right.grid(column=0,row=2)

        self.wrong = Button(image=self.cross,width=100,height=97,highlightthickness=0,command=self.no)
        self.wrong.grid(column=1,row=2)

        self.window.mainloop()

    def next(self):
        self.canvas.config(bg='white')
        if self.quiz.current > 8:
            self.canvas.itemconfigure(self.question_text,text='Game Over')
            self.right.config(state='disable')
            self.wrong.config(state='disable')
            restart_button = Button(text='Restart',command=self.restart)
            restart_button.grid(column=0,row=0)
        else:
            self.right.config(state='normal')
            self.wrong.config(state='normal')
            self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text,text=f'{self.quiz.current_question}')

    def yes(self):
        answer = 'True'
        if answer == self.quiz.current_answer:
            self.check(True)
        else:
            self.check(False)

    def no(self):
        answer = 'False'
        if answer == self.quiz.current_answer:
            self.check(True)
        else:
            self.check(False)

    def check(self,correct):
        if correct:
            self.quiz.score = self.quiz.score + 1
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.right.config(state='disable')
        self.wrong.config(state='disable')
        self.window.after(1000,self.next)

    def restart(self):
        self.quiz.refresh()
        self.canvas.itemconfigure(self.question_text,text=f'{self.quiz.current_question}')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        self.right.config(state='normal')
        self.wrong.config(state='normal')