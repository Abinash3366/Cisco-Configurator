from dependencies import Funserial
import pyperclip


def interface(Switch, Router):
    print("You have selected Interface Configuration")
    New = True
    ip = ""
    ipsub = ""
    ipv6 = ""
    vlannum = ""
    vlan = ""
    while New:
        type = input("Did you want to configure a range (R) or a single interface (S) or Quit (Q) ? ")
        if type == "Q":
            break
        if type == "R":
            range = input("What is the range of the interfaces? (Cisco Notation, Eg Gi0/0-2) ")
            interface = F"range {range}"
        else:
            interface = input("What is the interface/ you want to configure? (Eg. G0/0/0) ")
            descrp = input("What is the description of the interface? ")
            descrp = F"description {descrp}"
            if Router == "Y":
                if input("Do you want to start the interface? ") == "Y":
                    start = "no shutdown"
                if input('Do you want the interface to have an IP (Y/N) ') == 'Y':
                    ip = input('What is the IP address of the interface? ')
                    ipsub = input('What is the subnet of the interface? ')
                    ip = F"ip address {ip} {ipsub}"
                    ipv6 = input('What is the IPv6 address of the interface? (Include Prefix) ')
                    if ipv6 == "":
                        ipv6 = ""
                    else:
                        ipv6 = F"ipv6 address {ipv6}"

        if Switch == 'Y':
            if input('Do you want to configure Vlans on the interface? (Y/N) ') == 'Y':
                vlannum = input('What Vlan mode do you want? (Access, Dynamic, Trunk) ')
                if vlannum == 'Access':
                    vlan = input('What is the Vlan number of the interface? ')
                    vlan = F"switchport access vlan {vlan}"
                vlannum = F"switchport mode {vlannum}"
        Comport = input("What number is the COM port of your serial cable? ")
        config = F"""
conf t
interface {interface}
{descrp} 
{ip}
{ipv6}
{vlannum}
{vlan}
{start}
end
"""
        pyperclip.copy(config)
        Funserial.send(config, F"COM{Comport}", 9600, 0.05)
        print("Your Setup is now Copied to clipboard and sent to the relevant Serial Port")
