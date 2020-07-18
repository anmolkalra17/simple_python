# Write your code here
import random

game = ['rock', 'paper', 'scissors', '!rating', '!exit']
score = 0

def game_play():
    global score
    computer_choice = random.choice(game)

    if user_input == "paper":
        if computer_choice == 'scissors':
            print("Sorry, but computer chose scissors")
        elif computer_choice == 'rock':
            print("Well done. Computer chose rock and failed")
            score += 100
            write_in_file(name, score)
        elif computer_choice == 'paper':
            print("There is a draw (paper)")
            score += 50
            write_in_file(name, score)
    elif user_input == "rock":
        if computer_choice == 'paper':
            print("Sorry, but computer chose paper")
        elif computer_choice == 'scissors':
            print("Well done. Computer chose scissors and failed")
            score += 100
            write_in_file(name, score)
        elif computer_choice == 'rock':
            print("There is a draw (rock)")
            score += 50
            write_in_file(name, score)
    elif user_input == 'scissors':
        if computer_choice == 'rock':
            print("Sorry, but computer chose rock")
        elif computer_choice == 'paper':
            print("Well done. Computer chose paper and failed")
            score += 100
            write_in_file(name, score)
        elif computer_choice == 'scissors':
            print("There is a draw (scissors)")
            score += 50
            write_in_file(name, score)

def write_in_file(name, score):
    fname = name + ".txt"
    file = open(fname, 'a', encoding="utf-8")
    file.write(score + "\n")
    file.close()

def rating(name):
    fname = name + ".txt"
    file = open(fname, 'r', encoding="utf-8")
    file.read()
    file.close

def gameplay()
    user_input = input()
    k = user_input
    while k:
        if k == '!exit':
            print('Bye!')
            exit()
        elif k in game:
            game_play()
            k = input()
        elif k == '!rating':
            rating(name)
            k = input()
        elif k not in game:
            print('Invalid input')
            k = input()

name = input()
print(f"Hello {name} \n")

gameplay()
game_play()
