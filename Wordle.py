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


#milestone 1
    def enter_action():
        row_number = gw.get_current_row()
        string = "" #empty string to add letters to it
        for i in range(N_COLS): #creating a loop
            letter = gw.get_square_letter(row_number, i) #adding letters each word
            string += letter
        if is_english_word(string) and len(str(string)) == 5: #making sure that there is an input of 5 letters AND is an english word
            gw.show_message("That's a 5 letter English word!") #
        else:
            gw.show_message("Not in word list, sorry!") #if the word entered is not in the word list
        # What should happen when RETURN/ENTER is pressed.

#milestone 2
        def color_guess(guess, correct):
            letters_left = guess
            gw.set_square_color(0,0, CORRECT_COLOR)
            for i in range(len(guess)):
                if guess[i] == correct[i]:
                    gw.set_square_color(row_number, i, CORRECT_COLOR)
                elif guess[i] in correct:
                    gw.set_square_color(row_number, i, PRESENT_COLOR)
                else:
                     gw.set_square_color(row_number, i, MISSING_COLOR)
        color_guess(string.lower(), correct_word)

#milestone 3
    def find_random_word():
        random_word = ""
        while len(random_word) != 5:
            random_word = random.choice(ENGLISH_WORDS)
        return(random_word)

    correct_word = find_random_word()
    print(correct_word)


            


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
