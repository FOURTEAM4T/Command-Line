import os
os.chdir("..")
os.chdir("modes")
f = open("modes_list.4t","r")
modes = f.readline().split(",")
os.chdir("..")
os.chdir("ComLine")
from locale import currency
import random
import time
load = ["Loading...","Coder is sleeping. Please wait...","Have you got a ticket?","Oh what are you doing here?","Hello! Type /info for more info (About you :D)","Another phrase","What is this mean?","Dinner time!","It's starting!","What's next?","Chance to see this message is 0.00000000001%. You are lucky!","How long will this be?","Nice to see you again!","abc","Welcome to the circes!","Can't stop!","You will see this messages again and again","Do you like ice cream?","Now you are SUPERHERO!!!!Not.","Waiting is boring."]
l = random.choice(load)
print(l)
if l == "How long will this be?":
    time.sleep(4)
time.sleep(1)
import keyboard
import shutil
import win11toast
import psutil
import platform
from datetime import datetime
import requests
from colorama import Fore, init
import atexit
import importlib
import sys
import psutil
import logging
o = 0
nothing = ""
if nothing in modes:
    removing = True
    while removing == True:
        modes.remove(nothing)
        if not nothing in modes:
            removing = False
for i in modes:
    g = modes[o]
    __import__(g)
y = 0
for i in modes:
    im3 = modes[y]
    y = y+1
    im4 = importlib.import_module(im3)
    im4.system()
