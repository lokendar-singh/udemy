###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
game_digit = 3
def getDigits(n=3):
    digits = list(range(10))
    random.shuffle(digits)
    # print(digits[:3])

    if n>9:
        n=9
    return digits[:n]


# Another hint:
def get_guess():
    flag = True
    while(flag):
        guess = input("What is your guess (guess 3 digits)? ")
        if(type(guess) == type('string') and len(guess)==game_digit):
            return guess

def perfectCheck(guess):
    # print('Perfect check')
    flag = True
    for i in range(len(guess)):
        # print('value of i is: {}'.format(i))
        if int(guess[i]) != int(com_dig[i]):
            # print('perfect check : false')
            flag = False
    return flag


def matchCheck(guess):
    # print('match check : false')
    flag = False
    for i in range(len(guess)):
        # print('Match check '+ str(guess[i]) + ' == '+ str(com_dig[i]))
        if int(guess[i]) == int(com_dig[i]):
            # print('match check : true')
            flag = True
    return flag

def closeCheck(guess):
    flag = False
    for i in range(len(guess)):
        if int(guess[i]) in com_dig:
            flag = True
    return flag

def checkGuess():
    guess = get_guess()

    # print(type(guess), com_dig)
    ct = 0
    if perfectCheck(guess):
        print('Perfect guess, you win!!')
    elif matchCheck(guess):
        print('Match: correct position digit guess, try more!')
        checkGuess()
    elif closeCheck(guess):
        print('Close: correct digit guess, try more!')
        checkGuess()
    else:
        print('No match found')
        checkGuess()

com_dig = getDigits()
checkGuess()
# print('Computer guessed ' + str(com_dig))

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
