# Caesar Cipher Program
The **Caesar Cipher** program is an implementation of the ancient encryption algorithm used by Julius Caesar. This cipher shifts letters in the alphabet by a specific number of places (known as the "key") to encrypt or decrypt messages. The Caesar cipher is a simple yet effective way to secure messages by encoding text in a way that requires the key to interpret.

## How It Works

The Caesar Cipher shifts each letter in the message by a specified number of positions in the alphabet:

- **Encryption**: Moves each letter forward by the key value. For example, with a key of 3:
  - `A` becomes `D`
  - `B` becomes `E`
  - `C` becomes `F`
  - And so on...
  
- **Decryption**: Moves each letter backward by the key value to reveal the original message.

The program allows the user to both encrypt and decrypt messages by choosing a shift key.

## Features

- **Customizable Key**: The user can choose any number for the key to control the amount of shift in the encryption.
- **Encryption and Decryption**: Encrypt a plaintext message or decrypt an encrypted message by shifting letters in the opposite direction.
- **Case Sensitivity**: The cipher maintains case, keeping uppercase and lowercase letters as they are.

## Example

Suppose the message is `HELLO` and the key is `3`:

- **Encryption**: `HELLO` becomes `KHOOR`.
- **Decryption**: `KHOOR` becomes `HELLO`.

## Usage

1. **Run the Program**: Start the program to access the Caesar Cipher tool.
2. **Choose Mode**: Select whether you want to encrypt or decrypt a message.
3. **Enter Key**: Input the shift key (number of positions to shift).
4. **Input Message**: Enter the message to be encrypted or decrypted.
5. **View Result**: The program displays the encrypted or decrypted text.

## Requirements

- Python 3.x or later.

## Getting Started

1. Clone or download the project files.
2. Run `caesar_cipher.py` to start the program.

---

This Caesar Cipher program is a great way to explore basic encryption techniques and understand the fundamentals of cryptography. Experiment with different keys and messages to see the results!
