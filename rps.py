#!/usr/bin/python3

# Rocks Paper Scissors
# Created by Nicholas Lueth

from random import choice
from os import system, name

def clear():
    """
    This function produces a terminal clear dependent on which operating sytem you are using."""
    # If you are using a Windows system
    if name == "nt":
        _ = system("cls")
    # If you are using a unix-based system
    else:
        _ = system("clear")


def get_best_of():
    while True:
        try:
            best_of = int(input("What should this game be the best of?: "))
        except ValueError:
            print("Please type an odd integer.")
        else:
            if best_of % 2 == 0:
                print("Please type an odd integer.")
                continue
            else:
                break
    return best_of

class Game:
    _options = {"r": "Rock", "p": "Paper", "s": "Scissor"} 
    def __init__(self, best_of):
        self.your_score = 0
        self.comp_score = 0
        self.hand = None
        self.comp_hand = None
        self.best_of = best_of
        self.goal_score = int((best_of/2)+.5)

    def play(self):
        while self.your_score != self.goal_score and self.comp_score != self.goal_score:
            self.print_header()
            self.comp_hand = choice(list(self._options.keys()))
            self.hand = input("What's your move?: ").lower()
            if self.hand not in self._options.keys():
                print("That is not a valid option, please refer to the key.")
                input("Press enter to continue...")
                continue
            print(f"\nYour opponent played {self._options[self.comp_hand]}")
            if self.hand == self.comp_hand:
                self.tie()
            elif self.hand == "r" and self.comp_hand == "s":
                self.win()
            elif self.hand == "p" and self.comp_hand == "r":
                self.win()
            elif self.hand == "s" and self.comp_hand == "p":
                self.win()
            else:
                self.lose()
            input("Press enter to continue...")
        print()
        if self.your_score == self.goal_score:
            self.print_header()
            print("Congradulations, you won!\n")
        else:
            self.print_header()
            print("Better luck next time...\n")
        self.play_again()

    def print_header(self):
            clear()
            print("KEY:\nr = rock\np = paper\ns = scissors\n")
            print(f"It is a best of {self.best_of}!\nYour score: {self.your_score}\nComputer score: {self.comp_score}\n")

    def tie(self):
        print("It's a tie!")

    def win(self):
        self.your_score += 1
        print("You won a round!")

    def lose(self):
        self.comp_score += 1
        print("You lost a round!")
    
    def play_again(self):
        while True:
            pg = input("Would you like to play again? (y/n): ")
            if pg == "y":
                self.reset()
                self.play()
            elif pg == "n":
                exit(0)
            else:
                print("Invalid format, please type either y for yes, or n for no to play again.")
                input("Press enter to continue...")

    def reset(self):
        self.your_score = 0
        self.comp_score = 0
        self.hand = None
        self.comp_hand = None
        self.best_of = get_best_of()
        self.goal_score = int((self.best_of/2)+.5)

if __name__ == "__main__":
    # Clear console of everything but the game
    clear()
    # Creates the initial game object
    my_game = Game(get_best_of())
    # Start playing the game
    my_game.play()
