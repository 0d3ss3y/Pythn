import string
letter_dict = {letter: pos + 1 for pos, letter in enumerate(string.ascii_uppercase)}

def main():
    heading()
    code = get_code()

    if code != " ":
        hack(code)

def heading():
    print("Caesar Cipher Hacker")

def get_code():
    print("Enter the encrypted Caesar cipher message to hack.")
    code = input("> ")

    if code == " ":
        print("Invalid Caesar Cipher.")
    return code

def hack(code):
    attempt = ""
    i = 0
    while True:
        if i <= 26:
            for letter in code:

                if not letter.isalpha():
                    attempt += letter
                else:
                    position = letter_dict[letter]
                    org = position-i

                    if org == 0 or org > 0:
                        if org == 0:
                            diff_target = 26
                        else:
                            diff_target = 26 - org

                        for idx,value in letter_dict.items():
                            if value == diff_target:
                                attempt += idx
                    else:
                        for idx,value in letter_dict.items():
                            if value == org:
                                attempt += idx

            print(f"Key #{i}: {attempt}")
            attempt = ""
            i += 1

        else:
            break


if __name__ == '__main__':
    main()