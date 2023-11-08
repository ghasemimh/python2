def factorial(num):
    try:
        num = int(num)
        j=1
        if num > 0:
            for i in range(1, num+1):
                j*=i

            return j
        
    except:
        return "The value is incorrect"