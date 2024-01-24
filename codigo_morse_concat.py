letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",", "?", "\'", "/", ":", ";", "+", "-", "=", " "]
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.","--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ".-.-.-", "---..--", "..--..", ".----.", "-..-.", "---...", "-.-.-.", ".-.-.", "-....-", "-...-", "/"]

input_letters = input("Inserta el texto que desea traducir a codigo morse\n").lower()
output_morse = ""

for i in input_letters:
    try:
        output_morse += morse[letters.index(i)] + " "
    except:
        print("Este texto no se puede traducir a código morse")
        quit()
print(output_morse)