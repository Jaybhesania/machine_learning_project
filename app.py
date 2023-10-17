from flask import Flask

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def index():
    return "Hey, my name is JB and in love with Baby"


if __name__=="__main__":
    app.run(debug=True)