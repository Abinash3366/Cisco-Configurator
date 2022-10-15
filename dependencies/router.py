from datetime import datetime, time
import time
from dependencies import basic

# os.system('cls' if os.name == 'nt' else 'clear')

## Variables
Art = """
 _                    __        _    _                      
|_) _    _|_ _  __   /   _ __ _|_ o (_|    __ _ _|_ o  _ __ 
| \(_)|_| |_(/_ |    \__(_)| | |  | __||_| | (_| |_ | (_)| |
"""
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
dt = datetime.today()



# function
def router():
    while True:
        print(Art)
        print("B = Basic Configuration, A = Advanced Configuration (NIU) ")
        print("I = Interface/s Configuration, V = Vlan Configuration")
        print("Q = Quit")
        In = input("What would you like to do? ")
        print("")
        if In == "B":
            print("You have selected Basic Configuration")
            basic.Basic()
            time.sleep(1)
            continue
        elif In == "A":
            print("You have selected Advanced Configuration, this Selection is Not In Use (NIU)")
            break
        elif In == "I":
            print("You have selected Interface/s Configuration")

            break
        elif In == "V":
            print("You have selected Vlan Configuration")
            break
        elif In == "Q":
            print("You have selected to quit")
            break
        else:
            print("You have selected an invalid option")
            continue