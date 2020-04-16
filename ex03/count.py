import string

def text_analyzer(text = ""):
    '''This function give to you a analyze of a text. After run it, you can get count of total, uppercase and lowercase letters, punctuation and spaces.'''
    
    uppercase = 0
    lowercase = 0
    punctuation = 0
    spaces = 0
    total = 0
    
    if not text:
        text = input("What is the text to analyze?\n")
    
    for c in text:
      total += 1
      if c.isalpha():
          if c.isupper():
              uppercase += 1
          elif c.islower():
              lowercase += 1
      elif c in string.punctuation:
          punctuation += 1
      elif c.isspace():
          spaces += 1

    print ("The text contain", total,"characters:\n", 
            uppercase,"upper letters\n",
            lowercase, "lower letters\n",
            punctuation, "punctuation marks\n",
            spaces, "spaces")

