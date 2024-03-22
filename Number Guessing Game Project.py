from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}')
guess_limit = 3
guess_count = 0

while True:
    try:
        user_guess: int = int(input('Guess: '))
        guess_count += 1
        if guess_count < guess_limit:
            print(f'You have {guess_limit - guess_count} guess(es) remaining.')
        else:
            print(f'You are out of guesses! Better luck next game!')
            break
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it!')
        break

