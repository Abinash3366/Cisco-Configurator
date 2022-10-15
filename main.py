from dependencies import switch, router

# os.system('cls' if os.name == 'nt' else 'clear')
# Variables
Intro = """
 __                __        _    _ 
/   o  _  _  _    /   _ __ _|_ o (_|
\__ | _> (_ (_)   \__(_)| | |  | __|
            By Abinash
"""
PD = """
R = Router, S = Switch
Q = Quit
"""

while True:
        print(Intro)
        print(PD)
        Device = input("What is the device you want to configure? ")
        if Device == "R":
            print("You have selected a Router")
            router.router()
            continue
        elif Device == "S":
            print("You have selected a Switch")
            switch.switch()
            continue
        elif Device == "Q":
            print("Quitting")
            exit()
        else:
            print("You have selected an invalid device")
            continue