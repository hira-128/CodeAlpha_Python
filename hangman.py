import random

def hangman():
    words = ['python', 'coding', 'intern', 'skill', 'build']
    word = random.choice(words)
    guesses = ''
    turns = 6

    print("Welcome to Hangman!")

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        
        if failed == 0:
            print("\nYou won!")
            break
        
        guess = input("\nGuess a character: ").lower()
        guesses += guess
        
        if guess not in word:
            turns -= 1
            print(f"Wrong! {turns} turns left.")
            
    else:
        print(f"You lost! The word was {word}")

hangman()