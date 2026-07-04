def run_quiz(questions):
    score = 0
    
    print("--- WELCOME TO THE PYTHON QUIZ ---")
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        
        # Display options
        for option in q['options']:
            print(option)
            
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}. ❌")
            
    print(f"\n--- QUIZ COMPLETE ---")
    print(f"Your final score: {score}/{len(questions)}")

# Data structure for your quiz
quiz_data = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) define", "D) function"],
        "answer": "B"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": ["A) tuple", "B) string", "C) list", "D) integer"],
        "answer": "C"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    }
]

if __name__ == "__main__":
    run_quiz(quiz_data)
