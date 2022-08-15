def play_game():
    pass


# create blank board based on the letter

if __name__ == "__main__":
    play_game()




file = Path(args.file)
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Let's play Mystery Word")
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

if file.is_file():
        mystery_word(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
# this bring up an error message if the txt file does not exist
