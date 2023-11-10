import unittest
from server import app, db, connect_to_db, User, Dashboard

class TestModels(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.drop_all()
        db.create_all()
        connect_to_db(app, db_uri=app.config['SQLALCHEMY_DATABASE_URI'])

    def tearDown(self):
        """Tear down the test environment"""
        db.session.remove()
        db.drop_all()

    def test_user_model(self):
        """Test the User model"""
        user = User(fname='John', lname='Doe', email='johndoe@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

        self.assertEqual(user.fname, 'John')
        self.assertEqual(user.lname, 'Doe')
        self.assertEqual(user.email, 'johndoe@example.com')
        self.assertEqual(user.password, 'password123')

    def test_dashboard_model(self):
        """Test the Dashboard model"""
        user = User(fname='John', lname='Doe', email='johndoe@example.com', password='password123')
        db.session.add(user)
        db.session.commit()

        dashboard = Dashboard(dashboard_title='My Dashboard', user=user)
        db.session.add(dashboard)
        db.session.commit()

        self.assertEqual(dashboard.dashboard_title, 'My Dashboard')
        self.assertEqual(dashboard.user, user)

if __name__ == '__main__':
    unittest.main()