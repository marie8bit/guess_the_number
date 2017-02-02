import random
import sys

correct = 'you guessed correctly after '
too_low = 'too low'
too_high = 'too high'

def main():
    #initialize guess count variable
    guessNum = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:

        #count guesses
        guessNum += 1
        guess = get_guess()
        #send count with function call
        result = check_guess(guess, secret, guessNum)
        print(result)
        #adjust result to include count and allow for the ending of the program
        if (result == correct+str(guessNum)+ ' tries!'):
            again()

def configure_range():
    '''Set the high and low values for the random number'''
    while True:
        print ("What is the lowest number to be guessed?")
        try:
            low = int(input())
            break
        except:
            print("Please enter an int")
    while True:
        print ("What is the highest number to be guessed?")
        try:
            high = int(input())
            break
        except:
            print("Please enter an int")
    return low, high


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    # while loop to make sure user is entering a number
    while True:
        try:
            userInput = int(input('Guess the secret number? '))
            break
        except ValueError:
            print('please enter a int')

    return userInput


def check_guess(guess, secret, guessNum):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        #add count to user information
        return correct+str(guessNum)+ ' tries!'
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high
def again():
    print()
    play_again = input("Would you like to play again? yes or no:")
    if play_again.lower().startswith('y'):
        main()
    else:
        sys.exit()





if __name__ == '__main__':
    main()
