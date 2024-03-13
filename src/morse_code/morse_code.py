
morse_map = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
             "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
             ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",
             ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
             "----.": "9", "-----": "0"
             }


def morse_code(string):
    def morse_code(string):
    if "    " not in string:
        split_string = string.split(" ")
        return "".join(morse_map[code] for code in split_string)
    else:
        decoded_words = []
        split_string_words = string.split("    ")
        for word in split_string_words:
            decoded_word = "".join(morse_map[code] for code in word.split(" "))
            decoded_words.append(decoded_word)
        return '' ''.join(decoded_words)
