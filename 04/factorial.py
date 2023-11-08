def factorial(num):
    if int(num):
        j = 1
        for i in range(1, num+1):
            j*=i
            
        return j
        
    
    else:
        return "The input is not correct! :("