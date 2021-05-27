from data import Data
import html

class Quiz:
    def __init__(self):
        self.refresh()

    def next_question(self):
        self.current = self.current + 1
        self.current_question = f'Q{self.current+1}.{html.unescape(self.questions[self.current][0])}'
        self.current_answer = self.questions[self.current][1]

    def refresh(self):
        self.data = Data()
        self.score = 0
        self.questions = self.data.questions
        self.current = 0
        self.current_question = f'Q{self.current+1}.{html.unescape(self.questions[self.current][0])}'
        self.current_answer = self.questions[self.current][1]