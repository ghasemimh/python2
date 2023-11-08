def factorial(fa):
    rse = 1    
    try:    
        fa = int(fa)
        while True :
            if fa >= 1 :
                break
            else :
                print('Input value is incorrect! (Enter natural number)')

        for number in range(1, fa + 1):
            rse *= number

        print(rse)
    except :
        print('Plese type number again !!? ')