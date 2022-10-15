from dependencies import basic, interface

art = """
 __                   __        _    _                      
(_     o _|_ _ |_    /   _ __ _|_ o (_|    __ _ _|_ o  _ __ 
__)\^/ |  |_(_ | |   \__(_)| | |  | __||_| | (_| |_ | (_)| |
"""


# function
def switch():
    while True:
        print(art)
        print("B = Basic Configuration, A = Advanced Configuration (NIU) ")
        print("I = Interface/s Configuration, V = Vlan Configuration")
        print("Q = Quit")
        In = input("What would you like to do? ")
        if In == "B":
            print("You have selected Basic Configuration")
            basic.Basic(Switch='Y',Router='N')
            continue
        elif In == "A":
            print("You have selected Advanced Configuration, this Selection is Not In Use (NIU)")
            break
        elif In == "I":
            print("You have selected Interface/s Configuration")
            interface.interface(Switch='Y',Router='N')
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
