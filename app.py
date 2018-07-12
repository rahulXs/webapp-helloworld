from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "home page"

@app.route('/another')
def another():
    return 'another page'

if __name__=="__main__":
    app.run(debug=True)
