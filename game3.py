from questions import questions3

def friends_quiz():

    score = 0
    
    print("Welcome to the Friends Quiz! Guess who said the following lines.")
    
    for i, (quote, answer) in enumerate(questions3, 1):
        print(f"\nQuestion {i}: {quote}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}.")
    
    print(f"\nGame Over! You scored {score} out of {len(questions3)}.")
    
if __name__ == "__main__":
    friends_quiz()