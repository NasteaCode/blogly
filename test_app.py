from app import app

class TestBloglyRoutes(TestCase):

    def test_homepage("/"):
        with app.client() as client:
        
        resp = client.get('/')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)

    def test_users("/users")
        with app.client() as client:
        
        resp = client.get('/users')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)

    def test_user_add_form("/users/new")
        with app.client() as client:
        
        resp = client.get('/')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>Create a user</h1>', html)

