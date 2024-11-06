# Caesar Cipher Brute-Force Hacker

This program is designed to **hack messages encrypted with the Caesar Cipher** (a substitution cipher used in Project 6). Using a brute-force attack, it can decrypt messages without needing the encryption key. Because the Caesar Cipher has only 26 possible keys, this program can quickly try all possible decryptions and display the results.

## How It Works

The brute-force attack technique systematically tries each possible key, shifting the letters back by the key amount and displaying the result. With only 26 possible shifts in the Caesar Cipher, this approach is efficient and effective.

### Example

Suppose we have the encrypted message `"KHOOR"`, which was encoded using the Caesar Cipher with an unknown key:

1. The program will attempt each key from 1 to 26.
2. When it finds the correct key, the program will display the decrypted message.

For example, with the message `"KHOOR"`, when the key is `3`, the decryption reveals `"HELLO"`.

## Features

- **Brute-Force Decryption**: Attempts each of the 26 possible Caesar Cipher keys.
- **Automatic Key Detection**: Reveals the most plausible decrypted message based on readable output.
- **Quick and Efficient**: Tries all possible keys in a matter of seconds.

## Requirements

- Python 3.x or later.

## Usage

1. **Run the Program**: Start the Caesar Cipher brute-force hacker program.
2. **Input the Encrypted Message**: Enter the message you want to decrypt.
3. **View Possible Decryptions**: The program will display all possible decrypted messages.
4. **Identify the Correct Message**: Read through the outputs to find the correct decrypted message.

## Getting Started

1. Clone or download the project files.
2. Run `hacker.py` to start the program.
3. Follow the on-screen instructions to decrypt Caesar Cipher-encrypted messages.

---

This brute-force Caesar Cipher hacker is a simple yet powerful tool to demonstrate basic cryptographic decryption methods and brute-force techniques.
