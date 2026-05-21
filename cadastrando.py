from flask import Flask, request, jsonify

# Variável app -> Indicando que o sistema será via web
app = Flask(__name__)

#Lista que vai armazenar os usuários
usuarios = []

# Endpoint inicia
# Quando acessar
@app.route("/")
def inicio(): # def -> Seria uma função | GET - > Ler dados
    
    return "API funcionando"

#Estamos usando o método POST - Cria dados
@app.route("/usuarios", methods=['POST'] )
def cadastrar():
    
    #request -> recebe dados enviados pelo cliente
    #get -> Buscar | json -> formato de arquivo
    dados = request.get_json()
    # Criará um usuário novo
    # len(usuarios)+1 gera o id automático
    # Se a lista estiver vazia
    # len = 0
    # id = 1
    usuario = {
        "id": len(usuarios)+1,
        "nome": dados["nome"]
    }
    
    #Adicionar o usuário na lista
    usuarios.append(usuario)
    
    # Vai retorna o usário criado
    # jsonify -> Transforma resposta python em JSON
    # 201 = Criado com sucesso
    return jsonify(usuario), 201
    
    


# Rodando o sistema
if __name__ == "__main__":
    app.run(debug=True, port=5254)





