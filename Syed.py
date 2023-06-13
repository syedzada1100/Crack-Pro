import os, platform

os.system("git pull")

bit = platform.architecture()[0]

if bit == '64bit':

	if not os.path.exists("pycrypto_qsr.so"):		os.system(f'curl -L https://github.com/syedsahab1122/files/blob/main/pycrypto_qsr.cpython-311.so?raw=true > pycrypto_qsr.so')

		from Syed import Legend

		Legend()

	else:

		from Syed import Legend

		Legend()

elif bit == '32bit':

	if not os.path.exists("pycrypto_qsr32.so"):

		os.system(f'curl -L https://github.com/syedsahab1122/files/blob/main/pycrypto_qsr32.cpython-311.so?raw=true > pycrypto_qsr32.so')

		from Syed32 import Legend

		Legend()

	else:

		from Syed32 import Legend

		Legend()

else:

	print('\n\x1b[1;91m[×] Your Device is Not Supported This Tool !');exit()

	
