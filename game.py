import random
import sys

class Game:
    numbers_list = list(range(1,76))
    called_numbers = []

    def start():
        while True:
            draw = input("Press any key to draw a number, 'B' to call Bingo or 'S' to exit: ").upper()
            if draw != "S" and draw != "B":
                random.shuffle(Game.numbers_list)
                drawn_number = Game.numbers_list.pop()
                print(drawn_number)
                print("") # Just a line break
                Game.called_numbers.append(drawn_number)
            elif draw == "B":
                Game.bingo_call()
            elif draw == "S":
                print('End of the game')
                sys.exit(0)


    def bingo_call():
        print("These are the numbers called: ")
        print(Game.called_numbers)
        print("") # Just a line break
 