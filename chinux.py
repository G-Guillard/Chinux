#!/usr/bin/python2.6
# -*- coding: utf8 -*-


import sys;
import re;
import random

class chinux:

	def __init__(self):
		self.alllines = []
		self.rand = random
		self.CHINUX_VERSION = "0.1"
		self.lang = "en"
		self.HSK_level = 1
		self.merge_levels = True
		self.seed = 2
		self.nwords = -1
		self.configure("/sdcard/sl4a/scripts/chinux/chinux.conf");
		self.load_dictionary();
		global seed
		print seed
		if (seed >= 0):
			self.rand.seed(seed)


	def addaccent(self,zenewline):
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
		zenewline = zenewline.replace('ei1','e1i');
		zenewline = zenewline.replace('ei2','e2i');
		zenewline = zenewline.replace('ei3','e3i');
		zenewline = zenewline.replace('ei4','e4i');
		zenewline = zenewline.replace('ei5','e5i');			zenewline = zenewline.replace('er1','e1r');
		zenewline = zenewline.replace('er2','e2r');
		zenewline = zenewline.replace('er3','e3r');
		zenewline = zenewline.replace('er4','e4r');
		zenewline = zenewline.replace('er5','e5r');
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


	def configure(self,conf):
		try:
			file = open(conf);
		except:
			print "Error while trying to open " + conf + " : no such file or directory";

		global lang
		global HSK_level
		global merge_level
		global seed
		global nwords
		lines = file.readlines();
		file.close();

		for line in lines:
			if (len(line) > 2 and line[0] != "#"):
				if (line.split()[0] == "lang"):
					lang = line.split()[1]
				elif (line.split()[0] == "HSK_level"):
					HSK_level = int(line.split()[1])
				elif (line.split()[0] == "merge_levels"):
					merge_levels = bool(line.split()[1])
				elif (line.split()[0] == "seed"):
					seed = int(line.split()[1])
				elif (line.split()[0] == "nwords"):
					nwords = int(line.split()[1])

		print "lang :\t", lang
		print "HSK_level :\t", HSK_level
		print "merge_level :\t", merge_levels	
		print "seed :\t", seed
		print "nwords :\t", nwords


	def load_dictionary(self):
		global alllines
		dict = "/sdcard/sl4a/scripts/chinux/lang/" + lang + ".txt";
		try:
			file = open(dict);
		except:
			print "Error opening dictionary (" + dict + ") : no such file or directory";
			sys.exit(1);

		alllines = file.readlines();
		file.close();


	def lookupnewword(self):
		cut = re.compile(r'\[|\]|/');
		i=0;
		global rand
		zeline = cut.split(self.addaccent(alllines[self.rand.randint(0,len(alllines)-1)]));
		if (self.merge_levels):
			while int(zeline[0]) > HSK_level:
				zeline = cut.split(self.addaccent(alllines[self.rand.randint(0,len(alllines)-1)]));
		else:
			while (int(zeline[0]) != HSK_level):
				zeline = cut.split(self.addaccent(alllines[self.rand.randint(0,len(alllines)-1)]));
		translation = '';
	
		for i in range(3,len(zeline)-1): # 3 is ' ' and last one is '\r\n'
			if len(translation) is 0:
				translation = zeline[i];
			else:
				translation = translation + ", " + zeline[i];

		return (zeline[0].split()[0],zeline[0].split()[2],zeline[1],translation);




	def getnewword(self):

		newword = self.lookupnewword()
		if (self.merge_levels):
			while (int(newword[0]) > HSK_level):
				newword = self.lookupnewword();
		else:
			while (int(newword[0]) != HSK_level):
				newword = self.lookupnewword();

		print newword[0];
		print newword[1];
		print newword[2];
		print newword[3];


	def getnwords(self):
		global nwords
		return nwords


#	if __name__ == "__main__":
#	main();


