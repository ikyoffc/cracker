import sys, os, subprocess, platform, struct

if sys.version_info.major != 3:
 exit('\x1b[1;94m   /\x1b[1;91m_!_\x1b[1;94m\ \x1b[1;93msilahkan menggunakan python 3 ')

if not struct.calcsize("P")*8==32:
	exit('(¡) script tidak bisa digunakan di perangkat anda')

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
	os.system('pkg install play-audio -y &> /dev/null')
	
try:
	import requests
except:
	os.system('pip install requests')
 
try:
	import sty
except:
	os.system('pip install sty')
	
try:
	import bs4
except:
	os.system('pip install bs4')
	
os.system('chmod 777 running && ./running')
