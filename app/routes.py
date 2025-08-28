from flask import Blueprint, request, jsonify
from app.models import db, Subject, Review

bp = Blueprint('routes', __name__)

@bp.route('/v0/reviews', methods=['POST'])
def agregar_resena():
    try:
        body = request.get_json()
        if body and "materia" in body and "resena" in body:
            subject_json = body["materia"]
            review_json = body["resena"]

            if not subject_json.strip():
                return jsonify({"error": "El campo 'materia' no puede estar vacio"}), 400

            if not review_json.strip():
                return jsonify({"error": "El campo 'review' no puede estar vacio"}), 400

            subject = Subject.query.filter_by(name=subject_json).first()
            if not subject:
                subject = Subject(name=subject_json)
                db.session.add(subject)
                db.session.commit()

            review = Review(subject_id=subject.id, review=review_json)
            db.session.add(review)
            db.session.commit()

            return jsonify({
                "id": review.id,
                "materia": subject.name,
                "resena": review.review
            }), 201
        else:
            return jsonify({"error": "Payload invalido. Se requieren los campos 'materia' y 'resena'"}), 400
    except Exception:
        return jsonify({"error": "Error procesando el payload"}), 400
