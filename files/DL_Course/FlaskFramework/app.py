from flask import Flask

app = Flask(__name__) #Creates an instance of the Flask class which will be our WSGI app

@app.route("/") #decorator
def welcome(): #This function gets called when the route "/" is hit
    return "Welcome to the Flask Framework learning"

if __name__ == '__main__': #Entry point of any python file
    # app.run() # runs the app
    app.run(debug=True) # updates changes automatically without needing to restart the server