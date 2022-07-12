def move_zeros(lis):
    endZeros = []
    nonZeros = []
    for li in range(len(lis)):
        if lis[li] == 0:
            endZeros.append(lis[li])
        else:
            nonZeros.append(lis[li])               

    for end in endZeros:
        nonZeros.append(endZeros[end])
        

    return nonZeros

def main():
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
    print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
    print(move_zeros([0,0]))
    print(move_zeros([]))
    return    

if __name__ == "__main__":
    main()        