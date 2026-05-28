#Caroline Friesen
#Hacker
#Program will achieve all goals

import pandas as pd
data=pd.read_csv('hacker.csv')
#print(data)

filter=[]
des=data['Description'].tolist()
dataaa=data['Data_KB'].tolist()



def find_acc(word):
    for i in range (len(des)):
        if word in des[i]:
            filter.append([i])
    print(filter)
    filter.clear()
#print(data.loc[193:195])

#find_acc("Failed")


def find_data():
    for i in range (len(des)):
        if dataaa[i]>3000:
            filter.append([i])
    print(filter)
    filter.clear()
#print(data.loc[199])

#find_data()


def find_force(word):
    for i in range (len(des)):
        if word in des[i]:
            filter.append([i])
    print(filter)
    x=len(filter)
    print(f"The amount of people who had to rest was {x}")
    filter.clear()

find_force("Force")
