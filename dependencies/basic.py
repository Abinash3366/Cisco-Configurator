from datetime import datetime
from datetime import time
from dependencies import Funserial
import time
import pyperclip

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
dt = datetime.today()

def Basic(Switch, Router):
    hostname = input("What is the hostname of the device? ")
    Conpass = input("What is the console password of the device? ")
    SSHpass = input("What is the Telnet/SSH password of the device? ")
    Enablepass = input("What is the enable password of the device? ")
    banner = input("What is the banner of the device? ")
    Delvlan = input("Would you like to delete VLANs on the device? (Y,N) ")
    if Delvlan == "Y":
        vlanStatus = "delete flash:vlan.dat"
    else:
        print("VLANs will not be deleted")
    if Router == "Y":
        ipv6 = input("Would you like to enable IPv6 on the device? (Y,N) ")
        if ipv6 == "Y":
            ipv6Status = "ipv6 unicast-routing"
        else:
            print("IPv6 will not be enabled")
    Comport = input("What number is the COM port of your serial cable? ")
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
{ipv6Status}
exit
{vlanStatus}



    """
    pyperclip.copy(Config)
    Funserial.send(Config, F"COM{Comport}", 9600, 0.05)
    print("Your Setup is now Copied to clipboard and sent to the relevant Serial Port")
    time.sleep(1)