
guess_word = "python"

while True:
    word_guess = input("Enter a word to guess: ").strip().lower()
    if len(word_guess) < 3:
        print("Please enter a word that is at least 3 characters long.")
    elif len(word_guess) > 15:
        print("Please enter a word that is no more than 15 characters long.")
    else:
        if word_guess == guess_word:
            print("You guessed the word correctly!")
            break
        else:
            print("Incorrect guess. Try again.")
            correct_count = sum(
                letter == guess_word[index]
                for index, letter in enumerate(word_guess[:len(guess_word)])
            )
            print(f"You got {correct_count} letters correct.")