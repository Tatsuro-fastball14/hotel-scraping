from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/test/<username>')
def hello_world(username=None):
    return render_template('test.html', username=username)

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()