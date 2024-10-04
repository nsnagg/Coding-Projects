'''
Rock-paper-scissors:user vs computer
'''
import os
import random
# can also try import random as rd

# Rock beats Scissors
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper beats Rock
paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Scissors beat Paper
scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]

# Clearing the Screen
os.system("cls")

# Human choice
human_choice = int(input("Enter number: 0-Rock, 1-Paper, or 2-Scissors: "))
print("Your Choice:")
print(images[human_choice])

# Computer choice
computer_choice = random.randint(0, 2)

print("The Computers Choice")
print(images[computer_choice])

# Select Winner
if ((human_choice == 0 and computer_choice == 2)
        or (human_choice == 1 and computer_choice == 0)
        or (human_choice == 2 and computer_choice == 1)):
    print("You Win!!!")
elif human_choice == computer_choice:
    print("You Tied")
else:
    print("You Loose")

print(f"Human choice is: {human_choice}")
print(type(human_choice))

print(f"Computer choice is: {computer_choice}")
print(type(computer_choice))
