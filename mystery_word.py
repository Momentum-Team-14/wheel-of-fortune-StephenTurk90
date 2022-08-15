# # import random
# """Downloads random number generator"""

correct_list = []
wrong_list = []


# def play_game():
#     pass
#
#
#
# 
#
#
#
#
#

def guess_letters(word):
    letters_in_correct_word = ["_" for letter in word]
    tries = 8
    while tries > 0:
        guess_letter = input("Guess a letter: ")
        if guess not in correct_word:
            tries -= 1
            print(f"Wrong, have {tries} more tries")
        else:
            for i in range(len(letters_in_correct_word)):
                if guess == letters_in_correct_word[i]:
                    letters_in_correct_word[i] = guess
            print(letters_in_correct_word)

guess_letters(correct_word)
# create blank board based on the letter

# if __name__ == "__main__":
#     play_game()

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         mystery_word(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
# this bring up an error message if the txt file does not exist