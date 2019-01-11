from tkinter import *
import backend

win=Tk()

win.title("BOOK STORE")

titletext=Label(win,text="Title")
yeartext=Label(win,text="Year")
authortext=Label(win,text="Author")
isbntext=Label(win,text="ISBN")
titletext.grid(row=0,column=0)
yeartext.grid(row=1,column=0)
authortext.grid(row=0,column=2)
isbntext.grid(row=1,column=2)


############ SELECTING_CURSOR ##################

def get_select(event):
    index=t1.curselection()[0]
    selected_tuple=t1.get(index)
    global id
    id=selected_tuple[0]
    titlebox.delete(0,END)
    titlebox.insert(END,selected_tuple[1])
    authorbox.delete(0,END)
    authorbox.insert(END, selected_tuple[2])
    yearbox.delete(0,END)
    yearbox.insert(END, selected_tuple[3])
    isbnbox.delete(0,END)
    isbnbox.insert(END, selected_tuple[4])

################################################

 ################### VARIABLES #################
title=StringVar()
author=StringVar()
isbn=StringVar()
year=StringVar()
################################################


####################EXECUTABLE_FUNCTIONS########

def view_button():
    t1.delete(0,END)
    for row in backend.view():
        t1.insert(END,row)

def search_button():
    t1.delete(0,END)
    for row in backend.search(title.get(),author.get(),year.get(),isbn.get()):
        t1.insert(END,row)
    view_button()

def entry_button():
    backend.entry(title.get(),author.get(),year.get(),isbn.get())
    t1.delete(0,END)
    t1.insert(END,title.get(),author.get(),year.get(),isbn.get())
    view_button()

def update_button():
   backend.update(id,title.get(),author.get(),year.get(),isbn.get())
   view_button()

def delete_button():
    backend.delete(id)
    view_button()

#################################################

#_______________________ENTRY BOXES _______________
titlebox=Entry(win,textvariable=title)
yearbox=Entry(win,textvariable=year)
authorbox=Entry(win,textvariable=author)
isbnbox=Entry(win,textvariable=isbn)
titlebox.grid(row=0,column=1)
yearbox.grid(row=1,column=1)
authorbox.grid(row=0,column=3)
isbnbox.grid(row=1,column=3)

#__________________________________________________


#________________________BUTTONS_______________________

view=Button(win,text="View All",height=1,width=12,command=view_button)
search=Button(win,text="Search Entry",height=1,width=12,command=search_button)
add=Button(win,text="Add Entry",height=1,width=12,command=entry_button)
update=Button(win,text="Update Selected",height=1,width=12,command=update_button)
delete=Button(win,text="Delete Selected",height=1,width=12,command=delete_button)
close=Button(win,text="Close",height=1,width=12,command=win.destroy)
view.grid(row=2,column=3)
search.grid(row=3,column=3)
add.grid(row=4,column=3)
update.grid(row=5,column=3)
delete.grid(row=6,column=3)
close.grid(row=7,column=3)

#__________________________________________________

t1=Listbox(win,height=9,width=35)
t1.grid(row=2,column=0,columnspan=2,rowspan=6)
s1=Scrollbar(win)
s1.grid(column=2,row=2,rowspan=6)
t1.configure(yscrollcommand=s1.set)
s1.configure(command=t1.yview)
t1.bind('<<ListboxSelect>>',get_select)

win.mainloop()