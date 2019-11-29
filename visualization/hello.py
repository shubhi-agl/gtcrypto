from flask import Flask, render_template, request
app = Flask(__name__, template_folder="/Users/shubhi/Bitcoin/visualization/views/")


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello/<string:name>/", methods=['GET', 'POST'])
def hello(name):
    quote = "lalala"
    if request.method == 'GET':
        return render_template("test.html", **locals())
    else:
        node_id = request.form['node_id']
        return render_template("results.html", **locals())


if __name__ == "__main__":
    app.run()
