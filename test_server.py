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

    def test_dashboards_route(self):
        with self.app.session_transaction() as session:
            session['user_id'] = 1
        response = self.app.get('/dashboards')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Dashboards', response.data)

    def test_create_dashboard_route(self):
        with self.app.session_transaction() as session:
            session['user_id'] = 1
        response = self.app.post('/create-dashboard', data=dict(
            title='New Dashboard',
            language='Python'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New Dashboard', response.data)

    def test_delete_dashboard_route(self):
        with self.app.session_transaction() as session:
            session['user_id'] = 1
        response = self.app.post('/delete-dashboard', data=dict(
            dashboard_id=1
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Dashboard 1', response.data)

    def test_edit_dashboard_route(self):
        with self.app.session_transaction() as session:
            session['user_id'] = 1
        response = self.app.post('/edit-dashboard', data=dict(
            dashboard_id=1,
            title='New Title'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New Title', response.data)


if __name__ == '__main__':
    unittest.main()