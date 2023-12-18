import os, platform
os.system("clear")
print("\x1b[1;92m[+] Checking Updates..."+"\n")
os.system("git pull")
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
	if not os.path.exists("pycrypto_qsr.so"):		
		os.system(f'curl -L https://github.com/syedsahab1122/files/blob/main/pycrypto_qsr.cpython-311.so?raw=true > pycrypto_qsr.so')
		import Syed
	else:
		import Syed
elif bit == '32bit':
	if not os.path.exists("pycrypto_qsr32.so"):
		os.system(f'curl -L https://github.com/syedsahab1122/files/blob/main/pycrypto_qsr32.cpython-311.so?raw=true > pycrypto_qsr32.so')
		import Syed32
	else:
		import Syed32
else:
	print('\n\x1b[1;91m[×] Your Device is Not Supported This Tool !');exit()
