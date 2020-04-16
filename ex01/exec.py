import sys

print ("Ola", str(sys.argv[0]))

str1 = ' '.join(sys.argv)
str1 = str1[8:]
str2 = ''

for c in str1:
    if c.isupper():
        str2 += c.lower()
    elif c.islower():
        str2 += c.upper()
    else: 
        str2 += c

print (str2[len(str2)::-1])
