def is_prime(num):
    prime = True
    if(num <= 1):
        return False 
    elif(num > 1):    
        for n in range(2, int(num/2)+1):
            if(num % n == 0):
                prime =False
                break
            else:
                prime = True
                break
    else:
        prime = False        
    return prime    
