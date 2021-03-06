from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html")

@app.route('/start_page')
def start_page():
    return render_template("start_page.html")

@app.route('/pen')
def pen():
    return render_template("pen.html")

@app.route('/shirt')
def shirt():
    return render_template("shirt.html")

@app.route('/mouse')
def mouse():
    return render_template("mouse.html")

if __name__ == '__main__':
    app.run(debug=True)