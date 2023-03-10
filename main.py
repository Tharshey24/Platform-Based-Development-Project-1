
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db import DBConnect
from listComp import ListComp

conn = DBConnect()
root = Tk()
root.geometry('600x285')
root.title('Safety/Maintenance Management')
root.configure(background='#AEB6BF')

style = Style()
style.theme_use('classic')
for elem in ['TLabel', 'TButton', 'TRadioutton']:
	style.configure(elem, background='#AEB6BF')

labels = ['Subject:', 'Issue:', 'Campus:', 'Description:']
for i in range(4):
	Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

BuList = Button(root, text='List of issues')
BuList.grid(row=4, column=1)
BuSubmit = Button(root, text='Submit Now')
BuSubmit.grid(row=4, column=2)

Subject = Entry(root, width=40, font=('Arial', 14))
Subject.grid(row=0, column=1, columnspan=3)
SpanIssue = StringVar()
Radiobutton(root, text='Maintenance', value='Maintenance', variable=SpanIssue).grid(row=1, column=1)
Radiobutton(root, text='Safety', value='Safety', variable=SpanIssue).grid(row=1, column=2)

SpanCampus = StringVar()
Radiobutton(root, text='Ritson', value='Ritson', variable=SpanCampus).grid(row=2, column=1)
Radiobutton(root, text='Steve Biko', value='Steve Biko', variable=SpanCampus).grid(row=2, column=2)
Radiobutton(root, text='M/L Sultan', value='M/L Sultan', variable=SpanCampus).grid(row=2, column=3)

Description = Text(root, width=35, height=5, font=('Arial', 14))
Description.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

def SaveData():
	msg = conn.Add(Subject.get(), SpanIssue.get(), SpanCampus.get(), Description.get(1.0, 'end'))
	Subject.delete(0, 'end')
	Description.delete(1.0, 'end')
	showinfo(title='Add Info', message=msg)

def ShowList():
	listrequest = ListComp()


BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

root.mainloop()
