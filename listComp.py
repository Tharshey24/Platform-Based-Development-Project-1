from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('List of Issues')
		tv = Treeview(self._root)
		tv.pack()
		tv.heading('#0', text='ID')
		tv.configure(column=('#Subject', '#Issue', '#Campus', '#Description'))
		tv.heading('#Subject', text='Subject')
		tv.heading('#Issue', text='Issue')
		tv.heading('#Campus', text='Campus')
		tv.heading('#Description', text='Description')
		cursor = self._dbconnect.ListRequest()
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Subject',row['Subject'])
			tv.set('#{}'.format(row['ID']),'#Issue',row['Issue'])
			tv.set('#{}'.format(row['ID']), '#Campus', row['Campus'])
			tv.set('#{}'.format(row['ID']),'#Description',row['Description'])
			
