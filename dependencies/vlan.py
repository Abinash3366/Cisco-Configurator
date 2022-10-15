def vlan():
    vlan = input('What is the Vlan number of the interface? ')
    vlanname = input('What is the name of the Vlan? ')
    if input(F'Does {vlanname} have an IP') == 'Y':
        vlanip = input('What is the IP address of the Vlan? ')
        vlanipsub = input('What is the subnet of the Vlan? ')
        vlanipv6 = input('What is the IPv6 address of the Vlan? (Include Prefix)')
        if input('Do you want to configure a description on the vlan? ') == 'Y':