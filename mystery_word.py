import random


def play_game():
    correct_word = (random.choice(open("words.txt", "r").read().split()))
    # this allows the words in the list to be deciphered
    letters_in_correct_word = ["_" for letter in correct_word]
    length_of_word = len(correct_word)
    # debug
    print(correct_word)
    # debug end
    wrong_choices = []
    tries = 8
    print(f"The length of the word is {length_of_word} letters.\n\
{' '.join(letters_in_correct_word)}\n\
You have {tries} tries.\n")
    # This is the step for counting word length
    while tries > 0:
        guess = input("Guess a letter: ")
        # This letter can be upper or lower case and it should not matter
        # need to make it so cap or lower case both work
        # More than one letter is invalid, let them try again
        # need to make it so only one letter can be used
        # need to make it so words used previously cannot be used again?
        if guess not in correct_word:
            tries -= 1
            print(f"Wrong! You have {tries} more tries.")
            wrong_choices.append(guess)
            print(f"Your word is {' '.join(letters_in_correct_word)}")
            print(f"Your wrong choices so far are: {', '.join(wrong_choices)}\n")
            if tries == 0:
                print(f'You Lose! The correct answer was: "{correct_word}" ')
                print("Do you want to play again?\n")
        else:
            for i in range(len(letters_in_correct_word)):
                if guess == correct_word[i]:
                    letters_in_correct_word[i] = guess
            print(f"Correct!\n{' '.join(letters_in_correct_word)}")
            print(f"Your wrong choices so far are: {', '.join(wrong_choices)}\n")
            if correct_word == "".join(letters_in_correct_word):
                print("You win")
                return
                # need to make a loop


if __name__ == "__main__":
    play_game()
