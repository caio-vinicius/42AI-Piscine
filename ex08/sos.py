import sys

morse = {
	"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
	"f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
	"k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
	"p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
	"u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
	"z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
	"4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
	"9": "----.", ".": ".-.-.-", ",": "--.--", "?": "..--..", "'": ".----.",
	"!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
	":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
	"_": "..--.-", "\"": ".-..-.", "$": "...-.-", "@": ".--.-.", " ": " "
}

text = sys.argv[1]
ntext = ""

try:
	for c1 in text.lower():
		for c2, m in morse.items():
			if c1 == c2:
				ntext += m
	print (ntext)
except:
	print ("ERROR")
		
