# Python Libraries
import sys

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
        elif option == 2:
            print('Generating card...\n')
        elif option == 3:
            print('Bye')
            sys.exit(0)
        else:
            print('Enter a valid command')