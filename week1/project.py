def quiz():
    questions = [
        {
            "question": "What keyword is used to create a function in Python?",
            "choices": ["A. def", "B. func", "C. function", "D. lambda"],
            "answer": "A"
        },
        {
            "question": "Which movie won the Academy Award for Best Picture in 2020?",
            "choices": ["A. 1917", "B. Parasite", "C. Joker", "D. Ford v Ferrari"],
            "answer": "B"
        },
        {
            "question": "In Python, what does `len()` do?",
            "choices": ["A. Returns the length of an object", "B. Finds the maximum value", "C. Deletes an element", "D. Checks if a string is empty"],
            "answer": "A"
        },
        {
            "question": "Which character says, 'I'll be back' in *The Terminator*?",
            "choices": ["A. Sarah Connor", "B. The Terminator", "C. Kyle Reese", "D. T-1000"],
            "answer": "B"
        },
        {
            "question": "What is the output of `print(2 ** 3)` in Python?",
            "choices": ["A. 5", "B. 6", "C. 8", "D. 9"],
            "answer": "C"
        }
    ]
    
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        answer = input("Your answer (A/B/C/D): ").upper()
        
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score is: {score}/{len(questions)}")

def main():
    play_again = "Y"
    while play_again.upper() == "Y":
        quiz()
        play_again = input("\nDo you want to play again? (Y/N): ")

if __name__ == "__main__":
    main()
