#US National Parks
#Program will take input on users preferences and recommend a great trip suggestion

#Init
#Importing all external applications needed for the functions
import random
import webbrowser
import pandas as pd
data=pd.read_csv('park.csv')

#Assigning variables to columns in the dataset to create arrays
name=data["Name"].tolist()
loco=data["Location"].tolist()
pic=data["Image"].tolist()
date=data["Date established"].tolist()
area=data["Area in acres"].tolist()
visitors=data["Recreation visitors in 2019"].tolist()
desc=data["Description"].tolist()

filter=[]
#Additional arrays that sort the parks based on U.S. regions
mountwfilter=["Arches", "Black Canyon", "Bryce Canyon", "Canyonlands","Capitol Reef", "Carlsbad Caverns", "Glacier", "Grand Canyon", "Grand Teton", "Great Basin", "Great Sand Dunes", "Mesa Verde", "Petrified Forest", "Rocky Mountains", "Saguaro", "White Sands", "Yellowstone", "Zion"]
pwfilter=["Channel Island", "Crater Lake", "Death Valley", "Denali", "Gates of the Arctic", "Glacier Bay", "Haleakala", "Hawaii Volcanoes", "Joshua Tree", "Katmai", "Kenai Fjords", "Kings Canyon", "Kobuk Valley", "Lake Clark", "Lassen Volcanic", "Mount Rainer", "North Cascades", "Olympic", "Pinnacles", "Redwood", "Seqoia", "Wrangell-St. Elias", "Yosemitie"]
sandnfilter=["American Samoa", "Big Bend", "Biscayne", "Congaree", "Dry Tortugas", "Everglades", "Great Smoky Mountains", "Guadalpue Mountians", "Hot Springs", "Mammoth Cave", "Shenandoah", "Virgin Islands", "Acadia"]
mwfilter=["Badlands", "Cuyahoga Valley", "Gateway Arch", "Indiana Dunes", "Isle Royale", "Theodore Roosevelt", "Voyageurs", "Wind Cave"]

#Functions
def findparkregion(region): #Function assigns argument based on user's input of preferred geographical region
    if region=="mountainwest": #If statements sort through user inputs to match with data in the arrays
        random_park=random.choice(mountwfilter)
        print(f"A park that is suggested for you in the mountain west is {random_park}! We hope this is a great option for you.") #Program selects random park within the designated array by assigning the random function to a variable
    elif region=="pacificwest":
        random_park=random.choice(pwfilter)
        print(f"A park that is suggested for you in the pacific west is {random_park}! We hope this is a great option for you.")
    elif region=="south":
        random_park=random.choice(sandnfilter)
        print(f"A park that is suggested for you in the south is {random_park}! We hope this is a great option for you.")
    elif region=="midwest":
        random_park=random.choice(mwfilter)
        print(f"A park that is suggested for you in the midwest is {random_park}! We hope this is a great option for you.")
    else:
        print("That is not a regional option.")


def find_info(park_name): #Function asks for users to input a specific park to give an overview of the park, including its geographic location, general description, and image of the park
    for i in range (len(area)): #Loops through each park in the data set to check whether it meets the if statement requirements
        if park_name==name[i]:
            filter.append(name[i])#Adds the user's inputted park name into the empty filter
            print(filter)
            print(f"{park_name} is in {loco[i]}, and here is a brief overview: {desc[i]} Here is an image!")
            webbrowser.open(pic[i])#Opens the image of the inputted park
    if filter==[]:
        print("This park doesn't exist...Check spelling.")#Creates an output for when the input does not match any data to inform user of an error
    filter.clear()

def find_purp(feature):#Function uses user input to search for parks that match a desired feature or element
    for i in range (len(name)):#Loops through each park in the dataset
        if feature in desc[i]:#Program looks for specific word with each park's description to check whether it meets the if statement requirements
            filter.append(name[i])#Adds the park names that match contain the input word into an empty filter
    if filter==[]:
        print("No park that matches this feature or attraction was found...")#Creates an output for when the input does not match any data to inform user of an error
    else:
        print(f"The parks(s) that match for given feature/attraction of {feature} is {filter}. We hope the park selection(s) work well for you!")

    filter.clear()

