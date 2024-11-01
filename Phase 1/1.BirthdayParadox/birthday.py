import numpy as np
import random
import datetime as dt

def main():
    heading()
    limit = get_limit()
    birthdays = generate_birthdays(limit)
    print(birthdays)

def heading():
    print("Birthday Paradox")

def get_limit():
    print("\nHow many birthdays shall I generate? (Max 100)")
    num = input("> ")

    if num.isdigit() and int(num) > 100:
        return int(num)
    else:
        print("Please enter a valid number.")
        return get_limit()

def generate_birthdays(limit):
    startOfYear = dt.date(2024,1,1)
    birthdays = []

    for i in range(limit):
        birthday = startOfYear + dt.timedelta(days=random.randint(1,365))
        birthdays.append(birthday)
    return birthdays

if __name__ == '__main__':
    main()