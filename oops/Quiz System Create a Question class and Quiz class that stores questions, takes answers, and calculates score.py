class Question:
    def __init__(self,question,answers):
        self.question=question
        self.answers=answers
q1=Question('What is class','Object blueprint')
q2=Question('What is an object','An instance of class')
q3=Question('Defualt return type of constructor','No return type')
q4=Question('What is __init__','Constructor')
questions=[q1,q2,q3,q4]
class Quiz:
    def __init__(self,questions):
        self.questions=questions
    def score(self):
        score=0
        for q in self.questions:
            print(q.question)
            ent=input('Enter answer:')
            if ent.lower()==q.answers.lower():
                score+=1
        return score
quiz=Quiz(questions)
print(quiz.score())




        


