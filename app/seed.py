from app import create_app, db
from app.models import Subject, Review

def seed():
    materias = [
        "Algoritmos", "Redes de Computadoras", "Inteligencia Artificial",
        "Sistemas Operativos", "Ingeniería de Software", "Estructuras Discretas"
    ]
    for nombre in materias:
        if not Subject.query.filter_by(name=nombre).first():
            db.session.add(Subject(name=nombre))
    db.session.commit()

    subject = Subject.query.filter_by(name="Algoritmos").first()
    if subject and not Review.query.filter_by(subject_id=subject.id).first():
        review = Review(subject_id=subject.id, review="Lorem ipsum dolor sit amet")
        db.session.add(review)
        db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed()