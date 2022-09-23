# → 5x5 matrix of numbers randomly printed.

# → Numbers are unique.

# → Each column have an specific range.
# B = 1 to 15
# I = 16 to 30
# N = 31 to 45 (Middle is free)
# G = 46 to 60
# O = 61 to 75

import random

class Card:
    print_card = ''
    def generate_card():
        """
        Generates a bingo card and stores the numbers in a dictionary.
        """
        card = {
            "B": [],
            "I": [],
            "N": [],
            "G": [],
            "O": [],
        }
        min = 1
        max = 16
        for letter in card:
            card[letter] = random.sample(range(min, max), 5)
            min += 15
            max += 15
            if letter == "N":
                card[letter][2] = "X" # free space!

        # Organise the colums of numbers
        B = card["B"]
        I = card["I"]
        N = card["N"]
        G = card["G"]
        O = card["O"]

        """
        Add a space after the number if number in B is minor as 10
        in order to display the card correctly.
        """
        for i in range(5):
            if B[i] < 10:
                B[i] = str(B[i]) + " "

        Card.print_card = (f''' 
    Here is your Bingo Card. Write down your numbers!

     B   |   I   |   N   |   G   |   O
     {B[0]}  |   {I[0]}  |   {N[0]}  |   {G[0]}  |   {O[0]}
     {B[1]}  |   {I[1]}  |   {N[1]}  |   {G[1]}  |   {O[1]}
     {B[2]}  |   {I[2]}  |   {N[2]}   |   {G[2]}  |   {O[2]}
     {B[3]}  |   {I[3]}  |   {N[3]}  |   {G[3]}  |   {O[3]}
     {B[4]}  |   {I[4]}  |   {N[4]}  |   {G[4]}  |   {O[4]}
     ''')

        return Card.print_card

