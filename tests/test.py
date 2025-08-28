import unittest
from app import create_app

class GuardarPruebas(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

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

if __name__ == '__main__':
    unittest.main()