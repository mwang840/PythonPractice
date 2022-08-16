def funWithAnagrams(text):
    funAnagram = []
    flag = True

    for t in text:
        if len(funAnagram) == 0:
            funAnagram.append(t)

        for f in funAnagram:
            if(len(t) == len(f) and sorted(list(t)) == sorted(list(f))):
                flag = False
                break
        

        if (flag):
            funAnagram.append(t)    
    
        flag = True
    return funAnagram

def main():
    anagram = ["code", "anagrams", "doce", "aaagmrns"]
    anagram1 = ["cap", "lax", "xal", "pac"]
    funWithAnagrams(anagram)
    funWithAnagrams(anagram1)


if __name__ == "__main__":
    main()   