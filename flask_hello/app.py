#Flask Hello WOrld!

#importing flask
from flask import Flask

# creating application object 
app=Flask(__name__)


# using decorator pattern to link view function to a url

@app.route("/")
@app.route("/hello")

# define view using a function that returns a string

def hello_world():
	return ("Hello, World")

# starts the development server using run() method

if __name__=="__main__":
	app.run()