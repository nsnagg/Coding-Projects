import random as rd
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
the_word = rd.choice(word_list)
print(the_word)

placeholder = ""
for i in range(len(the_word)):
    placeholder += "_"

game_over = False
correct_letter = []
used_letters = ""
attempt = 6
print(stages[attempt])

while not game_over:
    print("**************************** HANGMAN GAME *****************************")
    display = ""
    guess = input("Guess a letter ").lower()

    # User feedback
    if guess not in the_word and guess not in used_letters:
        attempt -= 1
        print(stages[attempt])
    else:
        print(stages[attempt])

    if guess in used_letters:
        print(f"'{guess}' has already been used")
    else:
        used_letters += guess

    for letter in the_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter or letter in used_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print("Letters used already")
    print(used_letters)

    # Exit loop
    if "_" not in display:
        game_over = True
        print("You win!!")
    elif attempt == 0:
        game_over = True
        print("You are dead")








