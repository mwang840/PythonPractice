def divisors(n):
    divided = 1
    iterate = 1
    while iterate <= n/2:
        if n % iterate == 0:
            divided+=1
        iterate+=1    
    return divided