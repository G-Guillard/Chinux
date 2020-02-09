#!/usr/bin/python2.6
# -*- coding: utf8 -*-


# Nice missing features (randomly sorted) :
# - status bar (indicating current level, etc.)
# - option to choose the number of characters ?
# - history ?
# - possibility to hide characters ?
# - dictionary (to search for a word without exiting the main interface)
# - draw characters and check the drawing
# - (espeak-based) reader


import pygtk
import pango
pygtk.require('2.0')
import gtk
import chinux

VERSION = "0.1"

# GTK menu
ui_string = """<ui>
  <menubar name='Menubar'>
    <menu action='FileMenu'>
      <menuitem action='Quit'/>
    </menu>
    <menu action='OptionMenu'>
      <menuitem action='HSK level'/>
      <menuitem action='HSK1'/>
      <menuitem action='HSK2'/>
      <menuitem action='HSK3'/>
      <menuitem action='HSK4'/>
      <menuitem action='HSK5'/>
      <menuitem action='HSK6'/>
      <menuitem action='HSK7'/>
     <separator/>
      <menuitem action='MergeLevels'/>
      <menuitem action='ShowLabels'/>
     <separator/>
     <separator/>
      <menuitem action='Seed'/>
    </menu>
    <menu action='HelpMenu'>
      <menuitem action='About'/>
    </menu>
  </menubar>
</ui>"""

#      <menuitem action='Language'/>
#      <menuitem action='English'/>

class gtkgui:
	def __init__(self):
		self.hist_zh = []
		self.hist_pinyin = []
		self.hist_en = []
		self.cur_pos = 0
		self.history = 10
		self.level = 1
		self.labels = False

		# Create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		# Set window title
		self.window.set_title("Chinux")
		# Set a handler for the "destroy" event which will exit GTK
		self.window.connect("destroy",self.destroy)
		# Set window border size
		self.window.set_border_width(1)
		# Create a table for widgets
		table = gtk.Table(2,2,True)
		# Attach table to window
