
# MorseWave V1.0

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11-blue)

![logo](https://github.com/tomasilluminati/InkCode/blob/main/logo/ink_code_logo.png)

## Overview

MorseWave is a Python module that enables users to convert text to Morse code and vice versa. It offers a straightforward interface for converting between text and Morse code representations.

### Features

- Convert text to Morse code.
- Convert Morse code to text.
- Supports letters, numbers, and common punctuation symbols.
- Flexible output options: Morse code or text.

## Installation

Import the module into your Python script:

```bash
import morsewave as mw
```

Or Install with the pip command:

```bash
pip install morsewave
```

## Usage

### Example:

```python
input_string = "Hello, World!"
output_type = "Morse"
result = mw.morse_converter(input_string, output_type)
print(result)  # Output: ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
```

### Functionality:

- **mw.morse_converter(input_string, output_type):**
  - `input_string` (str): The string to be converted, which can be in Morse code or text format.
  - `output_type` (str): The desired output type as a string: 'Morse' or 'Txt' (case insensitive).

## Help Function

For detailed usage instructions, you can use the `help()` function:

```python
mw.help()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

