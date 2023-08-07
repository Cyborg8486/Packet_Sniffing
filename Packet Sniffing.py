from scapy.all import *

def paksnif(packet):
    # Write packet details to a file
    with open("output.txt", "a", encoding='utf-8') as f:
        f.write(packet.show(dump=True))
        f.write('\n')

def main():
    # Start packet sniffing
    sniff(prn=paksnif, count=10)

if __name__ == '__main__':
    main()
