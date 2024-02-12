"""
---------------------
|| MorseWave V1.0  ||
---------------------

by Tomás Illuminati

DEVELOPED IN PYTHON 3.11.0 64-bit
ENCODING: UTF-8
DATE: AUG 12 2023

MorseWave is a Python module that allows you to convert text to Morse code and vice versa. It provides a simple interface for converting between text and Morse code representations.

Usage:
- Import the module as "mw" by using the following command:
  Example: import morseconverter as mw

- Create a variable to hold the result of the conversion.

- Use the function mw.morse_converter(input_string, output_type) to perform the conversion.
  Example: result = mw.morse_converter(input_string, output_type)

  - input_string (str): The input string to be converted, which can be in Morse code or text format.
  - output_type (str): The desired output type as a string: 'Morse' or 'Txt' (case insensitive).

- Print the variable to view the converted result.

Example:
input_string = "Hello, World!"
output_type = "Morse"
result = mw.morse_converter(input_string, output_type)
print(result)  # Output: ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"

Note:
- This module includes functions for converting text to Morse code and Morse code to text.
- The Morse code dictionary includes letters, numbers, and common punctuation symbols.
- The output_type parameter determines whether the conversion result is in Morse code or text.
- Invalid output_type values will result in an "Error, Invalid Output Type" message.

"""

#HELP FUNCTION
def help():
    print("\n.......................................................................................")
    print("\n")
    print("           --------------------")
    print("           || MorseWave V1.0 ||")
    print("           --------------------")
    print("\n")
    print("-- To use we recommend importing the module as \"mw\"\n\n        Example: import morsewave as mw\n\n-- Create a variable\n\n-- Put the function mw.morse_converter( input_string, output_type ) in the variable\n\n       Example : var = mw.morse_converter(input_string, output type)\n\n-- [ input_String ] = Place the string here either in morse or in txt to convert\n-- [ output_type ]  = Put as string the type of output you want to get: Morse or Txt\n\n-- Print the variable")
    print("\n........................................................................................")


