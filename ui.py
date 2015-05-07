#-*- coding: utf-8 -*- 

from Tkinter import *

def ReadFile(filename):

	input_file = open(filename, 'r')
	array = input_file.readlines()
	lines = ''.join(array)
	
	return lines

root = Tk()

fram = Frame(root)
Label(fram,text='Text to find:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Find')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

fram2 = Frame(root)
Label(fram2,text='Text to change:').pack(side=LEFT)
edit2 = Entry(fram2)
edit2.pack(side=LEFT, fill=BOTH, expand=1)
edit2.focus_set()
butt2 = Button(fram2, text='Change')
butt2.pack(side=RIGHT)
fram2.pack(side=TOP)

fram3 = Frame(root)
butt3 = Button(fram3, text='Save')
butt3.pack()
fram3.pack(side=TOP)

text = Text(root)
text.insert('1.0', ReadFile('edit.txt'))
text.pack(side=BOTTOM, fill=BOTH, expand=1)


def find():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='red', underline=1)
    edit.focus_set()

def change():
    s = edit2.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
	    exchange = ''
	    for i in range(len(s)):
		    exchange = exchange + '*'
	    text.delete(idx, lastidx)
	    text.insert(idx, exchange)
            idx = lastidx
    edit2.focus_set()

def save():
	final = text.get('1.0',END)
	output = open('final.txt', 'w')
	output.write(final.encode('utf-8'))
	output.close()

butt.config(command=find)
butt2.config(command=change)
butt3.config(command=save)
root.mainloop()

