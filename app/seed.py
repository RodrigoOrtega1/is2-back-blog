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

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed()