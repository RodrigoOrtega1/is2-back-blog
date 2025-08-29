import unittest
from app import create_app, db

class GuardarPruebas(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_post_valido(self):
        payload = {
            "materia": "Matematicas",
            "resena": "Gran clase"
        }
        response = self.app.post('/v0/reviews', json=payload)
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        self.assertEqual(response_data["materia"], payload["materia"])
        self.assertEqual(response_data["resena"], payload["resena"])

    def test_post_invalido_faltan_campos(self):
        payload = {
            "resena" : "Gran clase"
        }
        response = self.app.post('v0/reviews', json=payload)
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertEqual(response_data["error"], "Payload invalido. Se requieren los campos 'materia' y 'resena'")

    def test_post_invalido_campos_vacios(self):
        payload = {
            "materia" : "",
            "resena" : ""
        }
        response = self.app.post('v0/reviews', json=payload)
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertIn("error", response_data)
    
    def test_post_invalido(self):
        response = self.app.post('/v0/reviews', headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertEqual(response_data["error"], "Error procesando el payload")

    def test_get_subjects(self):
        with self.app.app_context():
            from app.models import Subject
            db.session.add(Subject(name="Fisica"))
            db.session.commit()
        response = self.app.get('/v0/subjects')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(any(s["nombre"] == "Fisica" for s in data))

    def test_get_reviews(self):
        with self.app.app_context():
            from app.models import Subject, Review
            subject = Subject(name="Quimica")
            db.session.add(subject)
            db.session.commit()
            review = Review(subject_id=subject.id, review="Muy interesante")
            db.session.add(review)
            db.session.commit()
        response = self.app.get('/v0/reviews')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(any(r["materia"] == "Quimica" and r["resena"] == "Muy interesante" for r in data))


if __name__ == '__main__':
    unittest.main()