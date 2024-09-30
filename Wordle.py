########################################
# Name: Anika Neu
# Collaborators (if any): Quad Center
# GenAI Transcript (if any): N/A
# Estimated time spent (hr): 10
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
# The main function to play the Wordle game.
    def enter_action():
        row_number = gw.get_current_row()
        string = "" 
        for i in range(N_COLS): 
            letter = gw.get_square_letter(row_number, i) 
            string += letter
        if is_english_word(string) and len(str(string)) == 5:
            gw.show_message("That's a 5 letter English word!")
# Function to color the wordle squares to the correct/incorrect letters and placement
            def color_guess(guess, correct):
                letters_left = guess
                for i in range(len(guess)):
                    if guess[i] == correct[i]:
                        gw.set_square_color(row_number, i, CORRECT_COLOR)
                    elif guess[i] in correct:
                        gw.set_square_color(row_number, i, PRESENT_COLOR)
                    else:
                        gw.set_square_color(row_number, i, MISSING_COLOR)
            color_guess(string.lower(), correct_word)
            color_keys(string.lower(), correct_word)
            change_rows(string.lower())
        else:
            gw.show_message("Not in word list, sorry!")
# Finding a random english word as the answer for the wordle
    def find_random_word():
        random_word = ""
        while len(random_word) != 5:
            random_word = random.choice(ENGLISH_WORDS)
        return(random_word)
    correct_word = find_random_word()
    print(correct_word)
# Changing rows after a guess, and if the guess = correct, not moving rows
    def change_rows(string):
        if correct_word != string:
            current = gw.get_current_row()
            if current != N_ROWS - 1:
                current = current + 1
                gw.set_current_row(current)
            elif current == N_ROWS - 1:
                gw.show_message(f"You lose... The correct word is {correct_word}")
        else:
            gw.show_message("You win!")
# Making the keys of the wordle correspond to the wordle squares
    def color_keys(guess, correct):
        for i in range(N_COLS):
            letter = guess[i]
            color = gw.get_square_color(gw.get_current_row(), i)
            if color == CORRECT_COLOR:
                gw.set_key_color(letter, CORRECT_COLOR)
            elif color == PRESENT_COLOR:
                if gw.get_key_color(letter) != CORRECT_COLOR:
                    gw.set_key_color(letter, PRESENT_COLOR)
            else:
                if gw.get_key_color(letter) == UNKNOWN_COLOR:
                    gw.set_key_color(letter, MISSING_COLOR)


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
