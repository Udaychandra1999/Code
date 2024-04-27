from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=["POST"])
def add():
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    res = n1+n2
    return render_template('result.html',result =res)

if __name__ == '__main__':
    app.run(debug=True)