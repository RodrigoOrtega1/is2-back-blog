import unittest
from app import app

class GuardarPruebas(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_post_valido(self):
        payload = {
            "title": "Resena",
            "content": "Gran clase"
        }
        response = self.app.post('/v0/elements', json=payload)
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        self.assertEqual(response_data["message"], "Resena guardada")
        self.assertEqual(response_data["Resena"], payload)

    def test_post_invalido(self):
        response = self.app.post('/v0/elements', headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertEqual(response_data["error"], "Payload invalido")

if __name__ == '__main__':
    unittest.main()