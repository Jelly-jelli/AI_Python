from audioop import error
from random import randint


def cal_func(number, attempts):
    guess_num = int(input("Choose your guessing number : "))
    value_fx = guess_num ** 2 - number ** 2
    cal_derivative = 2 * value_fx
    guess_result = guess_num - (guess_num / cal_derivative)
    return guess_result


def guess(attempts,numrange):
    # if we input number is 3
    print('Implement game using Newtons method formular ::: ')
    number = randint(1,numrange)
    print('number : ', number)
    print('square of a number : ', number**2)
    error_tolerance = 0.001

    print("Welcome! Can you guess my secret number?")

    guess_num = int(input("Choose your guessing number : "))
    value_fx = guess_num**2-number**2
    cal_derivative = 2*value_fx
    guess_result = guess_num-(guess_num/cal_derivative)

    while guess_result != number and guess_num > error_tolerance and attempts > 0:
        if guess_result > number and attempts > 0:
            print('Too high')
            print('You have guess remain', attempts)
            attempts -= 1

        elif guess_result < number and attempts > 0:
            print('Too low')
            print('You have guess remain', attempts)
            attempts -= 1


        elif guess_result == number:
            print('Correct')
            attempts -= 1

        else:
            print('Incorrect and no attempts left. BAD LUCK !')
            attempts -= 1

    cal_func(guess_result, attempts)



    print("END-OF-GAME: thanks for playing!")

guess(attempts=3,numrange=5)



