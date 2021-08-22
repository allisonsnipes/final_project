# Create a program that can detect active ARP spoofing attacks on host machines.

import os

def getArpEntries():
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    addresses = {}


    for line in arp_table_lines:

        try:
            question, ip, where, mac, status, interface, ifscope, _type, interface2  = line.split()
        except:
            try:
                question, ip, where, mac, status, interface, ifscope, interface2 = line.split()
            except:
                continue

        if not mac in addresses:
            addresses[mac] = []
        addresses[mac].append(ip)

    return addresses


def duplicateMac():
    


def main():
    addresses = getArpEntries()
    print(addresses)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
