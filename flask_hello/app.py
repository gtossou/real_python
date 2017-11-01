#Flask Hello WOrld!

#importing flask
from flask import Flask

# creating application object 
app=Flask(__name__)


# error handling
app.config["DEBUG"] = True

# using decorator pattern to link view function to a url

@app.route("/")
@app.route("/hello")
def hello_world():
	return ("Hello, World")

@app.route("/test/<search_query>")
def search(search_query):
	return search_query
# define view using a function that returns a string

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael" :
		return "Hello, {}".format(name), 200
	else :
		return "Not Found", 404


# starts the development server using run() method

if __name__=="__main__":
	app.run()