def vlan():
    vlan = input('What is the Vlan number of the interface? ')
    vlanname = input('What is the name of the Vlan? ')
    if input(F'Does {vlanname} have an IP') == 'Y':
        vlanip = input('What is the IP address of the Vlan? ')
        vlanipsub = input('What is the subnet of the Vlan? ')
        vlanip = F"ip address {vlanip} {vlanipsub}"
        vlanipv6 = input('What is the IPv6 address of the Vlan? (Include Prefix)')
        if vlanipv6 == "":
            vlanipv6 = ""
        else:
            vlanipv6 = F"ipv6 address {vlanipv6}"
        if input('Do you want to configure a description on the vlan? ') == 'Y':
            vlandescrp = input('What is the description of the Vlan? ')
            vlandescrp = F"description {vlandescrp}"
