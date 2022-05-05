# Python Libraries
import sys

# My libraries
import card
import game

class Menu:
    def start():
        print('''
    ======================================
            Welcome to BINGO!

            Select an option:
            1 - Play Bingo
            2 - Generate your Bingo Card
            3 - Quit

    ======================================
    ''')
        option = input('Please enter your choice here: ')
        option = int(option)

        if option == 1:
            print('Starting...\n')
            game.Game.start()
        elif option == 2:
            print('Generating card...\n')
            print(card.Card.generate_card())
            Menu.new_card()
        elif option == 3:
            print('Bye')
            sys.exit(0)
        else:
            print('Enter a valid command')

    def new_card():
        answer = "Y"
        while answer == "Y":
            print("Generate new Bingo Card?")
            answer = input("Y/N: ").upper()
            if answer == "Y":
                print(card.Card.generate_card())
            elif answer == "N":
                Menu.start()
            else:
                print("#!# Invalid answer. Try again #!#")
                answer = "Y"