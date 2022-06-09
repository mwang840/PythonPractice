def to_camel_case(text):
    #Checks if text length is zero
    if(len(text) == 0):
        return 
    #Check to see if there are are - or _ shown then subsitute those out, then adds to the text
    #Also looks at the title
    #Joins the first char by uppercasing
    together = ''.join(text[0].upper())
    for i in range(1, len(text)):
        if(text[i] == ' '):
            together = together[i+1].upper()
            i+=1
        elif(text[i - 1] != ' '):
            together+=together[i]
    #Lowercases first letter of word and no spaces then joins the rest of the letters
    return together