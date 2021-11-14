#!/bin/python3


import os

print("\t\t[+ ] Setup File for d4rk_ddos tool [+] ")
print("-" * 90)
print("\t\t\t[+] Special Thanks to s0u1 [+] ")



try:

	import pyfiglet
	exit()
	

except:
	print("[-] pyfiglet module not installed ! ")
	print("[+] Installing pyfiglet module for you ...")
	os.system("pip3 install pyfiglet")
	print("[+] Sucessfully Installed pyfiglet module ")


try:

	import colorama
	exit()
	

except:
	print("[-] colorama module not installed ! ")
	print("[+] Installing colorama module for you .. " )
	os.system("pip3 install colorama")
	print("[+] sucessfully Installed colorama module " )
	
