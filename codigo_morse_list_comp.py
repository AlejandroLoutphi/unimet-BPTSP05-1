def list_translate(item, input_list: list, output_list: list):
    return output_list[input_list.index(item)]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",", "?", "\'", "/", ":", ";", "+", "-", "=", " "]
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.","--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", ".-.-.-", "---..--", "..--..", ".----.", "-..-.", "---...", "-.-.-.", ".-.-.", "-....-", "-...-", "/"]

x = input("Inserta el texto que desea traducir a codigo morse\n")
x = x.lower()
try:
    x = [list_translate(i, letters, morse) for i in x]
except:
    print("Este texto no se puede traducir a código morse")
    quit()
x = ' '.join(x)
print(x)