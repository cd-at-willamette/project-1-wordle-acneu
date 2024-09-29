########################################
# Name: Anika Neu
# Collaborators (if any): Quad Center
# GenAI Transcript (if any): N/A
# Estimated time spent (hr): 2
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        row_number = gw.get_current_row()
        string = "" #empty string to add letters to it
        for i in range(N_COLS): #creating a loop
            letter = gw.get_square_letter(row_number, i) #adding letters each word
            string += letter
        if is_english_word(string) and len(str(string)) == 5: #making sure that there is an input of 5 letters AND is an english word
            gw.show_message("That's a 5 letter English word!") #
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
            gw.show_message("Not in word list, sorry!") #if the word entered is not in the word list

    def find_random_word():
        random_word = ""
        while len(random_word) != 5:
            random_word = random.choice(ENGLISH_WORDS)
        return(random_word)

    correct_word = find_random_word()
    print(correct_word)

    def change_rows(string):
        if correct_word != string:
            current = gw.get_current_row()
            if current != N_ROWS - 1:
                current = current + 1
                gw.set_current_row(current)
            elif current == N_ROWS - 1:
                gw.show_message("Sorry, you lose")
        else:
            gw.show_message("You win!")

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
                    gw.set_key_color(letter, MISSING_COLOR


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
