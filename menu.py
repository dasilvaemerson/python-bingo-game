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

        if option == '1':
            print('Starting...\n')
            # return "Number 1"
            game.Game.start()
        elif option == '2':
            print('Generating card...\n')
            print(card.Card.generate_card())
            Menu.new_card()
        elif option == '3':
            print('Bye')
            return sys.exit(0)
        else:
            print('Enter a valid command')
            return Menu.start() #Restart the Menu Screen

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