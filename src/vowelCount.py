#counts the vowels in a sentence
def get_count(sentence):
    #initializes vowels to zero
    vowels = 0
    #loops over the characters of the sentence
    for i in sentence:
        #checks if there are vowels only in the lowercase, excluding 'y'
       if(i in "aeiou"):
           vowels+=1
    #returns the vowels after the loop is over
    return vowels