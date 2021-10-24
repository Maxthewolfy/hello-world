import random
import time
import sys


nomo = bool
start = bool
inp = 0


#Asking user if they want to start a program or not
def Asking():
    global nomo
    global start
    while True:
        yay = input("Yay or Nay?: ")
        if yay == "Yay":
            nomo = False
            start = False
            break
        elif yay == "Nay":
            nomo = True
            start = True
            break
        else:
            time.sleep(1.5)
            print("uhhh.. what was that again?")
            time.sleep(0.5)


#Number Randomizer
#Maxxy is an Easter Egg word, enter through Line 161's input
def Function():
    rando = random.randint(0, 10)
    if rando <= 5:
        print("Result:", rando)
        time.sleep(1.5)
        print("UwU it's ",rando, " better luck next time.")
    elif rando >= 6:
        print("Result:", rando)
        time.sleep(1.5)
        print("OwO it's ",rando, "! can we get an ice cream?")
    if rando == 0 and name == "Maxxy":
        time.sleep(1.5)
        print("Shhhh..")
        time.sleep(1.5)
        print("there there, don't cry now")
        time.sleep(0.5)
        print("Here")
        time.sleep(1)
        print("https://www.models-resource.com/resources/big_icons/23/22613.png")
        time.sleep(5)
        print('a lil something to "cheer" you up~')
        time.sleep(2)
        print("i bet ya gonna luv it ;3")
    elif  rando == 10:
        time.sleep(2)
        print("But wait, there's more!")
        if name == "Maxxy":
            time.sleep(2.5)
            print("https://twitter.com/Max_thewolfy")
            time.sleep(5)
            print("keep it between us, okay?")
            time.sleep(2)
            print("you,",name)
            time.sleep(1)
            print("and")
            time.sleep(1)
            print("me")
        else:
            pass
    else:
        pass

    time.sleep(1)
    print("it took",time.process_time(),"ms to process.")


#Main playing part, calling number randomizer and ask user for a replay
def play():
    while nomo == False:
        print("YAY! let's go!")
        time.sleep(1.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        Function()
        time.sleep(1)
        print("That was fun! wanna go for another round?")
        time.sleep(0.25)
        while True:
            again = input("Yay or Nay? ")
            if again == "Yay":
                break
            elif again == "Nay":
                Notplay()
                break
            else:
                time.sleep(1.5)
                print("uhhh.. what was that again?")
                time.sleep(0.5)
                

#Asking if user want to continue playing or not
def Notplay():
    print("it's okay", name ,"we can play again later :3")
    time.sleep(2)
    print("may be another shot?")
    time.sleep(0.25)
    global nomo
    global again
    while True:
       again = input("Yay or Nay? ")
       if again == "Yay":
           nomo = False
           play()
       elif again == "Nay":
           nomo = True
           break
       else:
           time.sleep(1.5)
           print("uhhh.. what was that again?")
           time.sleep(0.5)


#Closing the program
def Bye():
    print("See ya around", name, ":3")
    if name == "Maxxy":
        time.sleep(1.25)
        print("and don't forget to check me out more often")
        time.sleep(0.5)
        print("and debug me more often")
        time.sleep(1)
        print("kay?")
    else:
        pass
    time.sleep(2.5)
    sys.exit


#Whole Procedure
time.sleep(2)
print("Hewwo! OwO")
time.sleep(1.5)
print("Welcome to The Rando Number Game!")
time.sleep(2.5)
print("where we get to random numbers!")
time.sleep(1.25)
print("from 0 to 10")
time.sleep(1)
print("if we get anything higher than 5")
time.sleep(1.5)
print("WE GET FREE ICE CREAMS!")
time.sleep(2.5)
print("Before we get started!")
time.sleep(2)
while True:
    if inp == -1:
        break
    else:
        pass
    name = input("How should I call you?: ")
    time.sleep(1.5)
#Integers Detection
    try:
        inp = int(name)
    except:
        inp = -1
    if inp > 0:
        print("So...")
        time.sleep(1)
        print("Your name are numbers, huh?")
        while True:
            enter = input("")
            try:
                enter = int(enter)
            except:
                enter = -1
            if enter < 0:
                break
            elif enter == 1:
                print("I see, a fellow robot like me.")
                print("however, no matter who you are")
                print("We can all have fun together :)")
                inp = -1
                break
            elif enter == 0:
                time.sleep(1)
                print("So who are you exactly?")
                time.sleep(0.5)
                break
            elif enter > 1:
                print("Sorry, I don't understand decimal")
    else:
        break
time.sleep(0.7)
print(name,"? That's a wonderful name you have!")
time.sleep(1.5)
if name == 'Maxxy':
    print("wait...")
    time.sleep(1)
    print("You sound familiar....")
    time.sleep(3)
    print("anyway")
    time.sleep(0.5)
else:
    time.sleep(0.5)
print("nice to meet you", name)
time.sleep(3)
print("without further ado, shall we begin?")
time.sleep(2)
Asking()
while nomo == False:
    play()
if start == True:
    Notplay()
else:
    pass
Bye()
