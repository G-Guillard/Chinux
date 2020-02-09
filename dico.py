#!/usr/bin/python2.5
# -*- coding: utf8 -*-


import sys;
import re;
import tty,termios
import os

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
	return ch


def addaccent(zenewline):
	zenewline = zenewline.replace('ng1','1ng');
	zenewline = zenewline.replace('ng2','2ng');
	zenewline = zenewline.replace('ng3','3ng');
	zenewline = zenewline.replace('ng4','4ng');
	zenewline = zenewline.replace('ng5','5ng');
	zenewline = zenewline.replace('n1','1n');
	zenewline = zenewline.replace('n2','2n');
	zenewline = zenewline.replace('n3','3n');
	zenewline = zenewline.replace('n4','4n');
	zenewline = zenewline.replace('n5','5n');
	zenewline = zenewline.replace('ao1','a1o');
	zenewline = zenewline.replace('ao2','a2o');
	zenewline = zenewline.replace('ao3','a3o');
	zenewline = zenewline.replace('ao4','a4o');
	zenewline = zenewline.replace('ao5','a5o');
	zenewline = zenewline.replace('ai1','a1i');
	zenewline = zenewline.replace('ai2','a2i');
	zenewline = zenewline.replace('ai3','a3i');
	zenewline = zenewline.replace('ai4','a4i');
	zenewline = zenewline.replace('ai5','a5i');
	zenewline = zenewline.replace('e1i','e1i');
	zenewline = zenewline.replace('ei2','e2i');
	zenewline = zenewline.replace('ei3','e3i');
	zenewline = zenewline.replace('ei4','e4i');
	zenewline = zenewline.replace('ei5','e5i');
	zenewline = zenewline.replace('ou1','o1u');
	zenewline = zenewline.replace('ou2','o2u');
	zenewline = zenewline.replace('ou3','o3u');
	zenewline = zenewline.replace('ou4','o4u');
	zenewline = zenewline.replace('ou5','o5u');
	zenewline = zenewline.replace('a1','ā');
	zenewline = zenewline.replace('a2','á');
	zenewline = zenewline.replace('a3','ǎ');
	zenewline = zenewline.replace('a4','à');
	zenewline = zenewline.replace('a5','a');
	zenewline = zenewline.replace('e1','ē');
	zenewline = zenewline.replace('e2','é');
	zenewline = zenewline.replace('e3','ě');
	zenewline = zenewline.replace('e4','è');
	zenewline = zenewline.replace('e5','e');
	zenewline = zenewline.replace('i1','ī');
	zenewline = zenewline.replace('i2','í');
	zenewline = zenewline.replace('i3','ǐ');
	zenewline = zenewline.replace('i4','ì');
	zenewline = zenewline.replace('i5','i');
	zenewline = zenewline.replace('o1','ō');
	zenewline = zenewline.replace('o2','ó');
	zenewline = zenewline.replace('o3','ǒ');
	zenewline = zenewline.replace('o4','ò');
	zenewline = zenewline.replace('o5','o');
	zenewline = zenewline.replace('u1','ū');
	zenewline = zenewline.replace('u2','ú');
	zenewline = zenewline.replace('u3','ǔ');
	zenewline = zenewline.replace('u4','ù');
	zenewline = zenewline.replace('u5','u');
	zenewline = zenewline.replace('u:1','ǖ');
	zenewline = zenewline.replace('u:2','ǘ');
	zenewline = zenewline.replace('u:3','ǚ');
	zenewline = zenewline.replace('u:4','ǜ');
	zenewline = zenewline.replace('u:5','ü');
	zenewline = zenewline.replace('u:','ü');
	zenewline = zenewline.replace('v1','ǖ');
	zenewline = zenewline.replace('v2','ǘ');
	zenewline = zenewline.replace('v3','ǚ');
	zenewline = zenewline.replace('v4','ǜ');
	zenewline = zenewline.replace('v5','ü');
	return zenewline;




def lookupword(current):

	try:
		file = open("newdico.txt");
	except:
		print "The dictionary file do not exist !";
		sys.exit(1);

	lines = file.readlines();
	file.close();

	cut = re.compile(r'\[|\]|/');

	i=0;
	zeline = cut.split(addaccent(lines[current]));
	translation = '';
	for i in range(3,len(zeline)-1): # 3 is ' ' and last one is '\r\n'
		if len(translation) is 0:
			translation = zeline[i];
		else:
			translation = translation + ", " + zeline[i];

#		print zeline[i];

	return (zeline[0].split()[1],zeline[1],translation,lines[current]);



def lookupnewword(level,current):
	word = lookupword(current);
	if level != 0:
		while len(unicode(word[0],"utf8"))>level:
			word = lookupword();
	return word;



def main():
	level = 0;
	current = 0
	choice = 0
	while choice!='q' and choice!='Q':
		os.system('clear')
		if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == 'd' or choice == 'D' or choice == 0:
			result = lookupnewword(level,current);
			current = current + 1
		else:
			print "Please select a difficulty level between 1 (easy) and 4 (very hard)\nor 'q' (quit)"

		print "==============================================================================="
		print result[0];
		print "-------------------------------------------------------------------------------"
		print result[1];
		print "-------------------------------------------------------------------------------"
		print result[2];
		print "==============================================================================="
		print result[3]
#		choice = sys.stdin.readline(1)
		choice = getch()




if __name__ == "__main__":
	main();


