def good_vs_evil(good, evil):
    newGood = good.split()
    newEvil = evil.split()
    worth = [1, 2, 3, 3, 4, 10]
    unWorth = [1, 2, 3, 3, 5, 10]
    amIgood = 0
    amIEvil = 0

    for w in worth:
        amIgood += worth[w] * int(newGood[w])
        

    for e in evil:
        amIEvil += unWorth[e] * int(newEvil[e])

    if amIgood > amIEvil:
        return "Battle Result: Good eradicates all trace of Evil"
    elif amIEvil > amIgood:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: No victor on this battle field"

def main():
    print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
    return

    
if __name__ == "__main__":
    main()                 