from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "this is our first application"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=2000)
