from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/index")
def index():
    return "This is index"
if __name__=="__main__":
    app.run(debug=True)
