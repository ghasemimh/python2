class vehicle:
    max_speed = None
    def __init__(self , speed , doors):
        self.max_speed = speed
        self.door = doors

    def check_guarantee(self , g_time):
        self.guarantee_time = g_time
        if self.guarantee_time > 3:
            print("Not OK")

        elif self.guarantee_time <= 3:
            print("OK")

        else:
            print("valu Error :(")
        
        

car = vehicle(int(input("Enter max speed: ")))
print(car.max_speed)
reason = input("Enter your reason 'repair': ")
if reason == "repair":
    car.check_guarantee(int(input("Enter yout guarantee time: ")))
