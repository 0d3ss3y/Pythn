import random

def main():
    heading()
    rules()
    number = generate_random_number()
    play_game(number)





def generate_random_number():
    return random.randint(1, 999)

def rules():
    print("""
I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
    """)

def heading():
    print("Bagels, a deductive logic game.")


if __name__ == '__main__':
    main()