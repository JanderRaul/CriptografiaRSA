from flask import Flask, render_template
from flask.globals import request
app=Flask(__name__)

class RSA:
    def __init__(self, valorp, valorq, senha):
        self.valorp=valorp
        self.valorq=valorq
        self.senha=senha

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/valores', methods=["POST"])
def valores():
    entradas = RSA(
    request.form['valorp'],
    request.form['valorq'],
    request.form['senha'],)

    def primo(valor):
        cont = 0
        i = 0
        while (i <= int(valor)) or (cont < 2):
            i = i + 1
            x = int(valor) % i
            if x == 0:
                cont = cont + 1

        if cont <= 2:
            return True
        else:
            return False

    msg = []
    if (primo(entradas.valorp)):
        if (primo(entradas.valorq)):
            n=int(entradas.valorp)*int(entradas.valorq)
            z=(int(entradas.valorp)-1)*(int(entradas.valorq)-1)
            d=23
            mdc=6
            while d % mdc != 0 or z % mdc != 0:
                mdc = d
                while d % mdc != 0 or z % mdc != 0: 
                    mdc = mdc - 1

            e=6
            while (e*d)%z!=1:
                e=e+1
            alerta = "Calculos realizados com sucesso!!!"
            msg.append(str(alerta))

            text = entradas.senha
            ascii_values = [ord(character) for character in text]
            msg.append(str(ascii_values))

            RSAc = []
            for num in ascii_values:
                RSAc.append((num**e)%n)
            msg.append(str(RSAc))

            texto2 = []
            for num in RSAc:
                texto2.append((num**d)%n)

            senha = ''
            for char in texto2:
                senha = senha + chr(char)
            msg.append(senha)

        else:
            alerta = str(entradas.valorq) + " Não é um número primo!!!"
            msg.append(str(alerta))             
    else:
        alerta = str(entradas.valorp) + " Não é um número primo!!!"
        msg.append(str(alerta))        

    return render_template("index.html", entradas=msg)
app.run(debug=True)

