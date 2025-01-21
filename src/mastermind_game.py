import random
import re

def set_code():
    colours = ['b', 'y', 'r', 'g', 'o', 'p']
    code = []
    for i in range(4):
        code.append(random.choice(colours))
    return code

def mark_guess(guess, secret_code):
    code = secret_code.copy()
    guess_list = []
    for letter in guess:
        guess_list.append(letter)
    mark = []
    for i in range(0,len(guess_list)):
        if guess_list[i] == code[i]:
            mark.append('b')
            guess_list[i] = None
            code[i] = None
    for i in range(0,len(guess_list)):
        if guess_list[i] in code and guess_list[i] is not None:
            mark.append('w')
            code[code.index(guess_list[i])] = None
    return mark



def play_mastermind():
    secret_code = set_code()
    number_of_guesses = 0
    while True:
        while True:
            guess = input("Please guess a code of four pegs using colours: 'Blue' (b), Yellow (y), Red (r), Green (g), Orange (o), Pink (p)...")
            if re.match(r"^[byrgop]{4}$", guess):
                number_of_guesses+=1
                break
        mark = mark_guess(guess, secret_code)
        if mark != ['b', 'b', 'b', 'b']:
            print(mark)
        else:
            print(f'Congratulations - you cracked the code with {number_of_guesses} guess(es)!')
            break

if __name__ == '__main__':
    play_mastermind()



    





