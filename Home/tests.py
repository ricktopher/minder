from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Entry

class EntryTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test_email.com',
            password='secret'
        )

        self.entry = Entry.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        entry = Entry(title='A sample title')
        self.assertEqual(str(entry), entry.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.entry.get_absolute_url(), '/entry/1/')

    def test_entry_content(self):
        self.assertEqual(f'{self.entry.title}', 'A good title')
        self.assertEqual(f'{self.entry.author}', 'testuser')
        self.assertEqual(f'{self.entry.body}', 'Nice body content') 

    def test_entry_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_entry_detail_view(self):
        response = self.client.get('/entry/1/')
        no_response = self.client.get('/entry/100000/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'entry_detail.html')

    def test_entry_create_view(self):
        response = self.client.post(reverse('entry_new'), {
            'title':'New title',
            'body':'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_entry_update_view(self):
        response = self.client.post(reverse('entry_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })

        self.assertEqual(response.status_code, 302)

    def test_entry_delete_view(self): 
        response = self.client.post(
            reverse('entry_delete', args='1'))
        self.assertEqual(response.status_code, 302)