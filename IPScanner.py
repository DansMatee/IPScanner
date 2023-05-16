###################################################
###################################################
######                                       ######
######               IP Scanner              ######
######        Author: Daniel Americo         ######
######      Development Date: 28/09/2022     ######
######       Final Version Number: 1.0       ######
######                                       ######
######      This program is used to scan     ###### 
######        a network and get a list       ######
######            of all active IPs.         ######
######                                       ######
###################################################
###################################################

import subprocess, time, os

def cls(): # Helper function to clear the console
    os.system('cls' if os.name=='nt' else 'clear')

def logo():
    print(" _____ _____     _____                                  ")
    print("|_   _|  __ \   / ____|                                 ")
    print("  | | | |__) | | (___   ___ __ _ _ __  _ __   ___ _ __  ")
    print("  | | |  ___/   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| ")
    print(" _| |_| |       ____) | (_| (_| | | | | | | |  __/ |    ")
    print("|_____|_|      |_____/ \___\__,_|_| |_|_| |_|\___|_|    \n")                                                        

def ping(host):
    command = ['ping', '-n', '1', host] # Creates a string with the given arguments to look like ("ping -n 1 host")
    return subprocess.call(command) == 0 # returns true if the ping is successful

def main():
    cls()
    logo()
    print("Format IP: XXX.XXX.XXX.0")
    host = input("[*] Input local network IP: ")
    #host = "140.159.251.0" VU IP to test on, 192.168.56.0 does not work.
    try: 
        startHost = int(input("[*] Input start host number: "))
    except ValueError: # Handles error if the user does not input a number
        main()
    try:
        endHost = int(input("[*] Input end host number: "))
    except ValueError: # Handles error if the user does not input a number
        main()
    print("\nScan started\n")

    octets = host.split('.') # Splits host IP into 4 octets to use later
    IP = octets[0] + "." + octets[1] + "." + octets[2] + "." # Add first 3 octets together to form almost complete IP

    timer = time.perf_counter() # Creates a timer

    for i in range(startHost, endHost + 1):
        res = ping(IP+str(i)) # Adds the last octet (i) to the IP, completing it and then calling connect with the specified port (80)
        if res: # If we receive back True
            print(">>> Active device found at: " + IP+str(i) + f" [{time.perf_counter() - timer:.5f}]") # Shows what address we were successful in finding
    print(f"[{time.perf_counter() - timer:.5f}] Done Scanning") # Prints total time, rounded to 5 decimal places (.5f)

    while True: # Allows the user to either do another scan or quit the program
        checkControl = input("[S]can again | [Q]uit\n[*] Action: ")
        if checkControl == 's':
            main() # Calls the main function
        elif checkControl == 'q':
            quit() # Quits the program

if __name__ == "__main__":
    main()