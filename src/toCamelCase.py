from operator import sub


def to_camel_case(text):
    #Check to see if there are are - or _ shown then subsitute those out, then adds to the text
    #Also looks at the title
    together = sub(r"(_|-)+", " " , text).title().replace(" ", "")
    #Lowercases first letter of word and no spaces then joins the rest of the letters
    return ''.join([together[0].lower(), together[1:]])