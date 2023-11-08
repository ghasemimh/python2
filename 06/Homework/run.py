from main import karnameh
file = open("result.txt" , "w")
file.close()
file = open("result.txt" , "a")
results = karnameh()
for i in results:
    print(results[i])
    #file.write(results[i])