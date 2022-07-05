# MorseCode

MorseCode_Dict = {"0": "-----",
                  "1": ".----",
                  "2": "..---",
                  "3": "...--",
                  "4": "....-",
                  "5": ".....",
                  "6": "-....",
                  "7": "--...",
                  "8": "---..",
                  "9": "----.",
                  "a": ".-",
                  "b": "-...",
                  "c": "-.-.",
                  "d": "-..",
                  "e": ".",
                  "f": "..-.",
                  "g": "--.",
                  "h": "....",
                  "i": "..",
                  "j": ".---",
                  "k": "-.-",
                  "l": ".-..",
                  "m": "--",
                  "n": "-.",
                  "o": "---",
                  "p": ".--.",
                  "q": "--.-",
                  "r": ".-.",
                  "s": "...",
                  "t": "-",
                  "u": "..-",
                  "v": "...-",
                  "w": ".--",
                  "x": "-..-",
                  "y": "-.--",
                  "z": "--..",
                  ".": ".-.-.-",
                  ",": "--..--",
                  "?": "..--..",
                  "!": "-.-.--",
                  "-": "-....-",
                  "/": "-..-.",
                  "@": ".--.-.",
                  "(": "-.--.",
                  ")": "-.--.-"
                  }


# Convert to Morse Code

def to_morse(word):
    message = ""
    for letter in word:
        if letter == "":
            message += ""
        else:
            message += MorseCode_Dict[letter.lower()]
    return message


string = input("Enter the word you would like to encrypt: ")
encrypted_string = to_morse(string)
print(encrypted_string)
