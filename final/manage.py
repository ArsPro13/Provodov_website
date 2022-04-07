from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("final/templates/index.html")

@app.route('/about_us')
def about_us():
    return render_template("final/templates/about_us.html")


@app.route('/catalog')
def catalog():
    return render_template("final/templates/catalog.html")



if __name__ == '__main__':
    app.run(debug=True)