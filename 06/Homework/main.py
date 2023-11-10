file = open("result.txt" , "w")
file.close()
def karnameh():
    f_name = input("\nEnter your first name: ")
    l_name = input("\nEnter your last name: ")
    age = input("\nEnter your age: ")
    m_gread = input("\nEnter your Math gread: ")
    ph_gread = input("\nEnter your Physics gread: ")
    ch_gread = input("\nEnter your Chemistry gread: ")
    
    
    while True:
        try:
            age = int(age)
            break

        except:
            age = input("Enter your age again: ")
            
            
    while True:
        try:
            m_gread = float(m_gread)
            break
        
        except:
            m_gread = input("Enter your Math gread again: ")
            
            
    while True:
        try:
            ph_gread = float(ph_gread)
            break
        
        except:
            ph_gread = input("Enter your Physics gread again: ")
            
    while True:
        try:
            ch_gread = float(ch_gread)
            break
        
        except:
            ch_gread = input("Enter your Chemistry gread again: ")
            
            
            
    person = {"First name": f_name , "Last name": l_name , "Age": age , "Gread": {"Math gread": m_gread , "Physics gread": ph_gread , "Chemistry gread": ch_gread}}
    return person



#I want to write oop project