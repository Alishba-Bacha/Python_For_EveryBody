import _sqlite3

conn = _sqlite3.connect('email.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = input('Enter file: ')
if(len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From'):
        continue
    piece = line.split()
    email = piece[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(email, count)
                    VALUES(?, 1)''',(email, ))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?',
                    (email, ))
    
conn.commit()
#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0], row[1]))

cur.close()