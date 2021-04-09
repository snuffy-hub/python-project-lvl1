import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_user():
    name = welcome_user()
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        correct_answer = random.randint(0, 100)
        user_answer = prompt.string(f'Question: {correct_answer}\nYour answer: ')
        if int(user_answer) == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            count = 0
    print(f'Congratulations, {name}!')
