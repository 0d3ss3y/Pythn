# Bitmap Message Display Program

This **Bitmap Message Display** program is a beginner-friendly project that uses a bitmap, a simple 2D image, to display a custom message in a unique way. Each pixel in the bitmap has only two possible colors: a filled pixel or an empty one. This program replaces the filled pixels with characters from the user’s message, creating a visual pattern.

## How It Works

The program reads a bitmap represented as a multiline string. In the bitmap:
- **Empty spaces** represent blank areas in the output.
- **Any other character** represents a pixel that will be replaced by characters from the user’s message.

By default, the bitmap resembles a world map, but you can replace it with any pattern or image of your choice.

## Example

### Bitmap Template
Here’s an example of a bitmap template that might be included:

```
    ******    
  **      **  
**          **
**          **
  **      **  
    ******    
```

### User Message

If the user inputs the message “HELLO,” the program will replace each filled character in the bitmap with letters from the message in a repeating sequence, creating an output like:

```
    HELLOHE    
  LOHE  LHEL  
LOH     EHLLOH
LOH     EHLLOH
  LOHE  LHEL  
    HELLOHE    
```

## Features

- **Customizable Message**: Enter any text to see it displayed using the bitmap pattern.
- **Bitmap Customization**: Modify the bitmap to create different shapes and images.
- **Experimentation**: Try different combinations of messages and patterns to create varied designs.

## Usage

1. **Run the Program**: Start the program and enter a message when prompted.
2. **See the Result**: The program will display the message according to the bitmap pattern.

## Requirements

- Python 3.x or later.

## Getting Started

1. Clone or download this repository.
2. Run `message.py` to start the program.