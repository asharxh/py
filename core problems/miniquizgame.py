def new_func():
    questions = {
    "What is the capital of france?" : "Paris",
    "What is 5+7 ?" : "12",
    "Which Planet is Red" : "Mars",
}
    score = 0

    print("Welcome to the Mini Quizz game")

    for question, answer in questions.items():
        user_answer = input(questions).strip()
    
        if user_answer.lower() == answer.lower():
            print("Correct\n")
            score += 1
        else:
            print(f"Wrong! the correct answer is {answer}.\n")
        
            print(f"Your final score is {score}/{len(questions)}")
            print("Thanks for playing! ")

new_func()