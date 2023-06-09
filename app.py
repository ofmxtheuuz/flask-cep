from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route('/<cep>')
def CEP(cep):
    cepReq = get(f"https://viacep.com.br/ws/{cep}/json/").json()
    return render_template("Home.html",cep=cepReq)


if __name__ == '__main__':
    app.run(Debug=True)
