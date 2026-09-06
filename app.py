from flask import  Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET","POST" ])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        return render_template("cadastro_realizado.html", nome=nome , cpf=cpf)
    return render_template("Cadastro.html")

if __name__ == "__main__":
    app.run(debug = True)