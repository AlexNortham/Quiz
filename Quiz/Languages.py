class Languages():
    def __init__(self):
        self.score = 0

    def askQuestion(self,question, answer):
        print(question)
        if(input() == answer):
            self.score += 1
            print("correct")
        else:
            print("incorrect")

    def runQuiz(self):
        self.askQuestion("in what country do they use kanji?: ", "Japan")
        self.askQuestion("how do you say hello in Dutch?: ", "Hallo")

    def run(self):
        self.runQuiz()
        print(self.score)
