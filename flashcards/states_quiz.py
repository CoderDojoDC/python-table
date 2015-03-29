#!/usr/bin/env python3

import random, os, time

guess = ""
score = 0

def set_up_screen():
    os.system('clear')
    border = '*' * 42
    filler = " " * 40
    print('\n' + border)
    print("*" + filler + "*")
    print('*          State Capitals Quiz!          *')
    print("*" + filler + "*")
    print(border + '\n')
    print("SCORE: {0}\tREMAINING: {1}".format(score, len(data)))

f = open('states_data.txt', 'r')
data = [line.strip().split('\t') for line in f.readlines()]
f.close()

print("Data loaded and ready. Press [q] to quit")

while guess != "q":
    set_up_screen()
    choice_no = random.randint(0,len(data)-1)
    question = data[choice_no][0]
    answer = data[choice_no][1]
    guess = input("\nWhat is the capital of {0}? ".format(question))
    if guess == "q":
        print("Your score was {0}. Bye.\n\n".format(score))
    elif guess == answer:
        score += 1
        data.pop(choice_no)
        print("Correct! You got {0} correct so far. {1} states left!".format(score, len(data)))
        if len(data) == 0:
            print("YOU WIN!!!")
            break
    else:
        print("Wrong! The capital of {0} is {1}.".format(question, answer))
    time.sleep(1)
