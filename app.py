from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def f():
    if request.method == 'POST':
        password = request.form['password']
        return f"Your password contains {len(password)} characters!"
    return render_template('index.html')

@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        fname = request.form['fname']
        return f"Hello {fname}!"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)