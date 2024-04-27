from flask import Flask, render_template ,request

app = Flask(__name__,template_folder='templates')


@app.route('/',methods = ['GET','POST'])
def index():
    res = None
    if request.method == 'POST':
        n1 = int(request.form['num1'])
        n2 = int(request.form['num2'])
        res = n1+n2

    return render_template('index.html',result = res)

if __name__ =="__main__":
    app.run(debug=True)