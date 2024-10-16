# https://stackoverflow.com/questions/48552343/how-can-i-execute-a-python-script-from-an-html-button

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/left')
def left():
    print('Left arrow clicked')
    #return 'Click.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
