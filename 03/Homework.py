person_info = {}
person_info["first_name"] = input("Enter your first name: ")
person_info["last_name"] = input("\nEnter your last name: ")
person_info["father's_name"] = input("\nEnter your father's name: ")
person_info["national_code"] = int(input("\nEnter your national code: "))
person_info["birth_date"] = input("\nEnter your birth date: ")

for i , j in person_info.items():
    print()
    print(i , j)
    
    
while True:
    key = input("\nEnter a key for print Value (for the end while Enter 'end'): ")
    if key == "end":
        break
    
    elif key in person_info:
        print("\n" , person_info[key] , sep=""
              )
        
    else:
        print("\nThe key input is not find! :(")
        
print("The end")