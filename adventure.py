#Caroline Friesen
#Nesting practice
#Will take input from user and send them to a Hawaiian island

print("Get excited for your trip to Hawaii, time to start planning!")
def island_rec():
    popularity=input("Do you want to go to a popular or a niche island?: ")
    if popularity=="popular":
        activity=input("Do you want to hike or swim?: ")
        if activity=="hike":
            print("You should go to O'ahu!")
        elif activity=="swim":
            print("You should go to Maui!")
    elif popularity=="niche":
        activity=input("Do you want to hike or swim?: ")
        if activity=="hike":
            print("You should go to the big island(Local)!")
        elif activity=="swim":
            print("You should go to Kauai!")

island_rec()





