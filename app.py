from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v0/elements', methods=['POST'])
def agregar_resena():
    try:
        body = request.get_json()
        if body:
            return jsonify({"message": "Resena guardada", "Resena": body}), 201 #TODO: esto cambiara con la persistencia
        else:
            return jsonify({"error": "Payload invalido"}), 400
    except Exception:
        return jsonify({"error": "Payload invalido"}), 400

if __name__ == "__main__":
    app.run(debug=True)