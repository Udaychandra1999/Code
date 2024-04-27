from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    greeting= "Hello world"
    return render_template('index.html', greeting = greeting)

if __name__ == '__main__':
    app.run(debug=True)
