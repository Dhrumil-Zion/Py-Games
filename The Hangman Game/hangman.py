import random

def hangman():  # sourcery no-metrics
    word = random.choice(["dhrumil","zion","smit"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade += guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns -= 1
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break
            elif turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            elif turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            elif turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            elif turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            elif turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            elif turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            elif turns == 9:
                print("9 turns left")
                print("  --------  ")


name = input("Enter your name: ")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()
