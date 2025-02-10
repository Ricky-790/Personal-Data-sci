from flask import Flask, render_template, request

app = Flask(__name__) #Creates an instance of the Flask class which will be our WSGI app

@app.route("/") #decorator
def welcome(): #This function gets called when the route "/" is hit
    return "<html><h1>Welcome to the Flask Framework learning</h1></html> <br> <html><h2>Welcome to the Flask Framework learning</h2></html>"

@app.route("/index", methods=['GET']) #Default is get request
def index_page():
    return render_template('index.html') #looks for index.html file in a templates folder

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/form", methods =['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form['name']
        return f'<h1>{name}</h1>'
    return render_template('form.html')


if __name__ == '__main__': #Entry point of any python file
    # app.run() # runs the app
    app.run(debug=True) # updates changes automatically without needing to restart the server