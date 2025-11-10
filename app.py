from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    msg = dados.get("mensagem", "")
    resposta = f"Gismo JJ respondeu: [mensagem invertida] ({msg[::-1]})"
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(port=5000)
