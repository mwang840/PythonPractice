def parse(data):
    parsed = []
    score = 0
    for d in data:
        if d == "i":
            score += 1
        elif d == 'd':
            score -= 1
        elif d == 's':
            score *= score    
        elif d == 'o':
            parsed.append(score)        
        
    return parsed

def main():
    parsing = "isoisoiso"
    print(parse(parsing))

if __name__ == "__main__":
    main()        