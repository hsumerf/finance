from cs50 import SQL
import sys



db = SQL("sqlite:///finance.db")

# Names in Ascending or by sum up all cash columns of the same username
# rows = db.execute("SELECT username, SUM(cash) FROM users GROUP BY username")
# for row in range(len(rows)):
#     print(rows[row])
#rows = db.execute("SELECT symbol,sharename,num_of_shares,price,total FROM hist WHERE userid='umer2'")
# rows = db.execute("""SELECT name,symbol, SUM(shares),price,total
#     FROM hist
#     WHERE userid = 'umer2'
#     GROUP BY NAME
#     """)
# rows = db.execute("SELECT username FROM users WHERE id=108")
# name = rows[0]['username']
# rows = db.execute("""SELECT SUM(total)
#      FROM hist
#      WHERE userid = 'umer2'
#      """)
# name = 'umer3'
# rows = db.execute("SELECT * FROM users WHERE username = :name ",name=name)
# print(rows[0]['cash'])
# sum_result = db.execute("""SELECT SUM(total) as total
#     FROM hist
#     WHERE userid =:userid
#      """,
#      userid = name)
# print(sum_result[0]['total'])
# all_sum = sum_result[0]['total'] + rows[0]['cash']
# print(all_sum)

# rows = db.execute("SELECT username FROM users WHERE username=:user_id",user_id = 'umer')
# user_name = rows[0]['username']
# symbols_rows = db.execute("SELECT symbol FROM hist WHERE userid = :userid",userid=user_name)
# print(symbols_rows[0])
# all symbol rows
# user_name = rows[0]['username']
# print(user_name)
# symbols_rows = db.execute("SELECT symbol FROM hist WHERE userid = :userid GROUP BY NAME",userid=user_name)
# print(symbols_rows)
#


from helpers import apology, login_required, lookup, usd,lookme

# value = lookme('NFLX')
# print(value['price'])
# print(value)
# rows = db.execute("SELECT symbol,shares,price,timedate FROM hist WHERE userid = :user_name",user_name = 'ume')
# print(rows[0])
str = "abc5"
print(str.isalpha())