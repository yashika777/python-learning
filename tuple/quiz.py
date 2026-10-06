# Quiz Application (Mixed)
# Quiz structure
# quiz = {
#     "What is the capital of India?": {
#         "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
#         "answer": "Delhi"
#     },
#     "Which data type is immutable?": {
#         "options": ["List", "Dictionary", "Tuple", "Set"],
#         "answer": "Tuple"
#     }}
# Track scores (List)
# scores = []
# Track attempted students (Set)
# attempted = set()
# Features to implement:
# 1. Display questions one by one
# 2. Take user answers
# 3. Calculate score
# 4. Store score in list
# 5. Track student ID in set
# 6. Display average score
# 7. Show pass/fail (passing: 60%)
quiz = {
    "What is the capital of India?": {
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    "Which data type is immutable in Python?": {
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    },
    "Which keyword is used to define a function in Python?": {
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    "Which data structure stores unique values?": {
        "options": ["List", "Tuple", "Set", "String"],
        "answer": "Set"
    },
    "What is the output of 2 + 3 * 4?": {
        "options": ["20", "14", "24", "10"],
        "answer": "14"
    },
    "Which method is used to add an item to a list?": {
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "append()"
    },
    "Which symbol is used for comments in Python?": {
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    "Which function is used to find the length of a list?": {
        "options": ["size()", "length()", "count()", "len()"],
        "answer": "len()"
    },
    "Which loop is commonly used when the number of iterations is known?": {
        "options": ["while", "for", "do-while", "repeat"],
        "answer": "for"
    }
}
scores = []
attempted = set()
student_scores = {}
while True:
    print("""
---------- Quiz Application ----------
1. Start Quiz
2. Show Average Score
3. Show Your Score
4. Exit
""")
    dash = int(input("Enter your choice: "))
    if dash == 1:
        student_id = int(input("Enter your student ID: "))
        if student_id in attempted:
            print("You have already attempted the quiz!")
            continue
        attempted.add(student_id)
        correct = 0
        for i, (question, details) in enumerate(quiz.items(), start=1):
            print("\n", i, question)
            for j, option in enumerate(details["options"], start=1):
                print(j, option)
            answer = input("Enter your answer: ")
            if answer == details["answer"]:
                correct += 1
        score = (correct / len(quiz)) * 100
        student_scores[student_id] = score
        scores.append(score)
        print("\nYour score:", score, "%")
        if score >= 60:
            print("Result: PASS")
        else:
            print("Result: FAIL")
    elif dash == 2:
        if len(scores) == 0:
            print("No student has attempted the quiz yet.")
        else:
            average = sum(scores) / len(scores)
            print("Average score:", average, "%")
    elif dash == 3:
        student_id = int(input("Enter your student ID: "))
        if student_id in student_scores:
            print("Your score:", student_scores[student_id], "%")
        else:
            print("You haven't attempted the quiz yet.")
    elif dash == 4:
        print("Exiting... Bye bye!")
        break
    else:
        print("Invalid choice!")
    
            

            

    


                







