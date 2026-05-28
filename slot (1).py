#Caroline Friesen and Josie Check
#Slot Machine
#Will play a game of slots and put out
#Init
def game():
    import random
    outcomes= ["7", "♡", "♠", "♢"]
    b=0
    while True:
        i=int(input("How much would you like to deposit?(50/100/500/0): "))
        if i==500:
            print(f"Your balance is {b+500}")
            b=b+500
        elif i==50:
            print(f"Your balance is {b+50}")
            b=b+50
        elif i==100:
            print(f"Your balance is {b+100}")
            b=b+100
        elif i==0:
            print(f"Your balance didn't change, it is {b}")
        else:
            print("That is not a valid input...")
            break

        spining=input("Do you want to spin?Its cost is 10(yes/no): ")
        if spining=="yes" and b>=10:
            b= b-10
            print(f"Your balance is now {b}")
        elif spining=="yes" and b<10:
            print("INSUFFICIENT FUNDS, NEED TO INSERT CREDIT")
            break
        elif spining=="no":
            break

        item1=random.choice(outcomes)
        print(item1)

        item2=random.choice(outcomes)
        print(item2)

        item3=random.choice(outcomes)
        print(item3)

        if item1==7 and item2==7 and item3==7:
            print("You win the jackpot!!!!")
            b=b+500
            print(f"You get 500 credits, your balance is {b}!")
        elif item1 =="♡" and item2 == "♡" and item3 == "♡":
            print("You Win!!")
            b=b+100
            print(f"You get 100 credits, your balance is {b}!")
        elif item1 =="♠" and item2 == "♠" and item3 == "♠":
            print("You Win!!")
            b=b+100
            print(f"You get 100 credits, your balance is {b}!")
        elif item1 =="♢" and item2 == "♢" and item3 == "♢":
            print("You Win!!")
            b=b+100
            print(f"You get 100 credits, your balance is {b}!")
        else:
            print("Im sorry, you loose!")

        choice=input("Do you want to contine playing(if not you will cash out)?(yes/no): ")
        if choice=="yes":
            continue
        else:
            break


#Simulation
def simulation():
    import random
    outcomes= ["7", "♡", "♠", "♢"]
    weights=[5,45,35,15]
    b=0
    c=0
    i=int(input("How much would you like to deposit?(50000/10000/0): "))
    b=i
    print(f"Your starting balance is {b}")
    for i in range(1000):
            if b>=10:
                b=b-10
                c=c+10
            elif b<10:
                print("INSUFFICIENT FUNDS, NEED TO INSERT CREDIT")
                break
            item1=random.choices(outcomes,weights,k=1)

            item2=random.choices(outcomes,weights,k=1)

            item3=random.choices(outcomes,weights,k=1)

            if item1==[7] and item2==[7] and item3==[7]:
                b=b+500
                c=c-500
            elif item1 ==["♡"]and item2 == ["♡"] and item3 == ["♡"]:
                b=b+50
                c=c-50
            elif item1 ==["♠"] and item2 == ["♠"] and item3 == ["♠"]:
                b=b+50
                c=c-50
            elif item1 ==["♢"] and item2 == ["♢"] and item3 == ["♢"]:
                b=b+50
                c=c-50
            else:
                b=b+0
    print(f"Your final balance is {b}. The casino balance is {c}. Thank you for playing!")

#Main

simulation()
