import sqlite3

with open("candidates.txt", 'r') as candidates:
    lines = candidates.readlines()

candidate_list = []
for i in range(len(lines)):
    words = lines[i].split("|")
    words[-1] = str(words[-1]).replace("\n", "")
    candidate_list.append(words)


    
    
db = sqlite3.connect('Candidate.db')
cur = db.cursor()


cur.execute('PRAGMA  foreign_keys=1')

cur.execute('''drop TABLE if exists candidates''')

cur.execute('''CREATE TABLE  candidates ( id  integer  PRIMARY  KEY  NOT  NULL,
first_name TEXT, last_name TEXT,
middle_initial  TEXT, party TEXT  NOT  NULL)''')

for i in range(1, len(candidate_list)):
    cur.execute('''INSERT INTO candidates
    (id, first_name, last_name, middle_initial,party ) VALUES(?,?,?,?,?)''',[int(candidate_list[i][0])]+candidate_list[i][1:])
db.commit()
cur.execute('''select * from candidates''')
rows = cur.fetchall()
print(rows)





