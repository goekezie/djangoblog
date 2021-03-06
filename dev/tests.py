from django.test import TestCase
from .models import Post
from .models import Comment
from movie.models import MoviePost
from tech.models import TechPost

class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Tester", content="the Rolling Test")


    def Post_ws_Field_label(self):
        #The post can upload
        Post.objects.get(title="Tester")
        field_label = Post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_date_of_post(self):
        Post.objects.get(title="Tester")
        field_label = Post._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def title_name_max_length(self):
        Post.objects.get(title="Tester")
        max_length = Post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

class MoviePostTest(TestCase):
    def setUp(self):
        MoviePost.objects.create(title="Tester", content="the Rolling Test")


    def Post_ws_Field_label(self):
        #The post can upload
        MoviePost.objects.get(title="Tester")
        field_label = MoviePost._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_date_of_post(self):
        MoviePost.objects.get(title="Tester")
        field_label = MoviePost._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def title_name_max_length(self):
        MoviePost.objects.get(title="Tester")
        max_length = MoviePost._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

class TechPostTest(TestCase):
    def setUp(self):
        TechPost.objects.create(title="Tester", content="the Rolling Test")


    def Post_ws_Field_label(self):
        #The post can upload
        TechPost.objects.get(title="Tester")
        field_label = TechPost._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_date_of_post(self):
        TechPost.objects.get(title="Tester")
        field_label = TechPost._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def title_name_max_length(self):
        TechPost.objects.get(title="Tester")
        max_length = TechPost._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)