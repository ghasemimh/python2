Ghasemi = [1,2,3,4,5,6,7,8,9,10]
Ghasemi.append(input("Enter input 1: "))
Ghasemi.append(input("Enter input 2: "))
Ghasemi.append(input("Enter input 3: "))
Ghasemi.append(input("Enter input 4: "))

edit_index = int(input("Enter a number for edit array: "))
edit_value = input("Enter a value for edit array: ")

Ghasemi[edit_index] = edit_value
pop_index = int(input("Enter a number for pop index array: "))
if pop_index <= len(Ghasemi):
    Ghasemi.pop(pop_index)
    print("pop sucsesfuly")
    print(Ghasemi)

else:
    print("Error! your input is greather than array index! :(")
