def friends_quiz():
    questions = [
        ("We were on a break!", "Ross"),
        ("Joey doesn’t share food!", "Joey"),
        ("Could I *be* wearing any more clothes?", "Joey"),
        ("Welcome to the real world! It sucks. You’re gonna love it!", "Monica"),
        ("I wish I could, but I don’t want to.", "Phoebe"),
        ("How you doin’?", "Joey"),
        ("See? He’s her lobster!", "Phoebe"),
        ("It’s not that common, it doesn’t happen to every guy, and it *is* a big deal!", "Rachel"),
        ("Pivot! Pivot! Pivot!", "Ross"),
        ("Oh. My. God!", "Janice"),
        ("I’m not great at the advice. Can I interest you in a sarcastic comment?", "Chandler"),
        ("It’s like all my life everyone’s told me, ‘You’re a shoe!’", "Rachel"),
        ("That is *brand new* information!", "Phoebe"),
        ("You can’t just give up! Is that what a dinosaur would do?", "Joey"),
        ("I KNOW!", "Monica"),
        ("Come on, Ross! You’re a paleontologist. Dig a little deeper!", "Rachel"),
        ("I don’t even have a ‘pla’.", "Phoebe"),
        ("It’s not that common, it doesn’t happen to every guy, and it *is* a big deal!", "Rachel"),
        ("I stepped up! She’s my friend and she needed help. If I had to, I’d pee on any one of you!", "Joey"),
        ("Gum would be perfection.", "Chandler")
    ]
    
    score = 0
    
    print("Welcome to the Friends Quiz! Guess who said the following lines.")
    
    for i, (quote, answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {quote}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}.")
    
    print(f"\nGame Over! You scored {score} out of {len(questions)}.")
    
if __name__ == "__main__":
    friends_quiz()