import string

letter_dict = {letter: pos + 1 for pos, letter in enumerate(string.ascii_uppercase)}

def main():
    heading()
    opt = get_option()
    key = get_key()
    text = get_text(opt)

    if opt == 'e':
        encrypt(text.upper(),key)
    else:
        decrypt(text.upper(),key)

def heading():
    print("Caesar Cipher v1.0")

def get_option():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    opt = input("> ").lower()

    if opt[0] == 'e' or opt[0] == 'd':
        return opt
    get_option()

def get_key():
    print("Please enter the key (0 to 25) to use.")
    key = input("> ")

    if key.isdigit() and 0 <= int(key) <= 25:
        return int(key)
    get_key()

def get_text(opt):
    if opt == 'e':
        print("Enter the message to encrypt.")
    else:
        print("Enter the message to decrypt.")

    message = input("> ")

    if message.isspace() or message == '':
        get_text(opt)
    else:
        return message

def encrypt(text, add):
    encrypted = ""

    for letter in text:
        if letter.isspace() or letter.isdigit() or letter == " ":
            encrypted += letter
        else:
            origanl = letter_dict[letter]
            print(origanl, letter)
            target = origanl + add

            if target > 26:
                diff_target = target - 26

                for idx,value in letter_dict.items():
                    if value == diff_target:
                        encrypted += idx
            else:

                for idx,value in letter_dict.items():
                    if value == target:
                        encrypted += idx
    print(encrypted)
    return encrypted

def decrypt(text, key):
    pass

if __name__ == '__main__':
    main()