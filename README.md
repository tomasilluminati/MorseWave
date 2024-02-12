
# MorseWave V1.0

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

MorseWave is a Python module that enables users to convert text to Morse code and vice versa. It offers a straightforward interface for converting between text and Morse code representations.

### Features

- Convert text to Morse code.
- Convert Morse code to text.
- Supports letters, numbers, and common punctuation symbols.
- Flexible output options: Morse code or text.

## Installation

1. Clone this repository to your local machine.

2. Import the module into your Python script:

```python
import morsewave as mw
```

3. Start using the functions provided by the module.

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