def big_Busy(size, popularity):#Function sorts parks into categories based on their acre size and number of yearly visitors
    if size == "small" and popularity == "less visited":#If statements groups the parks into sections based on all potential user input combinations
        for i in range (len(name)):#Loops through each park in the dataset
            if area[i]<=50000 and visitors[i]<500000: #Inequalities reference numbers in the dataset to sort their size and popularity to check whether it meets the statement requirements
                filter.append(name[i])#Adds the park names that match contain the input word into an empty filter
    #if filter==[]:
        if filter==[]:
            print("No park was found...")#Creates an output when the input does not match any data to inform user of an error
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "small" and popularity == "average":#Program runs through all input combination options with if statements before outputting results
        for i in range (len(name)):
            if area[i]<=50000 and visitors[i]<2000000 and visitors[i]>500000:
                filter.append(name[i])
                print(filter)
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "small" and popularity == "popular":
        for i in range (len(name)):
            if area[i]<=50000 and visitors[i]>1000000 and visitors[i]>500000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "medium" and popularity == "less visited":
        for i in range (len(name)):
            if 150000>=area[i]>=50000 and visitors[i]<500000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "medium" and popularity == "average":
        for i in range (len(name)):
            if 150000>=area[i]>=50000 and visitors[i]<2000000 and visitors[i]>500000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "medium" and popularity == "popular":
        for i in range (len(name)):
            if 150000>=area[i]>=50000 and visitors[i]>2000000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "large" and popularity == "less visited":
        for i in range (len(name)):
            if 150000<=area[i] and visitors[i]<500000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}.")
            filter.clear()
    elif size == "large" and popularity == "average":
        for i in range (len(name)):
            if 150000<area[i] and visitors[i]<2000000 and visitors[i]>500000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}")
            filter.clear()
    elif size == "large" and popularity == "popular":
        for i in range (len(name)):
            if 150000<=area[i] and visitors[i]>2000000:
                filter.append(name[i])
        if filter==[]:
            print("No park was found...")
        else:
            random_pick=random.choice(filter)
            print(f"The park best for you in the {size} and {popularity} category is {random_pick}")
            filter.clear()


#Main menu
print("Welcome to the center for U.S. National Parks! We hope you're ready to branch out on some tree-mendous adventures...")
while True:
    decide=input("We have a lot you can do on our site. Would you like to find a park in your region, get info on a specific park, look for parks based on a specific feature, or search for parks based on size/popularity?(region/info/feature/size): ")
    if decide=="region" or decide=="Region":
        place=input("Our park finder for regions is top tier! Which region would you like to find a park in?(midwest/south/pacificwest/mountainwest): ")
        findparkregion(place)
        cont=input("Would you like to continue in our center and start over?(yes/no): ")
        if cont=="yes" or cont=="Yes":
            continue
        else:
            break
    elif decide=="info" or decide=="Info":
        pick=input("Leaf it to us to help you search for info on a specific National Park. Some examples would be Grand Teton or Zion: ")
        find_info(pick)
        cont=input("Would you like to continue in our center and start over?(yes/no): ")
        if cont=="yes" or cont=="Yes":
            continue
        else:
            break
    elif decide=="feature" or decide=="Feature":
        want=input("Great, this will give you the option to find parks that match a certain wanted feature. Recommended features include lake, canyon, river: ")
        find_purp(want)
        cont=input("Would you like to continue in our center and start over?(yes/no): ")
        if cont=="yes" or cont=="Yes":
            continue
        else:
            break
    elif decide=="size" or decide=="Size":
        land=input("This is an awesome finder if you are wanting specific conditions of a park. You can select between small and medium and large for the physical size of the park in acres(small/medium/large): ")
        people=input("The next part to finding a good park based on preferences is choosing if you want a park with less visitors, average visitors, or many visitors(less visited/average/popular): ")
        big_Busy(land, people)
        cont=input("Would you like to continue in our center and start over?(yes/no): ")
        if cont=="yes" or cont=="Yes":
            continue
        else:
            break
    else:
        print("That is not an option we offer. Check spelling and try again.")
        break

#Sources
#U.S. National Parks Dataset
#Website Name: National Park Service
#URL: https://www.nps.gov/aboutus/national-park-system.htm
#Dataset Source: https://docs.google.com/spreadsheets/d/1pPFi8LbDhqLAqAs75ayUh6quoBLTEAH0y5aaQSLV9No/edit?gid=0#gid=0
#All data, images, and other information came from the site above
