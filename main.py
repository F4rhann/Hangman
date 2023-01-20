import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)

    return word.lower()


def hangman():
    word = get_valid_word(words)
    word_leters = set(word)
    alphabets = set(string.ascii_lowercase)
    used_letters = set()

    lives = 5

    while len(word_leters) > 0 and lives > 0:

        word_list = [
            letter if letter in used_letters else "-" for letter in word]

        print(f"Lives: {lives}")
        print("Word:", " ".join(word_list), "\n")
        print("Used Words:", " ".join(used_letters))

        user_guess = input("Guess: ").lower()

        if user_guess in alphabets - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_leters:
                word_leters.remove(user_guess)

            else:
                lives -= 1
                print(f"{user_guess} is not in the word.\n")

        elif user_guess in used_letters:
            print(f"You already used {user_guess}. Try another letter.\n")

        elif user_guess not in alphabets:
            print("Invalid Letter.\n")

    if lives == 0:
        print(f"You lost. The word was {word}.")
    else:
        print("Yo, You guessed the word correct.")


hangman()
