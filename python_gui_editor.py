#-*- coding: utf-8 -*- 

from Tkinter import *

import tkFileDialog

def ReadFile(filename):
	
	if filename != '':
		input_file = open(filename, 'r')
		array = input_file.readlines()
		lines = ''.join(array)
	else:
		lines = ''

	return lines

class OpenFileButton:

	def __init__(self, master):
		
		self.fram = Frame(master)
		self.fram.pack(side=TOP)

		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\'
		options['initialfile'] = 'myfile.txt'
		options['parent'] = master
		options['title'] = 'This is a title'

		self.master = master
		self.openedfilename = ''

	def openfile(self):

		self.openedfilename = tkFileDialog.askopenfilename(**self.file_opt)
		
		text = TextArea(self.master, self.openedfilename).return_text()
		FindButton(self.master, text)
		ChangeButton(self.master, text)
		SaveButton(self.master, text, 'final.txt')

class FindButton:
	#Find Button
	def __init__(self, master, text):
		
		self.fram = Frame(master)
		self.fram.pack(side=TOP)

	        self.label = Label(self.fram,text='Text to find:')
		self.label.pack(side=LEFT)
		
		self.edit = Entry(self.fram)
		self.edit.pack(side=LEFT, fill=BOTH, expand=1)
		self.edit.focus_set()
		
		self.butt = Button(self.fram, text='Find')
		self.butt.pack(side=LEFT)
		self.butt.config(command=self.find)

		self.count = 0
		self.countlabel = Label(self.fram,text='Count: ' + str(self.count))
		self.countlabel.pack(side=RIGHT)
		
		self.text = text

	def find(self):
		
		self.text.tag_remove('found', '1.0', END)
		s = self.edit.get()
		
		if s:
			idx = '1.0'
			while 1:
			    	idx = self.text.search(s, idx, nocase=1, stopindex=END)
			    	if not idx: break
			    	lastidx = '%s+%dc' % (idx, len(s))
			    	self.text.tag_add('found', idx, lastidx)
			    	idx = lastidx
			    	self.count = self.count + 1
			self.text.tag_config('found', foreground='red', underline=1)

		self.countlabel["text"] = 'Count: ' + str(self.count)
		self.count = 0
	    	self.edit.focus_set()

class ChangeButton:
	#Chnage Button
	def __init__(self, master, text):
			
		self.fram = Frame(master)		
		self.fram.pack(side=TOP)

		self.label = Label(self.fram,text='Text to change:')
		self.label.pack(side=LEFT)
		
		self.edit = Entry(self.fram)
		self.edit.pack(side=LEFT, fill=BOTH, expand=1)
		self.edit.focus_set()
		
		self.butt = Button(self.fram, text='Change')
		self.butt.pack(side=RIGHT)
		self.butt.config(command=self.change)
		
		self.text = text

	def change(self):

	    s = self.edit.get()
	    if s:
		idx = '1.0'
		while 1:
		    idx = self.text.search(s, idx, nocase=1, stopindex=END)
		    if not idx: break
		    lastidx = '%s+%dc' % (idx, len(s))
		    exchange = ''
		    for i in range(len(s)):
			    exchange = exchange + '*'
		    self.text.delete(idx, lastidx)
		    self.text.insert(idx, exchange)
		    idx = lastidx
	    self.edit.focus_set()

class SaveButton:
	#Save Button
	def __init__(self, master, text, filename):

		self.fram = Frame(master)
		self.fram.pack(side=TOP)

		self.butt = Button(self.fram, text='Save')
		self.butt.pack()
		self.butt.config(command=self.save)
		
		self.filename = filename
		self.text = text

	def save(self):

		final = self.text.get('1.0',END)
		output = open(self.filename, 'w')
		output.write(final.encode('utf-8'))
		output.close()

class TextArea:
	#TextArea
	def __init__(self, master, filename):
		
		self.text = Text(master)
		self.text.insert('1.0', ReadFile(filename))
		self.text.pack(side=BOTTOM, fill=BOTH, expand=1)
		
	def return_text(self):

		return self.text

class AskArea:

	def __init__(self, master):

		self.fram = Frame(master)
		self.fram.pack(side=TOP)

		self.newbutt = Button(self.fram, text='Open New File')
		self.newbutt.pack()
		self.newbutt.config(command=self.new)
	
		self.oldbutt = Button(self.fram, text='Open Exist File')
		self.oldbutt.pack()
		self.oldbutt.config(command=self.old)

		self.master = master

	def old(self):

		self.master.destroy()
		root = Tk()
		root.title("Python Gui Editor")
		OpenFileButton(root).openfile()

	def new(self):

		self.master.destroy()
		execute('newIn.txt', 'newOut.txt')

def execute(inputfile, outputfile):
	
	root = Tk()
	root.title("Python Gui Editor")

	text = TextArea(root, inputfile).return_text()
	FindButton(root, text)
	ChangeButton(root, text)
	SaveButton(root, text, outputfile)

	root.mainloop()

if __name__ == "__main__":

	root = Tk()
	root.title("Which one do you open?")
	root.minsize(300,50)
	
	AskArea(root)

	root.mainloop()

