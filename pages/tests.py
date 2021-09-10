from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post, BlogPost
# Create your tests here.

# simple test case

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


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(test='testing model')

    def test_view_url_existing_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_user_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser', email='test@email.com', password='testing@123')
        self.post = BlogPost.objects.create(
            title='testing blog', body='testing blog descc', author=self.user)

    def test_string_representation(self):
        post = BlogPost(title='A blog post')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'testing blog')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'testing blog descc')

    def test_post_list_view(self):
        resp = self.client.get(reverse('blog'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'testing blog descc')
        self.assertTemplateUsed(resp, 'blog.html')

    def test_post_detail_view(self):
        resp = self.client.get('/blog/1/')
        no_resp = self.client.get('/blog/1000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'testing blog')
        self.assertTemplateUsed(resp, 'post_detail.html')
