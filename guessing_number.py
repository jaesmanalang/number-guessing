import random
import os

attempts = 0
game_playing = True


def play_game():
    reset()
    global game_playing, attempts
    max_range = get_max_range()
    the_number = number_to_guess(max_range)
    while game_playing:
        guess = player_guess(max_range)
        if check_guess(guess, the_number):
            game_playing = False

    while True:
        choice = str(input('Do you want to play again? y/n: '))
        if choice.lower() == 'y':
            play_game()
        elif choice.lower() == 'n':
            break
        else:
            continue

    print('Thank you for playing.')


def check_guess(guess, the_number):
    global attempts, highest_score
    if guess == the_number:
        print('You guessed it. Congratulations!')
        if attempts > 1:
            print(f"It took {attempts} tries.")
        else:
            print(f"It took only {attempts} try.")
        return True
    elif guess > the_number:
        print('Too high!')
        return False
    else:
        print('Too low!')
        return False


def number_to_guess(max_num):
    return random.randint(1, max_num)


def player_guess(max_num):
    global attempts
    while True:
        try:
            guess = int(input(f'Please guess a number between 1-{max_num}: '))
            attempts += 1
        except ValueError:
            print('Please enter a number.')
        else:
            break
    return guess


def get_max_range():
    while True:
        try:
            max_number = int(input('Please enter the maximum number range: '))
        except ValueError:
            print('Please enter a number.')
        else:
            break
    return max_number


def reset():
    global attempts, game_playing
    attempts = 0
    game_playing = True
    clear()


def clear():
    os.system('cls')


if __name__ == '__main__':
    play_game()
