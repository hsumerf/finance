from cs50 import SQL
import sys

db = SQL("sqlite:///finance.db")
# phpliteadmin command but not working in python
#INSERT INTO "users" ("id","username","hash") VALUES (NULL,'umer','umr')
user='final'
hashed='ab'
#correct  command
#db.execute("INSERT INTO users (username,hash) VALUES (:username,:hash)",username=user,hash='abc')
# id is incrementing by itself


#rows = db.execute("SELECT * FROM Album")
#db.execute("INSERT INTO users ("id","username","hash") VALUES (NULL,'ali','hashed')")
#db.execute("INSERT INTO "users" ("id","username","hash") VALUES (NULL,'umer','hash')")"
#rows = db.execute("SELECT * FROM users WHERE username=:username",{'username':'ali'})

    #it will check if the user is in database or not
#name = db.execute("SELECT cash FROM users WHERE username=:username",username='umer')
#if len(name)!=0:
    #print(name[0]['cash'])
# rows = db.execute("SELECT cash from users Where id=:userid",userid=session["user_id"])

# rows = db.execute("SELECT * from users Where id=:user",user=103)
# if len(rows)!=0:
#     bal = rows[0]['cash']
#     print(bal)
id = 2
shares = 3
pershare = 10.53

# db.execute("""INSERT INTO full_purchase (userid,num_of_shares,share,total)
#         VALUES (:userid,:num_of_shares,:share,:total)"""
#         ,userid = id,
#         num_of_shares = shares,
#         share = pershare,
#         total = shares * pershare)

#db.execute("ALTER TABLE full_purchase RENAME TO TempOldTable")

#CREATE TABLE my_purchase (name TEXT, COLNew {type} DEFAULT {defaultValue}, qty INTEGER, rate REAL);
db.execute("""CREATE TABLE hist (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,userid TEXT NOT NULL,sharename TEXT NOT NULL,
symbol TEXT NOT NULL, num_of_shares INTEGER NOT NULL,share REAL NOT NULL, total REAL NOT NULL, time
DATETIME NOT NULL DEFAULT CURRENT_TIME, date DATETIME NOT NULL DEFAULT CURRENT_DATE, timedate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP) """)



#db.execute("INSERT INTO "users" ('id',"username",'hash') VALUES ('NULL','ali','abc')
#rows = db.execute("SELECT * FROM users WHERE username=:username",{'username':'ali'})
#rows = db.execute(f"SELECT * FROM 'Album' WHERE Title ='{sys.argv[1]}' ")
#for row in rows:
# else:
#     print('oh')
#print(sys.argv[1])