from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

connect = sqlite3.connect('persistencia.sqlite3')
connect.execute(
    "CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)"
)
connect.execute(
    "CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, subject_id INTEGER NOT NULL, \
    review TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (subject_id) REFERENCES subjects(id))"
)

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
            
            with sqlite3.connect("persistencia.sqlite3") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT OR IGNORE INTO subjects (name) VALUES (?)", (subjects,))
                cursor.execute("SELECT id FROM subjects WHERE name = ?", (subjects,))
                subject_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO reviews (subject_id, review) VALUES (?, ?)", (subject_id, review))
                conn.commit()

            return jsonify({"message": "Resena guardada", "Resena": body}), 201
        else:
            return jsonify({"error": "Payload invalido. Se requieren los campos 'materia' y 'resena'"}), 400
    except Exception:
        return jsonify({"error": "Error procesando el payload"}), 400

if __name__ == "__main__":
    app.run(debug=True)