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
    # .join() removes the brackets and commas
    print(f"Let's Begin! The length of the word is {length_of_word} letters.\n\
{' '.join(letters_in_correct_word)}\n\
You have {tries} tries.\n")
    # This is the step for counting word length
    while tries > 0:
        guess = input("Guess a letter: ").lower()
        # this code allows the capital or lower to work
        if len(guess) >= 2:
            print("Invalid input.")
            # More than one letter is invalid, let them try again
            print(f"Please Try Again! \
The length of the word is\
{length_of_word} letters.\n\
{' '.join(letters_in_correct_word)}\n\
You still have {tries} tries.")
            print(f"Your wrong choices so far are: \
{', '.join(wrong_choices)}\n")
        else:
            # words used previously cannot be used again by using this code:
            if guess not in correct_word:
                if guess in wrong_choices:
                    print("Letter has already been used")
                # this line of code reduces the tries
                else:
                    tries -= 1
                    print(f"Wrong! You have {tries} more tries.")
                    wrong_choices.append(guess)
                    # adds wrong letters to wrong_choices list
                    print(f"Your word is {' '.join(letters_in_correct_word)}")
                    print(f"Your wrong choices so far are: \
{', '.join(wrong_choices)}\n")
# ','.join() removes the brackets and reintroduces the comma
                    if tries == 0:
                        print(f'You Lose! The correct answer was: "\
{correct_word}" ')
            else:
                # this alerts the user: letter has been input before
                if guess in letters_in_correct_word:
                    print("Letter has already been used")
                else:
                    for i in range(len(letters_in_correct_word)):
                        if guess == correct_word[i]:
                            letters_in_correct_word[i] = guess
                    print(f"Correct!\n{' '.join(letters_in_correct_word)}")
                    print(f"Your wrong choices so far are: \
{', '.join(wrong_choices)}\n")
                if correct_word == "".join(letters_in_correct_word):
                    print(
                            f'You win!  You got the word \
"{correct_word}" ')
                    print(' ')
                    break

    play = input('Do you want to play a game?  (y/n?) ').lower()
    if (play == 'y'):
        print(' ')
        play_game()


if __name__ == "__main__":
    play_game()
