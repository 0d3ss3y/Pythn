from bitmap import BitMap

def main():
    heading()
    text = get_input()

    if text.isdigit():
        run_image1()
    else:
        run_image2()

def heading():
    print("Bitmap Message")

def get_input():
    print("Enter the message to display with the bitmap.")
    ans = input("> ")

    if ans == " ":
        get_input()
    return ans

def run_image1():
    image = BitMap(64)
    print(image.tostring())
    image.set(1)
    print(image.tostring())

def run_image2():
    image = BitMap.fromstring("00011101")
    print(image.tostring())
    image.flip(1)
    print(image.tostring())

if __name__ == '__main__':
    main()