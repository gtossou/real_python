#app config for postgre https://postgresapp.com/documentation/configuration-python.html
#blog.py - controller

#imports

from flask import Flask, render_template, request,session, flash, redirect, \
url_for,g
import psycopg2

#database config 
DBNAME="postgres"
USERNAME="postgres"
PASS="postgres"
PORTN=5433
HOSTNAME="localhost"

app=Flask(__name__)

# pulls in app confiuration by looking for uppercase variable
app.config.from_object(__name__)

#function used for connecting to database

def connect_db():
	try:
	    conn=psycopg2.connect(dbname=DBNAME,password=PASS,user=USERNAME,host=HOSTNAME,port=PORTN)
	except:
		print("connection failed")

	return conn;

@app_route("/")
def login():
	return render_template("login.html")

@app_route("/main"):
	def main():
		return render_template("main.html")
		
if __name__=="__main__":
	app.run(debug=True)