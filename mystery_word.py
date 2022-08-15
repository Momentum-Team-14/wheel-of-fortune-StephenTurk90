import random

# with open('text-word.txt', 'r') as file:
#     correct_word = file.read().replace('\n', '')

correct_word = (random.choice(open("words.txt", "r").read().split()))

right_word = []
wrong_list = []
# 2 empty list


def guess_letters(word):
    letters_in_correct_word = ["_" for letter in word]
    tries = 26
    while tries > 0:
        guess = input("Guess a letter: ")
        if guess not in word:
            tries -= 1
            print(f"Wrong, have {tries} more tries")
            if tries == 0:
                print("You Lose!")
                print("Do you want to play again?")
        else:
            for i in range(len(letters_in_correct_word)):
                if guess == word[i]:
                    letters_in_correct_word[i] = guess
            print(letters_in_correct_word)


guess_letters(correct_word)


if __name__ == "__main__":
    guess_letters()
