name = input("Enter your name: ")
last_name = input("Enter your last name: ")
father_name = input("Enter your father name: ")
num_gread = int(input("Enter your gread number: "))
gread = []
avg = 0
for i in range(1, num_gread+1):
    gread2 = int(input("Enter your gread: "))
    gread.append(gread2)
    avg += gread2
    
avg /= num_gread
karnameh = {"f_name": name , "l_name": last_name , "fahter_name": father_name , "gread": gread , "avg": avg}
print(karnameh)
