from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd,lookme

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT username FROM users WHERE id=:user_id",user_id = session["user_id"])
    name = rows[0]['username']
    # name, symbol, sum of all shares,sum of total
    rows = db.execute("""SELECT name,symbol, SUM(shares) as shares,price,SUM(total) as total
    FROM hist
    WHERE userid = :userid
    GROUP BY NAME
    ORDER BY NAME""",
    userid = name)
    # sum of All amount of bought shares
    sum_result = db.execute("""SELECT SUM(total) as total
    FROM hist
    WHERE userid =:userid
     """,
     userid = name)
    sum_total = sum_result[0]['total'] # tuple convering into Dict and then in int
    cash_rows = db.execute("SELECT cash FROM users WHERE username =:userid ",userid = name )
    balance = cash_rows[0]['cash']
    if not sum_total:
        return render_template("index.html",rows=rows,balance=balance,total_cash=balance)
    #cash = amount remaining + Amount spent for shares
    total_cash = balance + sum_total
    return render_template("index.html",rows=rows,balance=balance,total_cash=total_cash)




    # return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method=="POST":
        if not request.form.get("symbol"):
            apology("blank symbol",400)
        symbol = request.form.get("symbol")
        value = lookup(symbol)
        #check return value
        if value is None:
            return apology("INVALID SYMBOL",400)
        if not request.form.get("shares"):
            return apology("MISSING SHARES",403)
        if request.form.get("shares").isnumeric()==False:
            return apology("Invalid shares",400)
        #print(type(request.form.get("shares")))
        num_of_shares = int(request.form.get("shares")) #returns is in string, type cast is must
        #print(type(num_of_shares))


            #check if it is less than 0 or it is numeric or it is int type
        if num_of_shares < 0:
            return apology("Invalid shares",400)
        current_price = value['price']
        symbol_name = value['name']
        rows = db.execute("SELECT * from users Where id=:userid",userid=session["user_id"]) #only the selected row will be selected because of condition(WHERE)
        cur_bal = rows[0]['cash']
        total_amount = num_of_shares*current_price
        if cur_bal<(total_amount):
            return apology("CAN'T AFFORD",400)

        db.execute("UPDATE users SET cash = :cur_bal - :total_amount WHERE username = :username",cur_bal=cur_bal,total_amount=total_amount,username = rows[0]['username'])
        db.execute("""INSERT INTO hist (userid,name,symbol,shares,price,total)
        VALUES (:userid,:sharename,:symbol,:num_of_shares,:price,:total)"""
        ,userid = rows[0]['username'],
        sharename = symbol_name,
        symbol = symbol,
        num_of_shares = num_of_shares,
        price = current_price,
        total = total_amount )
        return redirect("/")


    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    name_rows = db.execute("SELECT username FROM users WHERE id = :userid",userid = session["user_id"])
    name = name_rows[0]['username']
    rows = db.execute("SELECT symbol,shares,price,timedate as transacted FROM hist WHERE userid = :user_name",user_name = name)

    return render_template("history.html",rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("blank symbol",400)
        name = request.form.get("symbol")
        value = lookup(name)
        if value is None:
            return apology("invalid symbol",400)

        return render_template("quoted.html",value=value)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("blank username",400)

        if not request.form.get("password"):
            return apology("blank password",400)

        if request.form.get("password")!=request.form.get("confirmation"):
            return apology("MISMATCH PASSWORD", 400)

        rows = db.execute("SELECT * FROM users WHERE username=:username",username=request.form.get("username"))

        if len(rows)!=0:
             return apology("username taken",400)
        # elif (db.execute("SELECT * FROM users WHERE username=:username",username=request.form.get("username"))==request.form.get("username"):
        #     apology("same",403)

        user = request.form.get("username")
        hashed = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username,hash) VALUES (:username,:hash)",username=user,hash=hashed)
        return render_template("login.html")
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("MISSING SYMBOL",400)
        if not request.form.get("shares"):
            return apology("MISSING SHARES",400)
        symbol = request.form.get("symbol")
        value = lookup(symbol)
        if value is None:   #check if it returns value
            return apology("Missed lookup",400)
        num_of_shares = int(request.form.get("shares"))
        amount = value['price'] * num_of_shares
        #select current user from users database table
        name_in_rows = db.execute("SELECT username FROM users WHERE id=:user_id",user_id = session["user_id"])
        user_name = name_in_rows[0]['username']
        #select cash of current user
        rows = db.execute("SELECT cash FROM users WHERE username = :user_name",user_name = user_name)
        #after selling add amount in users cash
        db.execute("UPDATE users SET cash = :cash + :new_amount WHERE username = 'umer'",cash = rows[0]['cash'],new_amount = amount)
        symbols_rows = db.execute("SELECT symbol FROM hist WHERE userid = :user_name GROUP BY NAME",user_name=user_name)
        return render_template("sell.html",symbols_rows=symbols_rows)
    else:
        rows = db.execute("SELECT username FROM users WHERE id=:user_id",user_id = session["user_id"])
        user_name = rows[0]['username']
        symbols_rows = db.execute("SELECT symbol FROM hist WHERE userid = :user_name GROUP BY NAME",user_name=user_name)
        return render_template("sell.html",symbols_rows=symbols_rows)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
