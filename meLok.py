# ~ ========================== meLok Tool (OSINT) ========================== ~ #
# # meLok Tool (OSINT: Open Source Intelligence)
# Version: 0.1
# By Lunar
# © Lunar
# ~ ========================== Import & From ========================== ~ #
# ~ ========================== From ========================== ~ #
from colorama import *
# ~ ========================== Import ========================== ~ #
import requests
import json
import os
import time
import socket
init(autoreset=True)
# ~ ========================== Utils ========================== ~ #
Fore.ORANGE = f"\033[38;5;208m" # \033[38;5;208m
hostname = socket.gethostname()
# ~ ========================== meLok Clear & configuration: ASCII + Prompt & Settings ========================== ~ #
# ~ ========================== Clear ========================== ~ #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# ~ ========================== configuration ========================== ~ #
prompt = f"""{Style.BRIGHT}{Fore.ORANGE}╭─[{Fore.WHITE} {hostname} ~{Fore.ORANGE} ]
{Fore.ORANGE}╰─── {Fore.WHITE}$ """
# ~ ========================== settings ========================== ~ #
# ~ ========================== meLok Style ========================== ~ #
def meLokascii():
    meLokascii = [
    f"",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠾⠿⠿⠟⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⠰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀{Fore.ORANGE}⢀⣤⣤⡀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⢀⣴⡄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀{Fore.ORANGE}⢀⣾⠋ ⢿⡄⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⢠⣾⣿⣿⣿⣦⡀⠻⢿⣿⣿⣿⣿⣿⣿⠛⠛⠃⠀⠀⠀{Fore.ORANGE}⣼⡇⠀ ⢸⡇⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣠⣤⣤⣌⣉⠙⠻⢿⣦⣄⠙⠻⠿⣿⡿⠃{Fore.WHITE}⠰⣦⠀⠀{Fore.ORANGE}⠀⠀⣿⡄⠀⠀⣼⠇⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣶⣤⣈⠛⢿⣶⣄⠀⠀⠀⠀{Fore.WHITE}⢸⠇⠀⠀{Fore.ORANGE}⠀⠸⣧⣀⣰⠏⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡈⠛⢷⠀⠀{Fore.WHITE}⠀⣾⠀⠀⠀{Fore.ORANGE}⠀⠀⢸⡿⠁⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀{Fore.WHITE}⢸⣿⣿⣷⣦{Fore.ORANGE}⠀⠀⢸⡇⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀{Fore.WHITE}⠘⠿⣿⠿⠋{Fore.ORANGE}⠀⠀⣸⡇⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀{Fore.ORANGE}⠛⠁⠀⠀⠀⠀",
    f""
    ]
    for line in meLokascii:
        print(line)
        time.sleep(0.02)
def meLokasciinostyle():
    meLokasciinostyle = [
    f"",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠾⠿⠿⠟⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⠀⠀⠰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀{Fore.ORANGE}⢀⣤⣤⡀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⠀⠀⢀⣴⡄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀{Fore.ORANGE}⢀⣾⠋ ⢿⡄⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠀⢠⣾⣿⣿⣿⣦⡀⠻⢿⣿⣿⣿⣿⣿⣿⠛⠛⠃⠀⠀⠀{Fore.ORANGE}⣼⡇⠀ ⢸⡇⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣠⣤⣤⣌⣉⠙⠻⢿⣦⣄⠙⠻⠿⣿⡿⠃{Fore.WHITE}⠰⣦⠀⠀{Fore.ORANGE}⠀⠀⣿⡄⠀⠀⣼⠇⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣶⣤⣈⠛⢿⣶⣄⠀⠀⠀⠀{Fore.WHITE}⢸⠇⠀⠀{Fore.ORANGE}⠀⠸⣧⣀⣰⠏⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡈⠛⢷⠀⠀{Fore.WHITE}⠀⣾⠀⠀⠀{Fore.ORANGE}⠀⠀⢸⡿⠁⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀{Fore.WHITE}⢸⣿⣿⣷⣦{Fore.ORANGE}⠀⠀⢸⡇⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀{Fore.WHITE}⠘⠿⣿⠿⠋{Fore.ORANGE}⠀⠀⣸⡇⠀⠀⠀⠀",
    f"{Style.BRIGHT}{Fore.ORANGE}          ⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀{Fore.ORANGE}⠛⠁⠀⠀⠀⠀",
    f""
    ]
    for line in meLokasciinostyle:
        print(line)
