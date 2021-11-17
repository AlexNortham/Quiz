class Geography():
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
        self.askQuestion("what is the capital of France?: ", "Paris")
        self.askQuestion("what country is Brussels in?: ", "Belgium")

    def run(self):
        self.runQuiz()
        print(self.score)