#		self.window.add(table)
		main_vbox = gtk.VBox(False,1)
		self.window.add(main_vbox)
		self.create_ui()
		# Default strings
		self.hist_zh.append("光顾")
		self.hist_pinyin.append("guāng gù")
		self.hist_en.append("Welcome")
		# Create the chinese characters label
		if self.labels:
			self.frame_zh = gtk.Frame("Chinese characters")
		else:
			self.frame_zh = gtk.Frame()
		self.label_zh = gtk.Label(self.hist_zh[0])
		self.label_zh.modify_font(pango.FontDescription("sans 48"))
		self.label_zh.set_width_chars(6)
		self.label_zh.set_line_wrap(True)
		# Attach the label to the table
		self.frame_zh.add(self.label_zh)
		table.attach(self.frame_zh,0,1,0,1)
		# Create the pinyin label
		if self.labels:
			self.frame_pinyin = gtk.Frame("Pinyin pronunciation")
		else:
			self.frame_pinyin = gtk.Frame()
		self.label_pinyin = gtk.Label(self.hist_pinyin[0])
		self.label_pinyin.set_width_chars(20)
		self.label_pinyin.set_line_wrap(True)
		# Attach the label to the table
		self.frame_pinyin.add(self.label_pinyin)
		table.attach(self.frame_pinyin,1,2,0,1)
		# Create the English label
		if self.labels:
			self.frame_en = gtk.Frame("English translation")
		else:
			self.frame_en = gtk.Frame()
		self.label_en = gtk.Label(self.hist_en[0])
		self.label_en.set_width_chars(20)
		self.label_en.set_line_wrap(True)
		# Attach the label to the table
		self.frame_en.add(self.label_en)
		table.attach(self.frame_en,0,1,1,2)
		# Create buttons
		button_next = gtk.Button("Next")
		button_prev = gtk.Button("Previous")
		button_quit = gtk.Button("Quit")
		# Connect buttons
		button_next.connect("clicked",self.callback,"Next")
		button_prev.connect("clicked",self.callback,"Previous")
		button_quit.connect("clicked",self.destroy)
		# Attach button to last panel
		navigbox = gtk.HBox(True,0) # Homogeneous,spacing
		navigbox.pack_start(button_prev,False,True,5) # expand,fill,padding
		navigbox.pack_start(button_next,False,True,5) # expand,fill,padding)
		navigbox.pack_start(button_quit,False,True,5) # expand,fill,padding)
		table.attach(navigbox,1,2,1,2)

		main_vbox.pack_start(self.ui.get_widget('/Menubar'),expand=False)
		main_vbox.pack_start(table,False,True,0)

	        status = gtk.Statusbar()
	        main_vbox.pack_end(status, expand=False)

		# Display the window
		self.window.show_all()


	# Get next or previous entry
	def callback(self,widget,data):
		if data == "Next":
			self.getnext()
		if data == "Previous":
			self.getprev()

	# Safely quit chinux
	def destroy(self,widget,data=None):
		print "Exiting."
		gtk.main_quit()

	# Set HSK difficulty level
	def setlevel(self,widget,data):
		self.level = data
		print self.level

	# Get next entry
	def getnext(self):
		# We are not browsing the history
		if self.cur_pos+1 == self.history or (len(self.hist_zh)<self.history and self.cur_pos==len(self.hist_zh)-1):
			# Get a new entry
			result = chinux.lookupnewword(self.level)
			self.label_zh.set_text(result[0])
			self.label_pinyin.set_text(result[1])
			self.label_en.set_text(result[2])

			self.hist_zh.append(self.label_zh.get_text())
			if len(self.hist_zh) > self.history:
				self.hist_zh.pop(0)
	
			self.hist_pinyin.append(self.label_pinyin.get_text())
			if len(self.hist_pinyin) > self.history:
				self.hist_pinyin.pop(0)

			self.hist_en.append(self.label_en.get_text())
			if len(self.hist_en) > self.history:
				self.hist_en.pop(0)

			if self.cur_pos + 1 < self.history:
				self.cur_pos = self.cur_pos + 1

		# We are browsing the histry
		else:
			self.cur_pos = self.cur_pos + 1
			self.label_zh.set_text(self.hist_zh[self.cur_pos])
			self.label_pinyin.set_text(self.hist_pinyin[self.cur_pos])
			self.label_en.set_text(self.hist_en[self.cur_pos])
			
	# Get previous entry
	def getprev(self):
		if self.cur_pos > 0:
			self.cur_pos = self.cur_pos - 1
		self.label_zh.set_text(self.hist_zh[self.cur_pos])
		self.label_pinyin.set_text(self.hist_pinyin[self.cur_pos])
		self.label_en.set_text(self.hist_en[self.cur_pos])

	# Display some information about chinux
	def about(self,action):
		dialog = gtk.MessageDialog(
				None,
				(gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT),
				gtk.MESSAGE_INFO, 
				gtk.BUTTONS_OK,
				"Chinux version " + chinux.VERSION + "\nGTK plugin version " + VERSION
			)
		dialog.run()
		dialog.destroy()

	# Create window and menus
	def create_ui(self):
        	ag = gtk.ActionGroup('WindowActions')
        	actions = [
        	    ('FileMenu', None, '_File'),
        	    ('Quit',     gtk.STOCK_QUIT, '_Quit', '<control>Q',
        	     'Quit application', self.destroy),
			('OptionMenu', None, '_Preferences'),
			('HSK level',None,'HSK level :'),
#			('Language',None,'Language :'),
			('Seed',None,'_Random seed',None,None,self.getseed),
        	    ('HelpMenu', None, '_Help'),
        	    ('About',    None, '_About', None, 'About application',
        	     self.about),
        	    ]
        	ag.add_actions(actions)
		ag.add_radio_actions([
			('HSK1',None,'Level _1',None,None,0),
			('HSK2',None,'Level _2',None,None,1),
			('HSK3',None,'Level _3',None,None,2),
			('HSK4',None,'Level _4',None,None,3),
			('HSK5',None,'Level _5',None,None,4),
			('HSK6',None,'Level _6',None,None,5),
			('HSK7',None,'_Higher level',None,None,6),
		],0,self.changelevel)
		ag.add_toggle_actions([('MergeLevels',None,'_Merge levels',None,None,self.mergelevels)])
		ag.add_toggle_actions([('ShowLabels',None,'_Show Labels',None,None,self.showlabels)])
#		ag.add_radio_actions([
#			('English',None,'_English',None,None,0)
#		],0,self.changelang)
        	self.ui = gtk.UIManager()
        	self.ui.insert_action_group(ag, 0)
        	self.ui.add_ui_from_string(ui_string)

	# Main function
	def main(self):
		gtk.main()

	# Change the HSK level
	def changelevel(self,action,current):
		if current.get_active():
			self.level = current.get_current_value()
			print self.level

	# ??
	def showlabels(self,action):
		self.labels =  not self.labels
#		COMMENT RAFFRAICHIR JUSTE LES LABELS ???

	# Merge the current HSK level with lower ones
	def mergelevels(self,action):
		self.merge = not self.merge 

	# Change the language of definitions
#	def changelang(self,action):
#		print ""

	def responseToDialog(entry, dialog, response):
#	        dialog.response(response)
		print ""

	# Change the random seed
	def getseed(self,action):
		# Create a dialog box
		dialog = gtk.Dialog(title=None,parent=None,flags=0,buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OK,gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		# Add text to the dialog box
		label = gtk.Label('Enter new seed :')
		dialog.vbox.pack_start(label,True,True,0)
		label.show()
		# Add text field
		seed = gtk.Entry()
		seed.connect("activate",self.responseToDialog,dialog,gtk.RESPONSE_OK)
		dialog.vbox.pack_start(seed,True,True,0)
		# Launch dialog box
		dialog.show_all()
		dialog.run()
		zeseed = seed.get_text()
		seed.destroy()
                print zeseed
#		hbox = gtk.HBox()
#		hbox.pack_start(gtk.Label("Seed :"),False,5,5)
#		hbox.pack_end(seed)
#		seed.connect('activate',response

	



# Let's go !
if __name__ == "__main__":
	base = gtkgui()
	base.main()






