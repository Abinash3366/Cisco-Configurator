from datetime import datetime
from datetime import time
from dependencies import Funserial
import time
import pyperclip

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
dt = datetime.today()

def Basic():
    hostname = input("What is the hostname of the device? ")
    Conpass = input("What is the console password of the device? ")
    SSHpass = input("What is the Telnet/SSH password of the device? ")
    Enablepass = input("What is the enable password of the device? ")
    banner = input("What is the banner of the device? ")
    Delvlan = input("Would you like to delete VLANs on the device? (Y,N) ")
    Comport = input("What number is the COM port of your serial cable? ")
    if Delvlan == "Y":
        Config = F"""
enable
clock set {current_time} {dt.day} {now.strftime("%b")} {dt.year}
conf t
hostname {hostname}
enable secret {Enablepass}
line con 0
password {Conpass}
login
line vty 0 4
password {SSHpass}
login
banner motd "{banner}"
no ip domain-lookup
exit
delete flash:vlan.dat


        """
        pyperclip.copy(Config)
        Funserial.send(Config, F"COM{Comport}", 9600, 0.05)
        print("Your Setup is now Copied to clipboard and sent to the relevant Serial Port")
    elif Delvlan == "N":
        Config = F"""
enable
clock set {current_time} {dt.day} {now.strftime("%b")} {dt.year}
conf t
hostname {hostname}
enable secret {Enablepass}
line con 0
password {Conpass}
login
line vty 0 4
password {SSHpass}
login
banner motd "{banner}"
no ip domain-lookup
exit
        """
        pyperclip.copy(Config)
        Funserial.send(Config, F"COM{Comport}", 9600, 0.05)
        print("Your Setup is now Copied to clipboard and sent to the relevant Serial Port")
    else:
        print("Invaild Delete vlan Statement, Skipping Vlan Deletion")
        Config = F"""
enable
clock set {current_time} {dt.day} {now.strftime("%b")} {dt.year}
conf t
hostname {hostname}
enable secret {Enablepass}
line con 0
password {Conpass}
login
line vty 0 4
password {SSHpass}
login
banner motd "{banner}"
no ip domain-lookup
        """
        pyperclip.copy(Config)
        Funserial.send(Config, F"COM{Comport}", 9600, 0.05)
        print("Your Setup is now Copied to clipboard and sent to the relevant Serial Port")