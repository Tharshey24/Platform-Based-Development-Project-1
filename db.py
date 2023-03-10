import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('WebApp.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists Comp(ID integer primary key autoincrement, Subject varchar(255), Issue varchar(255), Campus varchar(255), Description text)')
		self._db.commit()
	def Add(self, Subject, Issue, Campus, Description):
		self._db.execute('insert into Comp (Subject, Issue, Campus, Description) values (?,?,?,?)',(Subject,Issue,Campus,Description))
		self._db.commit()
		return 'Your issue has been submitted.'
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor
