file = open("data.txt" , "a")


while True:
    f_name = input("Enter your firs name: ")
    if f_name == "end":
        break
    l_name = input("Enter your last name: ")
    dad_name = input("Enter your father's name: ")
    file.write(f_name)
    file.write(l_name)
    file.write(dad_name)
    
    
file.close()