try:
    def exit_handler():
        print ('Session ended')

    os.chdir("..")
    os.chdir("sets")
    f = open("license.4t","r")
    lis = f.readline()
    os.chdir("..")
    os.chdir("ComLine")
    if lis == "none":
        print("Free version.")
        lisence = "free"
    elif lis == "basic":
        print("Standart version")
        lisence = "standart"
    elif lis == "premium":
        print("Premium version")
        lisence = "premium"
    elif lis == "dev":
        print("Develooper version")
        lisence = "dev"
    else:
        print("Lisence error")

    run = True

    def info():
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")
        # Boot Time
        print("="*40, "Boot Time", "="*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        # let's print CPU information
        print("="*40, "CPU Info", "="*40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")
        # Memory Information
        print("="*40, "Memory Information", "="*40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"Used: {get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")
        # Disk Information
        print("="*40, "Disk Information", "="*40)
        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)}")
            print(f"  Free: {get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {get_size(disk_io.read_bytes)}")
        print(f"Total write: {get_size(disk_io.write_bytes)}")
        # Network information
        print("="*40, "Network Information", "="*40)
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    def location():


        def get_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response["ip"]


        def get_location():
            ip_address = get_ip()
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "ip": ip_address,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name")
            }
            ip = "ip: ",ip_address
            city ="city: ",response.get("city")
            region ="region: ",response.get("region")
            country ="country: ",response.get("country_name")
            print(ip)
            print(city)
            print(region)
            print(country)


        get_location()
    def get_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    def ip():


        def get_location():
            ip_address = input("Type your ip: ")
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "ip": ip_address,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name")
            }
            ip = "ip: ",ip_address
            city ="city: ",response.get("city")
            region ="region: ",response.get("region")
            country ="country: ",response.get("country_name")
            print(ip)
            print(city)
            print(region)
            print(country)


        get_location()
    def caesar():
        init()
        # Define a function for Caesar cipher encryption.
        def implement_caesar_cipher(text, key, decrypt=False):
           # Initialize an empty string to store the result.
           result = ""
           # Iterate through each character in the input text.
           for char in text:
               # Check if the character is alphabetical.
               if char.isalpha():
                   # Determine the shift value using the provided key (or its negation for decryption).
                   shift = key if not decrypt else -key
                   # Check if the character is lowercase
                   if char.islower():
                       # Apply the Caesar cipher encryption/decryption formula for lowercase letters.
                       result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                   else:
                       # Apply the Caesar cipher encryption/decryption formula for uppercase letters.
                       result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
               else:
                   # If the character is not alphabetical, keep it as is e.g. numbers, punctuation
                   result += char
           # Return the result, which is the encrypted or decrypted text
           return result
        def crack_caesar_cipher(ciphertext):
           # Iterate through all possible keys (0 to 25) as there 26 alphabets.
           for key in range(26):
               # Call the caesar_cipher function with the current key to decrypt the text.
               decrypted_text = implement_caesar_cipher(ciphertext, key, decrypt=True)
               # Print the result, showing the decrypted text for each key
               print(f"{Fore.RED}Key {key}: {decrypted_text}")
        # Accept user input.
        encrypted_text = input(f"{Fore.GREEN}[?] Please Enter the text/message to decrypt: ")
        # Check if the user does not specify anything.
        if not encrypted_text:
           print(f"{Fore.RED}[-] Please specify the text to decrypt.")
        else:
            crack_caesar_cipher(encrypted_text)
    def country_info():
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        print("country:", response.get("country_name"))
        print("currency:", response.get("currency_name"))
        print("country calling code:", response.get("country_calling_code"))
        print("time zone:", response.get("utc_offset"))
        print("languages:", response.get("languages"))
        print("your postal:", response.get("postal"))
        print("capital:", response.get("country_capital"))

    an = False

    def command():
        com = input().strip().lower()
        if com == "/close":
            exit()
        try:
            if com == "":
                com = "nothing"
            if com == "/keytap":
                key = input()
                keyboard.press_and_release(key)
            elif com == "/print":
                  pr = input()
                  print(pr)
            elif com == ":)":
                print("\033[32;1mMy answer is smile :)\033[0m")
            elif com == "/file.create":
                fn = input("File name (Please type extensions :>]):")
                f = open(fn,"a")
                f.close()
            elif com == "/dir.create":
                dr = input()
                os.mkdir(dr)
            elif com == "/del.dir":
                dr = input()
                shutil.rmtree(dr)
            elif com == "/del.file":
                f = input()
                os.remove(f)
            elif com == "/open":
                f = input()
                os.system(f)
            elif com == "/caesar":
                caesar()
            elif com == "/info":
                info()
            elif com == "/location":
                location()
            elif com== "/help":
                os.chdir("..")
                os.chdir("help")
                os.system("help.txt")
                os.chdir("..")
                os.chdir("ComLine")
            elif com == "/ip":
                if lisence == "free" or lisence=="standart" or lisence=="premium":
                    print("IP are coming soon!")
                elif lisence == "dev":
                    ip()
                else:
                    print("IP are coming soon!")
            elif com == "/variable":
                if lisence=="free" or lisence=="standart" or lisence=="premium":
                    pass
                elif lisence=="dev":
                    what_variable = input('Which Variable?: ')
                    print(globals()[what_variable])
                else:
                    pass
            elif com == "/country.info":
                country_info()
            elif com == "/upgrade":
                print("Your license is",lisence+".")
                print("Others coming soon.")
            elif com == "/install":
                importer = input("What mode you want to install?: ")
                try:
                    __import__(importer)
                    x = len(modes)
                    x=x-1
                    modes.append(importer)
                    os.chdir("..")
                    os.chdir("modes")
                    f = open("modes_list.4t","a")
                    f.write(","+importer)
                    os.chdir("..")
                    os.chdir("ComLine")
                except:
                    print("No mode named",importer)
            elif com == "/modes":
                y = 0
                for i in modes:
                    print(modes[y])
                    y = y+1
            elif com == "/unistall":
                unistaller = input("What mode you want to unistall?: ").strip()
                question = input("Sure (yes/no): ").lower().strip()
                if question == "yes":
                    if unistaller in modes:
                        if unistaller == "mode_example" or unistaller == "test":
                            print("Can't unistall system modes")
                        else:
                            modes.remove(unistaller)
                            os.chdir("..")
                            os.chdir("modes")
                            f = open("modes_list.4t","r")
                            s = f.read()
                            f.close()
                            f = open("modes_list.4t","w")
                            d = s.replace(unistaller,"")
                            f.write(d)
                            f.close()
                            os.chdir("..")
                            os.chdir("ComLine")
                    else:
                        print("No mode named",unistaller)
            else:

                y = 0
                for i in modes:
                    im = modes[y]
                    y = y+1
                    im2 = importlib.import_module(im)
                    im2.main(com)
                    os.chdir("..")
                    os.chdir("mode_editor")
                    f = open("answer.4t","r")
                    os.chdir("..")
                    os.chdir("ComLine")
                    ans = f.readline()
                    an = False
                    if ans == "True":
                        an = True
                        break
                    elif ans == "False":
                        pass
                    else:
                        print("Errrrrrrroooooorrororor. Files error")
                if an == True:
                    pass
                else:
                    err2 = [com+" is genius","Try other command","I don't know this command","I am not sure but "+com+" isn't right","Oh that's strange!","BOOOOOO! Don't care I'm only typo in "+com,"Please give up! You will never type command right","Another typo","Last try!"]
                    print("\033[31;1m"+random.choice(err2)+"\033[0m")
        except Exception as err:
            print('\033[31;1mI have an error. You can read help file by command "/help"\033[0m')
            if lisence == "free" or lisence == "premium" or lisence == "standart":
                pass
            elif lisence == "dev":
                print(err)
    while run==True:
        print("Command Line v0.1.0 beta by 4T")
        print("Created with Python 3.12")
        print("Type your command:")
        command()
    while run==False:
        pass
finally:
    pass