#MAIN FUNCTION ( INPUT , EXPECTED OUTPUT )
def morse_converter(input_string, output_type):

    #TEXT TO MORSE CONVERTER FUNCTION ( TEXT INPUT )
    def txt_morse_conver(input_string):
        
        #DICTIONARY OF SYMBOLS
        full_dict = {

                #ALPHABET
                "A":".-", 
                "a":".-",
                "B":"-...",
                "b":"-...",
                "C":"-.-.",
                "c":"-.-.",
                "D":"-..",
                "d":"-..",
                "E":".",
                "e":".",
                "F":"..-.",
                "f":"..-.",
                "G":"--.",
                "g":"--.",
                "H":"....",
                "h":"....",
                "I":"..",
                "i":"..",
                "J":".---",
                "j":".---",
                "K":"-.-",
                "k":"-.-",
                "L":".-..",
                "l":".-..",
                "M":"--",
                "m":"--",
                "N":"-.",
                "n":"-.",
                "O":"---",
                "o":"---",
                "P":".--.",
                "p":".--.",
                "Q":"--.-",
                "q":"--.-",
                "R":".-.",
                "r":".-.",
                "S":"...",
                "s":"...",
                "T":"-",
                "t":"-",
                "U":"..-",
                "u": "..-",
                "V":"...-",
                "v":"...-",
                "W":".--",
                "w":".--",
                "X":"-..-",
                "x":"-..-",
                "Y":"-.--",
                "y":"-.--",
                "Z":"--..",
                "z":"--..",

                #NUMBERS
                "0":"-----",
                "1":".----",
                "2":"..---",
                "3":"...--",
                "4":"....-",
                "5":".....",
                "6":"-....",
                "7":"--...",
                "8":"---..",
                "9":"----.",

                #SIGNS
                ".":".-.-.-",
                ",":"--..--",
                "?":"..--..",
                "¿":"..-.-",
                "!":"-.-.--",
                "¡":"--...-",
                "-":"-....-",
                "+":".-.-.",
                "=":"-...-",
                "/":"-..-.",
                ":":"---...",
                ";":"-.-.-.",
                "(":"-.--.-",
                ")":"-.--.-",
                "$":"...-..-",
                "&":".-...",
                "@":".--.-.",
                "\"":".-..-.",

                #SPACE
                " ":"/",
                }

        #CHOPING THE STRING INTO WORDS THAT MAKE IT UP
        input_string = list(input_string)

        #MAIN LIST STATEMENT
        main_array = []


        for word in range(0, len(input_string)):
            main_array = main_array + list(input_string[word])

        #VARIABLE TEXT STATEMENT
        text = ""

        #FOR LOOP WHICH CONVERTS EACH CHARACTER TO THE EQUIVALENT IN THE DICTIONARY, THEN REMOVES LEFT SPACES AND CHANGES IT TO UPPERCASE
        for i in range (0, len(main_array)):
            if main_array[i] in full_dict:
                text = text + " "+ full_dict[main_array[i]]
            text = text.lstrip()
            text = text.upper()
        return text

    #MORSE TO TEXT CONVERTER FUNCTION ( TEXT INPUT )
    def morse_txt_conver(input_string):

        #DICTIONARY OF SYMBOLS
        full_dict = {

                #ALPHABET
                ".-":"A", 
                ".-":"a",
                "-...":"B",
                "-...":"b",
                "-.-.":"C",
                "-.-.":"c",
                "-..":"D",
                "-..":"d",
                ".":"E",
                ".":"e",
                "..-.":"F",
                "..-.":"f",
                "--.":"G",
                "--.":"g",
                "....":"H",
                "....":"h",
                "..":"I",
                "..":"i",
                ".---":"J",
                ".---":"j",
                "-.-":"K",
                "-.-":"k",
                ".-..":"L",
                ".-..":"l",
                "--":"M",
                "--":"m",
                "-.":"N",
                "-.":"n",
                "---":"O",
                "---":"o",
                ".--.":"P",
                ".--.":"p",
                "--.-":"Q",
                "--.-":"q",
                ".-.":"R",
                ".-.":"r",
                "...":"S",
                "...":"s",
                "-":"T",
                "-":"t",
                "..-":"U",
                "..-":"u",
                "...-":"V",
                "...-":"v",
                ".--":"W",
                ".--":"w",
                "-..-":"X",
                "-..-":"x",
                "-.--":"Y",
                "-.--":"y",
                "--..":"Z",
                "--..":"z",

                #NUMBERS
                "-----":"0",
                ".----":"1",
                "..---":"2",
                "...--":"3",
                "....-":"4",
                ".....":"5",
                "-....":"6",
                "--...":"7",
                "---..":"8",
                "----.":"9",

                #SIGNS
                ".-.-.-":".",
                "--..--":",",
                "..--..":"?",
                "..-.-":"¿",
                "-.-.--":"!",
                "--...-":"¡",
                "-....-":"-",
                ".-.-.":"+",
                "-...-":"=",
                "-..-.":"/",
                "---...":":",
                "-.-.-.":";",
                "-.--.":"(",
                "-.--.-":")",
                "...-..-":"$",
                ".-...":"&",
                ".--.-.":"@",
                ".-..-.":"\"",

                #SPACE
                "/":" ",
                }

        #CORRECTION OF "/" FOR " / " IN CASE THE USER FORGETS TO PLACE A SPACE BETWEEN THE SIGN
        dash_edition = input_string.replace("/"," / ")

        #MAIN LIST STATEMENT
        main_array = []

        #ASSIGNMENT OF THE MODIFIED STRING TO THE MAIN LIST, AND DIVIDED CHARACTER BY FACE
        main_array = dash_edition.split()

        #VARIABLE TEXT STATEMENT
        text = ""

        #FOR LOOP WHICH CONVERTS EACH CHARACTER TO THE EQUIVALENT IN THE DICTIONARY, THEN REMOVES LEFT SPACES AND CHANGES IT TO UPPERCASE
        for i in range (0, len(main_array)):
            if main_array[i] in full_dict:
                text = text + full_dict[main_array[i]]
            text = text.lstrip()
            text = text.upper()
        return text

    #DECLARATION OF THE CONTAINER VARIABLE OF THE FINAL STRING
    result = ""

    #PARAMETER CORRECTOR ( output_type ), REMOVING SPACES AND RETURNING EVERYTHING TO LOWERCASE
    output_type = output_type.strip()
    output_type = output_type.lower()


    #CONDITIONAL DETECTOR OF THE EXPECTED OUTPUT & OUTPUT IN WRONG CASE
    if output_type == "morse":
        result = txt_morse_conver(input_string)
    elif output_type == "txt":
        result = morse_txt_conver(input_string)
    else:
       result = "Error, Invalid Output Type"

    #FUNCTION FINAL RETURN
    return result

