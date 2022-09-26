from flask import Flask, request

from main import calculadoraFrete

app = Flask("API REST")


@app.route("/calculaFrete", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()

    altura = []
    largura = []
    peso = []
   
    altura.append(body.get("dimensao").get("altura"))
    largura.append(body.get("dimensao").get("largura"))
    peso.append(body.get("peso"))


    medidas = calculadoraFrete(altura,largura,peso)
    return medidas


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response
 


app.run()