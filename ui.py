from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Some random question",
                                                fill=THEME_COLOR,
                                                font=("Arial", 20, "italic")
                                                )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.r_button = Button(image=right_img, highlightthickness=0, command=self.true_pressed)
        self.r_button.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.w_button = Button(image=wrong_img, highlightthickness=0, command=self.false_pressed)
        self.w_button.grid(column=1, row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.r_button.config(state="disabled")
            self.w_button.config(state="disabled")

    def true_pressed(self):
         self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)