def meLokmenu():
    meLokmenu = [
    f"",
    f"{Style.BRIGHT}{Fore.ORANGE}  > OSINT Tool",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}01{Fore.ORANGE}] IP LookUp           {Fore.ORANGE}[{Fore.WHITE}11{Fore.ORANGE}] Shodan            {Fore.ORANGE}[{Fore.WHITE}21{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}02{Fore.ORANGE}] MAC LookUp          {Fore.ORANGE}[{Fore.WHITE}12{Fore.ORANGE}] Google Dorking    {Fore.ORANGE}[{Fore.WHITE}22{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}03{Fore.ORANGE}] Email LookUp        {Fore.ORANGE}[{Fore.WHITE}13{Fore.ORANGE}] Reverse Geocoding {Fore.ORANGE}[{Fore.WHITE}23{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}04{Fore.ORANGE}] Username LookUp     {Fore.ORANGE}[{Fore.WHITE}14{Fore.ORANGE}] Website Analysis  {Fore.ORANGE}[{Fore.WHITE}24{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}05{Fore.ORANGE}] Name LookUp         {Fore.ORANGE}[{Fore.WHITE}15{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}25{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}06{Fore.ORANGE}] Social Media LookUp {Fore.ORANGE}[{Fore.WHITE}16{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}26{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}07{Fore.ORANGE}] Domain LookUp       {Fore.ORANGE}[{Fore.WHITE}17{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}27{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}08{Fore.ORANGE}] VIN LookUp          {Fore.ORANGE}[{Fore.WHITE}18{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}28{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}09{Fore.ORANGE}] ID LookUp           {Fore.ORANGE}[{Fore.WHITE}19{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}29{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}10{Fore.ORANGE}] Phone Number LookUp {Fore.ORANGE}[{Fore.WHITE}20{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}30{Fore.ORANGE}] Soon",
    f""
    ]
    for line in meLokmenu:
        print(line)
        time.sleep(0.02)    
def meLokmenunostyle():
    meLokmenunostyle = [
    f"",
    f"{Style.BRIGHT}{Fore.ORANGE}  > OSINT Tool",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}01{Fore.ORANGE}] IP LookUp           {Fore.ORANGE}[{Fore.WHITE}11{Fore.ORANGE}] Shodan            {Fore.ORANGE}[{Fore.WHITE}21{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}02{Fore.ORANGE}] MAC LookUp          {Fore.ORANGE}[{Fore.WHITE}12{Fore.ORANGE}] Google Dorking    {Fore.ORANGE}[{Fore.WHITE}22{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}03{Fore.ORANGE}] Email LookUp        {Fore.ORANGE}[{Fore.WHITE}13{Fore.ORANGE}] Reverse Geocoding {Fore.ORANGE}[{Fore.WHITE}23{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}04{Fore.ORANGE}] Username LookUp     {Fore.ORANGE}[{Fore.WHITE}14{Fore.ORANGE}] Website Analysis  {Fore.ORANGE}[{Fore.WHITE}24{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}05{Fore.ORANGE}] Name LookUp         {Fore.ORANGE}[{Fore.WHITE}15{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}25{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}06{Fore.ORANGE}] Social Media LookUp {Fore.ORANGE}[{Fore.WHITE}16{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}26{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}07{Fore.ORANGE}] Domain LookUp       {Fore.ORANGE}[{Fore.WHITE}17{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}27{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}08{Fore.ORANGE}] VIN LookUp          {Fore.ORANGE}[{Fore.WHITE}18{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}28{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}09{Fore.ORANGE}] ID LookUp           {Fore.ORANGE}[{Fore.WHITE}19{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}29{Fore.ORANGE}] Soon",
    f"{Style.BRIGHT}  {Fore.ORANGE}[{Fore.WHITE}10{Fore.ORANGE}] Phone Number LookUp {Fore.ORANGE}[{Fore.WHITE}20{Fore.ORANGE}] Soon              {Fore.ORANGE}[{Fore.WHITE}30{Fore.ORANGE}] Soon",
    f""
    ] 
    for line in meLokmenunostyle:
        print(line)   
def meLokpub():
    meLokpub = [
    f"{Style.BRIGHT}  {Fore.ORANGE}  ╭─────────────────────────────────────────╮ ",
    f"{Style.BRIGHT}  {Fore.ORANGE}  │ {Fore.WHITE}Github {Fore.ORANGE}: {Fore.WHITE}github.com/Lunarrrrrrrrr/meLok {Fore.ORANGE}│ ",
    f"{Style.BRIGHT}  {Fore.ORANGE}  ╰─────────────────────────────────────────╯ "
    ]
    for line in meLokpub:
        print(line)
        time.sleep(0.02)   
