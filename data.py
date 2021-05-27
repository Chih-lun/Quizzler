import requests

class Data:
    #0 is test, 1 is answer
    def __init__(self):
        self.response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
        self.raw_data = self.response.json()['results']
        self.questions = []
        for i in self.raw_data:
            text = i['question']
            answer = i['correct_answer']
            self.questions.append([text,answer])