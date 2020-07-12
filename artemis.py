
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
