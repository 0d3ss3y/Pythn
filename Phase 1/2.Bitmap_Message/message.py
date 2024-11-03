from bitmap import BitMap

def main():
    heading()
    text = get_input()

    if text.isdigit():
        run_image1(int(text))
    else:
        run_image2(text)

def heading():
    print("Bitmap Message")

def get_input():
    while True:
        print("Enter a text or number to create a bitmap message")
        ans = input("> ").strip()
        if ans:  # Check if input is not empty
            return ans
        else:
            print("Input cannot be empty. Please try again.")

def run_image1(number):
    try:
        image = BitMap(number)
        print(image.tostring())
        image.set(1)
        print(image.tostring())
    except Exception as e:
        print(f"Error creating bitmap with number: {e}")

def run_image2(text):
    try:
        image = BitMap.fromstring(text)
        print(image.tostring())
        image.flip(1)
        print(image.tostring())
    except Exception as e:
        print(f"Error creating bitmap from text: {e}")

if __name__ == '__main__':
    main()
