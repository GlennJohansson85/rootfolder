# ======================================
# TESTS.PY
# ======================================
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog_app.models import Post, Comment

class BlogAppViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()

    def test_user_registration_view(self):
        response = self.client.get(reverse('user_registration'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_view(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_category_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('post_category', args=['category_name']))
        self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)


    def test_delete_post_view(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            user=self.user
        )
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete_post', kwargs={'post_id': post.id}))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect to 'home'

    def test_comment_view(self):
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            user=self.user
        )
        self.client.force_login(self.user)
        response = self.client.post(reverse('comment', kwargs={'post_id': post.id}), {'text': 'Test Comment'})
        self.assertEqual(response.status_code, 200)

