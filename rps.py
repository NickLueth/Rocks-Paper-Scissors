#!/usr/bin/python3

# Rocks Paper Scissors
# Created by Nicholas Lueth

# Import choice to choose a random move for the opponent
from random import choice
# Import system and name in order to clear console for organizational purposes
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
    """
    This function get's the number of rounds the game will be best of.
    """
    # Loop until the user gives a valid response
    while True:
        try:
            best_of = int(input("What should this game be the best of?: "))
        # If the response isn't able to cast to an integer, tell them to type an odd integer instead
        except ValueError:
            print("Please type an odd integer.")
        else:
            # If the response isn't an odd number ask them to type an odd number instead
            if best_of % 2 == 0:
                print("Please type an odd integer.")
                continue
            # If the input is valid, break out of the loop
            else:
                break
    return best_of

class Game:
    # The move options
    _options = {"r": "Rock", "p": "Paper", "s": "Scissor"} 
    def __init__(self, best_of):
        # The number of points you have in the game
        self.your_score = 0
        # The number of points the computer has
        self.comp_score = 0
        # The move the player last played
        self.hand = None
        # The move the computer last played
        self.comp_hand = None
        # The number of total possible rounds
        self.best_of = best_of
        # The score each player is trying to get to win
        self.goal_score = int((best_of/2)+.5)

    def play(self):
        # Repeat until a player wins the game
        while self.your_score != self.goal_score and self.comp_score != self.goal_score:
            # Prints the header of the game
            self.print_header()
            # Generates a move for the computer
            self.comp_hand = choice(list(self._options.keys()))
            # Ask the user what they'd like to play for the turn
            self.hand = input("What's your move?: ").lower()
            # If the user doesn't respond with a valid move option, tell them to refer to the key
            if self.hand not in self._options.keys():
                print("That is not a valid option, please refer to the key.")
                input("Press enter to continue...")
                # Continue to the next loop
                continue
            # Display the move that the opponent played
            print(f"\nYour opponent played {self._options[self.comp_hand]}")
            # If there is a tie, run the tie function
            if self.hand == self.comp_hand:
                self.tie()
            # If you win, run the win function
            elif self.hand == "r" and self.comp_hand == "s":
                self.win()
            elif self.hand == "p" and self.comp_hand == "r":
                self.win()
            elif self.hand == "s" and self.comp_hand == "p":
                self.win()
            # If you lose, run the lose function
            else:
                self.lose()
            input("Press enter to continue...")
        # Extra line for organizational purposes
        print()
        # If you win the whole game, show the winner banner
        if self.your_score == self.goal_score:
            self.print_header()
            print("Congradulations, you won!\n")
        # If you lose the whole game, show the loser banner
        else:
            self.print_header()
            print("Better luck next time...\n")
        # Run the play again function to see if the user wants to play again
        self.play_again()

    def print_header(self):
            clear()
            print("KEY:\nr = rock\np = paper\ns = scissors\n")
            print(f"It is a best of {self.best_of}!\nYour score: {self.your_score}\nComputer score: {self.comp_score}\n")

    def tie(self):
        """
        This function prints to the user that the round was a tie.
        """
        print("It's a tie!")

    def win(self):
        """
        This function increases your score and displays to the user that they won the round.
        """
        self.your_score += 1
        print("You won a round!")

    def lose(self):
        """
        This function increases the computer's score and displays to the user that they lost the round.
        """
        self.comp_score += 1
        print("You lost a round!")
    
    def play_again(self):
        """
        This function determins if the user would like to play the game again.
        """
        while True:
            pg = input("Would you like to play again? (y/n): ")
            # If the user wants to play again, reset the values of the game and start the game again
            if pg == "y":
                self.reset()
                self.play()
            # If the user doesn't want to play again, quit
            elif pg == "n":
                exit(0)
            # If the input isn't valid, let the user know what they need to do
            else:
                print("Invalid format, please type either y for yes, or n for no to play again.")
                input("Press enter to continue...")

    def reset(self):
        """
        This function resets the values in the game.
        """
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
