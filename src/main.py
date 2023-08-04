import os
import datetime
from datetime import datetime


class PositiveAmount(Exception):
    def __init__(self):
        super().__init__('Amount must > 0')
        self.message = 'Amount must > 0'


class ValidDate(Exception):
    def __init__(self):
        super().__init__('Invalid date. Date must be in the format DD/MM/YYYY')
        self.message = 'Invalid date. Date must be in the format DD/MM/YYYY'


def check_date(date):
    try:
        datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        raise ValidDate


def isAlreadyUsed(username):
    path = os.path.join(os.getcwd(), 'username.txt')
    with open(path, 'r') as file:
        lines = file.readlines()
    users = [line.strip() for line in lines]
    return username in users


def openApp(username):
    print(f'Welcome {username} to the finance app!')
    exit = False
    while exit == False:
        try:
            category = input('Enter category: ')

            time = input('Enter date in the format DD/MM/YYYY: ')
            check_date(time)

            amount = int(input('Enter amount (>0): '))
            if amount <= 0:
                raise PositiveAmount
        except ValidDate as e:
            print('Error:', e)
        except PositiveAmount as e:
            print('Error:', e)
        else:
            # path to file containing user's history
            history_path = os.path.join(
                os.getcwd(), f'user-history/{username}.txt')

            # Handle options in user input
            option_income = input(
                'Do you want to enter income or expense? (i/e): ')

            if option_income == 'e':
                amount = amount * -1

            with open(history_path, 'r') as file:
                total = int(file.readline)

            parsed_time = datetime.strptime(time, "%d/%m/%Y")
            formatted_time = parsed_time.strftime("%d/%m/%Y")

            with open(history_path, 'a') as file:
                file.write(
                    f'{category}, {formatted_time}, {amount}, {option_income}\n')
        finally:
            option_exit = input('Do you want to continue? (y/n): ')
            if option_exit == 'n':
                exit = True
                print('Goodbye!')


if __name__ == '__main__':
    username = input('Enter username: ')
    if not isAlreadyUsed(username):
        option = input(
            'This username has not been created yet. Do you want to create a new account? (y/n): ')
        if option == 'y':
            username_path = os.path.join(os.getcwd(), 'username.txt')

            history_path = os.path.join(
                os.getcwd(), f'user-history/{username}.txt')

            with open(username_path, 'a') as file:
                file.write(username + '\n')

            with open(history_path, 'w') as file:
                file.write('0\n')

            openApp(username)
    else:
        openApp(username)
