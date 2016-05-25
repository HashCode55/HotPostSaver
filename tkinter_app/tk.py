from Tkinter import *
import tkMessageBox
import praw

# Code to add widgets will go here...
reddit = praw.Reddit(user_agent = "automator by /u/holybananas666")	
store = []
def fetch():
	subre = reddit.get_subreddit(sub_reddit.get())
	for submission in subre.get_hot(limit = 10):
		select.insert(END, str(submission))
		store.append(str(submission.selftext.encode('utf-8')))

def which_selected():
	return int(select.curselection()[0])

def onselect(evt):
	w = evt.widget
	index = int(w.curselection()[0])
	value = w.get(index)
	open_new = Toplevel(win)
	sc_bar = Scrollbar(open_new)
	sc_bar.pack(side = RIGHT, fill = Y)
	label = Label(open_new, text = store[index], yscrollcommand = sc_bar.set())
	label.pack()
	print 'You selected item %d: "%s"' % (index, value)

def make_window():
	global sub_reddit, num_to_fetch, select
	win = Tk()

	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text = "Name of the subreddit: ").grid(row = 0,  column = 0, sticky = W)
	sub_reddit = StringVar()
	name = Entry(frame1, textvariable = sub_reddit)
	name.grid(row = 0, column = 1, sticky = W)

	Label(frame1, text="Posts to fetch: ").grid(row=1, column=0, sticky=W)
    	num_to_fetch= StringVar()
    	phone= Entry(frame1, textvariable=num_to_fetch)
    	phone.grid(row=1, column=1, sticky=W)

    	frame2 = Frame(win, pady = 20)
    	frame2.pack()
    	b1 = Button(frame2,text=" Fetch", command = fetch)
    	b2 = Button(frame2,text="open")
    	b3 = Button(frame2,text="Save")
    	b1.pack(side=LEFT)
     	b2.pack(side=LEFT)
    	b3.pack(side=LEFT)

    	frame3 = Frame(win, pady = 10)
    	frame3.pack()
    	scroll = Scrollbar(frame3, orient=VERTICAL)
    	select = Listbox(frame3, yscrollcommand=scroll.set, height=6, width = 50)
    	select.bind('<<ListboxSelect>>', onselect)
    	scroll.config (command=select.yview)
    	scroll.pack(side=RIGHT, fill=Y)
    	select.pack(side=LEFT,  fill=BOTH, expand=1)
    	return win


win = make_window()
win.geometry("500x300")
win.title("Reddit Hot Posts!")
win.mainloop()

