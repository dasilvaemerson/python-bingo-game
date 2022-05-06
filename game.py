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
        Game.bingo_check()
    
    def bingo_check():
        while True:
            try:
                number = int(input("Please, enter a number from the bingo card to check if it was called: "))
            except ValueError:
                print("Invalid input. ONLY NUMBERS. Try again.\n")
                Game.bingo_check()
            if number in Game.called_numbers:
                print(f"Number {number} OK\n")
            else:
                print(f"The number {number} was not called\n")
                Game.resume_game()

    def resume_game():
            answer = "Y"
            while answer == "Y":
                print("Keep playing?")
                answer = input("Y/N: ").upper()
                if answer == "Y":
                    print("") # Just a line break
                    Game.start()
                elif answer == "N":
                    print("") # Just a line break
                    print('End of the game')
                    sys.exit(0)
                else:
                    print("#!# Invalid answer. Try again #!#\n")
                    answer = "Y"
                
 