import string

letter_dict = {letter: pos + 1 for pos, letter in enumerate(string.ascii_uppercase)}

def main():
    heading()
    opt = get_option()
    key = get_key()
    text = get_text(opt)

    if opt == 'e':
        code = encrypt(text.upper(),key)
        print(f"User encrypted message:\n{code}")
    else:
        message = decrypt(text.upper(),key)
        print(f"User decrypted message:\n{message}")

    again()

def again():
    print("\nWanna continue [Y/N]")
    answer = input("> ")[0].upper()

    if answer == 'Y':
        print()
        return main()
    print("Thank you for playing!")

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
        if not letter.isalpha():
            encrypted += letter
        else:
            origanl = letter_dict[letter]
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
    return encrypted

def decrypt(text, key):
    decrypted = ""

    for letter in text:
        if not letter.isalpha():
            decrypted += letter
        else:
            code = letter_dict[letter]
            orginal = code - key

            if orginal == 0:
                diff_target = 26

                for idx, value in letter_dict.items():
                    if value == diff_target:
                        decrypted += idx

            elif orginal < 0:
                diff_target = 26 + orginal

                for idx, value in letter_dict.items():
                    if value == diff_target:
                        decrypted += idx
            else:

                for idx, value in letter_dict.items():
                    if value == orginal:
                        decrypted += idx
    return decrypted

if __name__ == '__main__':
    main()