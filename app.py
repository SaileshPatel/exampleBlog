#Imports for all the bits we'll need
from flask import Flask, render_template, request, redirect, url_for
import time
import datetime

#Creates an App Object
app = Flask(__name__)

#Turns debugging on so that we get useful debug errors to use
app.debug = True


#So we don't have to worry about working with databases yet I have mocked you up one here that will do the job (very badly)

DB = []
# Use this function to add to the "database"
def addToDB(entry):
	global DB
	DB.append(entry)

#Use this function to retrieve from the database
#field_name and field value should be strings, just_one is a boolean indicating if you want one or more results returned
def getFromDB(field_name, field_value, just_one):
	matches = []
	for entry in DB:
		if entry[field_name] == field_value:
			if just_one == True:
				return [entry]
			else:
				matches.append(entry)
	return return_list


		



@app.route("/", methods=["GET"]) #This the is the URL that we will be directed to and what methods can access it
def index():
	#You could put more code in here to do complex things
	return render_template("index.html",db=DB) #but we just want to serve back this template from the "templates" folder



@app.route("/posts/new", methods=["GET"])
def postsNew():
	entryJson = {"title":request.args['title'], "body":request.args['body'], "time":datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')}
	#not doing any validation
	addToDB(entryJson)
	print DB
	return redirect('/')

	




#runs the app 
if __name__ == "__main__":
	app.run()
