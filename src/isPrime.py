def is_prime(num):
    if num <= 1:
        return False
    index = 2
    for n in range(2, num):
        if num % n == 0:
            return False
    return True    
