#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import curses;
import chinux;
import locale;

locale.setlocale(locale.LC_ALL, "");


def format_text2(str,textwidth,delimiter=' '):
	i = 0;
	phrase = [];
#	if delimiter is '':
#		if len(unicode(str,"utf8"))*2>textwidth:
#			size = len(str)/(len(str)/textwidth+1);
#			while i+size<len(str):
#				phrase.append(str[i:i+size]);
#				i = i+size;
#		else:
#			phrase.append(str);
#	else:
	phrase.append(str);
	return phrase;

def format_text(str,textwidth,delimiter=' '):
	i = 0;
	phrase = [];
#	while len(str[i:i+textwidth])>1:
	while i+textwidth<len(str):
			phrase.append(str[i:i+textwidth].rsplit(delimiter,1)[0]);
			i = i+len(phrase[len(phrase)-1])+1;
	phrase.append(str[i:i+textwidth]);
	return phrase;




def main():
	level = 5;
	w1x = 1;
	w1y = 1;
	w1w = 26;
	w1h = 10;
	w2x = 27;
	w2y = 1;
	w2w = 26;
	w2h = 10;
	w3x = 1;
	w3y = 11;
	w3w = 52;
	w3h = 10;
	choice = 0;
	while choice != ord('q'):
		scr = curses.initscr();
		scr.clear();
		scr.border(0);
		scr.refresh();
		result = chinux.lookupnewword(level);
		w1 = curses.newwin(w1h,w1w,w1y,w1x);
		w1.box();
		w2 = curses.newwin(w2h,w2w,w2y,w2x);
		w2.box();
		w3 = curses.newwin(w3h,w3w,w3y,w3x);
		w3.box();
		try:
			formatted = format_text2(result[0],4,'');
			for i,text in enumerate(formatted):
				# Chinese characters take two latin characters, hence the "*2"
				w1.addstr((w1h-len(formatted))/2+i+1,(w1w-len(unicode(text,"utf8")*2)%w1w)/2, text); 
			formatted = format_text(result[1],w2w-2);
			for i,text in enumerate(formatted):
				w2.addstr((w2h-len(formatted))/2+i+1,(w2w-len(unicode(text,"utf8"))%w2w)/2, text);
			formatted = format_text(result[2],w3w-2);
			for i,text in enumerate(formatted):
				w3.addstr((w3h-len(formatted))/2+i+1,(w3w-len(unicode(text,"utf8"))%w3w)/2, text);
		except:
			print result;
		w1.refresh();
		w2.refresh();
		w3.refresh();
#		scr.refresh();
		choice = w1.getch();

	curses.endwin();








if __name__ == "__main__":
	main();


