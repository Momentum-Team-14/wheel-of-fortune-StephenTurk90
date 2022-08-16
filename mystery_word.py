import random

# with open('text-word.txt', 'r') as file:
#     correct_word = file.read().replace('\n', '')

correct_word = (random.choice(open("words.txt", "r").read().split()))
# this allows the words in the list to be deciphered


def guess_letters(word):
    letters_in_correct_word = ["_" for letter in word]
    length_of_word = len(word)
    wrong_choices = []
    tries = 8
    print(f"The length of the word is {length_of_word} letters.\n\
{letters_in_correct_word}\n\
You have {tries} tries.")
    # This is the step for counting word length
    while tries > 0:
        guess = input("Guess a letter: ")
        if guess not in word:
            tries -= 1
            print(f"Wrong, have {tries} more tries")
            wrong_choices.append(guess)
            print(f"Your word is {letters_in_correct_word}")
            print(f"Your wrong choices so far are: {wrong_choices}")
            if tries == 0:
                print("You Lose!")
                print("Do you want to play again?\n \
Choose your first letter to begin.")
        else:
            for i in range(len(letters_in_correct_word)):
                if guess == word[i]:
                    letters_in_correct_word[i] = guess
            print(f"Correct!\n{letters_in_correct_word}")
            print(f"Your wrong choices so far are: {wrong_choices}")


guess_letters(correct_word)


if __name__ == "__main__":
    guess_letters(correct_word)

"""1. at the start let the user know how many letters exist
2a. user to supplies a letter per round
2b. This letter can be upper or lower case and it should not matter
2c. more than one letter is invalid, let them try again
3. Let the user know if their guess appears in the secret word.
4. Display the partially guessed word letters that have not been guessed"""
# Step 1 is done
# Step 2 is partially done, b, and c still needs to be done
# Step 3 is done
# Step 4 is done
"""We still need to make the game loop"""