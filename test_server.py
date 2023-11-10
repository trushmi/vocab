import unittest
from server import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  
        self.assertIn('/login', response.headers['Location']) 
    
    def test_login(self):
        self.app.post('/login', data=dict(
            email='john@example.com',
            password='password123'
        ), follow_redirects=True)

    def test_logout(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have been logged out', response.data)


if __name__ == '__main__':
    unittest.main()