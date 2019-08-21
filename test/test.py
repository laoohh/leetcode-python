from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)11')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)11')
