def filter_list(l):
    numbers = []
    for li in l:
        if(type(li) == int):
            numbers.append(li)
    
    return numbers