import threading
import socket
from time import sleep
from random import randint
from os import system

word_list = open('list.txt', 'rb')
current_word = []
point = 0

def draw_map() :
	global current_word
	global point
	def p_word(word) :
		tmp = '|' + ' '*randint(0, (48 - len(word))) + word
		tmp += ' ' * (49 - len(tmp)) + '|'
		return tmp
	while True :
		system('clear')
		add_word()
		print '-' * 50
		if current_word :
			print '\n'.join(p_word(i) for i in current_word[::-1])
		print '\n'.join('|' + ' '*48 + '|' for _ in range(20 - len(current_word)))
		print '-' * 50
		print 'point = {0}'.format(point)
		sleep(2)

def add_word() :
	global word_list
	global current_word
	current_word.append(word_list.readline().strip())

def receiver() :
	global point
	global current_word
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ss.bind( ( '127.0.0.1' , 9998) )
	ss.listen(1)
	conn, addr = ss.accept()
	while(True) :
		data = conn.recv(1024).strip()
		if data in current_word :
			current_word.remove(data)
			point += 1
		#conn.close()

if __name__ == '__main__' :
	threading.Thread(target=draw_map).start()
	threading.Thread(target=receiver).start()


def input_word() :
	global current_word
	while True :
		tmp = raw_input()
		if tmp in current_word :
			current_word.remove(tmp)
