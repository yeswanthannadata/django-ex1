from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Post
# Create your tests here.

#simple test case

# class SimpleTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(test='testing model')

    def test_test_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.test}'
        self.assertEqual(expected_object_name, 'testing model')