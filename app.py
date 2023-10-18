from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def index():
    return "Hey, this is my first ML Project"


if __name__=="__main__":
    app.run(debug=True)