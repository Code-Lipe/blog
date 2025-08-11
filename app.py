from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    posts = [
        {'titulo': 'Meu Primeiro Post', 'autor': 'João'},
        {'titulo': 'Aprendendo Python', 'autor': 'Maria'}
    ]
    return render_template("index.html", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)