def meLokpubnostyle():
    meLokpubnostyle = [
    f"{Style.BRIGHT}  {Fore.ORANGE}  ╭─────────────────────────────────────────╮ ",
    f"{Style.BRIGHT}  {Fore.ORANGE}  │ {Fore.WHITE}Github {Fore.ORANGE}: {Fore.WHITE}github.com/Lunarrrrrrrrr/meLok {Fore.ORANGE}│ ",
    f"{Style.BRIGHT}  {Fore.ORANGE}  ╰─────────────────────────────────────────╯ "
    ]
    for line in meLokpubnostyle:
        print(line) 
# ~ ========================== meLok TOOL ========================== ~ # 
def meLok():
    while True:
        clear()
        meLokasciinostyle()
        meLokpubnostyle()
        meLokmenunostyle()
        melockprompt = input(prompt)
        if melockprompt == "#":
            exit()
        elif melockprompt == "1":
            o1()
        elif melockprompt == "2":
            o2()
        elif melockprompt == "3":
            o3()
        elif melockprompt == "4":
            o4()
        elif melockprompt == "5":
            o5()
        elif melockprompt == "6":
            o6()
        elif melockprompt == "7":
            o7()
        elif melockprompt == "8":
            o8()
        elif melockprompt == "9":
            o9()
        elif melockprompt == "10":
            o10()
        elif melockprompt == "11":
            o11()
        elif melockprompt == "12":
            o12()
        elif melockprompt == "13":
            o13()
        elif melockprompt == "14":
            o14()
        elif melockprompt == "15":
            o15()
        elif melockprompt == "16":
            o16()
        elif melockprompt == "17":
            o17()
        elif melockprompt == "18":
            o18()
        elif melockprompt == "19":
            o19()
        elif melockprompt == "20":
            o20()
        elif melockprompt == "21":
            o21()
        elif melockprompt == "22":
            o22()
        elif melockprompt == "23":
            o23()
        elif melockprompt == "24":
            o24()
        elif melockprompt == "25":
            o25()
        elif melockprompt == "26":
            o26()
        elif melockprompt == "27":
            o27()
        elif melockprompt == "28":
            o28()
        elif melockprompt == "29":
            o29()
        elif melockprompt == "30":
            o30()
# ~ ========================== meLok Option ========================== ~ # 
def o1():
    print("Option 1 selected.")
    time.sleep(2)

def o2():
    print("Option 2 selected.")
    time.sleep(2)

def o3():
    print("Option 3 selected.")
    time.sleep(2)

def o4():
    print("Option 4 selected.")
    time.sleep(2)

def o5():
    print("Option 5 selected.")
    time.sleep(2)

def o6():
    print("Option 6 selected.")
    time.sleep(2)

def o7():
    print("Option 7 selected.")
    time.sleep(2)

def o8():
    print("Option 8 selected.")
    time.sleep(2)

def o9():
    print("Option 9 selected.")
    time.sleep(2)

def o10():
    print("Option 10 selected.")
    time.sleep(2)

def o11():
    print("Option 11 selected.")
    time.sleep(2)

def o12():
    print("Option 12 selected.")
    time.sleep(2)

def o13():
    print("Option 13 selected.")
    time.sleep(2)

def o14():
    print("Option 14 selected.")
    time.sleep(2)

def o15():
    print("Option 15 selected.")
    time.sleep(2)

def o16():
    print("Option 16 selected.")
    time.sleep(2)

def o17():
    print("Option 17 selected.")
    time.sleep(2)

def o18():
    print("Option 18 selected.")
    time.sleep(2)

def o19():
    print("Option 19 selected.")
    time.sleep(2)

def o20():
    print("Option 20 selected.")
    time.sleep(2)

def o21():
    print("Option 21 selected.")
    time.sleep(2)

def o22():
    print("Option 22 selected.")
    time.sleep(2)

def o23():
    print("Option 23 selected.")
    time.sleep(2)

def o24():
    print("Option 24 selected.")
    time.sleep(2)

def o25():
    print("Option 25 selected.")
    time.sleep(2)

def o26():
    print("Option 26 selected.")
    time.sleep(2)

def o27():
    print("Option 27 selected.")
    time.sleep(2)

def o28():
    print("Option 28 selected.")
    time.sleep(2)

def o29():
    print("Option 29 selected.")
    time.sleep(2)

def o30():
    print("Option 30 selected.")
    time.sleep(2)
    
if __name__ == '__main__':
    clear()
    meLokascii()
    meLokpub()
    meLokmenu()
    meLok()