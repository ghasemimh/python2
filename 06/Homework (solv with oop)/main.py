class person():
    f_name = None
    l_name = None
    age = 0
    m_gread = None
    ph_gread = None
    ch_gread = None
    file = open("result.txt" , "w")
    file.close()
    
    def set_f_name():
        f_name = input("Enter your first name: ")
        
    def set_l_name():
        l_name = input("Enter yorur last nem: ")
        
    def set_age():
        age = input("Enter your age: ")
        
        while True:
            try:
                age = int(age)
                break
            
            except:
                age = input("Enter your age again: ")
                
                
    def set_greads():
        m_gread = input("Enter your Math gread: ")
        ph_gread = input("Enter your Physics gread: ")
        ch_gread = input("Ente your Chemistry gread: ")
        
        while True:
            try:
                m_gread = float(m_gread)
                ph_gread = float(ph_gread)
                ch_gread = float(ch_gread)
                break
            except:
                m_gread = input("Enter your Math gread again: ")
                ph_gread = input("Enter your Physics gread again: ")
                ch_gread = input("Ente your Chemistry gread again: ")
                
    file = open("result.txt" , "a")
    karnameh = {"First name": f_name , "Last name": l_name , "Age": age , "Gread": {"Math gread": m_gread , "Physics gread": ph_gread , "Chemistry gread": ch_gread}}
    for i in karnameh:
        print(karnameh[i])
