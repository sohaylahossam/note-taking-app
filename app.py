#import framework for creating web apps and the library used to connect to MariaDB database
from flask import Flask, request, render_template
import pymysql
from datetime import datetime

# initializing flask app
app = Flask(__name__)
# use connect function to connect to MariaDB database 
conn = pymysql.connect(host="localhost", user="note_user", password="StrongPass123!", db="notes_db")

# Define a route for the homepage (/) that accepts both GET and POST requests
@app.route("/", methods=["GET", "POST"])


def index():
    # if user submits a note , get the note the user typed and then insert it into database
    if request.method == "POST":
        note = request.form["note"]
        with conn.cursor() as cur:
            cur.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
        conn.commit()

    # Fetch all notes and their timestamps from the datavase

    with conn.cursor() as cur:
        cur.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")
        notes = cur.fetchall()

# display the notes using an HTML template 
    return render_template("index.html", notes=notes)

# calling the function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)