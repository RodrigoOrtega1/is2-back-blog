from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v0/elements', methods=['POST'])
def agregar_resena():
    try:
        body = request.get_json()
        if body and "materia" in body and "resena" in body:
            subjects = body["materia"]
            review = body["resena"]

            if not subjects.strip():
                return jsonify({"error": "El campo 'materia' no puede estar vacio"}), 400

            if not review.strip():
                return jsonify({"error": "El campo 'review' no puede estar vacio"}), 400
            return jsonify({"message": "Resena guardada", "Resena": body}), 201  # TODO: Reemplazar con persistencia
        else:
            return jsonify({"error": "Payload invalido. Se requieren los campos 'materia' y 'resena'"}), 400
    except Exception:
        return jsonify({"error": "Error procesando el payload"}), 400

if __name__ == "__main__":
    app.run(debug=True)