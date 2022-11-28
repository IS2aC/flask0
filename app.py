from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def portal():
	return render_template('portal.html')

@app.route("/validation", methods = ['GET', 'POST'])
def valid():
    name  = request.form.get('name')
    return render_template('valid.html', name = name)


if __name__ == "__main__":
    app.run(debug =True)



