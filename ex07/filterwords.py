from string import printable
import sys

#if all(c in printable for c in sys.argv[1]):

try:
	nlist = []
	text = sys.argv[1].split()
	length = sys.argv[2]

	for w in text:
		if not len(w) <= int(length):
			nlist.append(w)
	print (nlist)
except:
	print ("ERROR")


