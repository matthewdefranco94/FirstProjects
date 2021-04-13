#Matthew's first python c0de: Hangman
import random
from secret_words import secret_words

def word_retrieval():
    secret_word = random.choice(secret_words)
    return secret_word.upper()


def play_game(secret_word):
    chosen_word = len(secret_word) * "_"
    guessed = False
    player_attmpt_lttrs = []
    player_attmpt_words = []
    remaining_attempts = 8


    print("Please select a letter or guess a word")
    print(hangman_model(remaining_attempts))
    print(chosen_word)
    
    while not guessed and player_attmpt_lttrs > 0:
        player_guess = input('Guess a letter or a word: ' + str).upper

        #guessing a letter
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in player_attmpt_lttrs:
                print("Letter" , player_guess, "has been used already.")
            elif player_guess != player_attmpt_lttrs:
                print(player_guess, "is not in the word.")
                remaining_attempts -= 1
                player_attmpt_lttrs.append(player_guess)
                print(player_attmpt_lttrs)
            else:
                print(player_guess, "is a correct letter!")
                player_attmpt_lttrs.append(player_guess)
        #copied section
                word_as_list = list(chosen_word)
                indices = [i for i, player_attmpt_lttrs in enumerate(chosen_word) if player_attmpt_lttrs == player_guess]
                for index in indices:
                    word_as_list[index] = player_guess
                chosen_word = "".join(word_as_list)
                if "_" not in chosen_word:
                    player_guess = True
 

        #guessing a word
        elif len(player_guess) == len(chosen_word) and player_guess.isalpha():
            if player_guess in player_attmpt_words:
                print("you guess the word", player_guess)
            elif player_guess != chosen_word:
                print("That is not the correct word")
                remaining_attempts -= 1
                player_attmpt_words.append(player_guess)
            else:
                player_guess = True
                word_completion = chosen_word

        else:
            print("Please use only letters.")
            print(hangman_model(remaining_attempts))
            print(word_completion)
        if guessed:
            print("That is the correct word!")
        else:
            print("You lose They word was", chosen_word ,". Good day, Sir!")




def hangman_model(remaining_attempts):
    model = ["""
            -----------
            |          |
            |          O
            |         \\|/
            |          |
            |         / \\
            """,
            """
            -----------
            |          |
            |          O
            |         \\|/
            |          |
            |         / 
            """,
            """
            -----------
            |          |
            |          O
            |         \\|/
            |          |
            |         
            """,
            """
            -----------
            |          |
            |          O
            |         \\|/
            |        
            |         
            """,
            """
            -----------
            |          |
            |          O
            |         \\|
            |         
            |         
            """,
            """
            -----------
            |          |
            |          O
            |          |
            |          
            |         
            """,
            """
            -----------
            |          |
            |          O
            |         
            |         
            |         
            """,
            """
            -----------
            |          |
            |          
            |         
            |         
            |       
            """
    ]
    return model[remaining_attempts]

def game():
    chosen_word = word_retrieval()
    play_game(word_retrieval())

if __name__ == "__main__":
    game()    

