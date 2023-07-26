from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='mohamed', email='mohamed@gmail.com', password='12345'
        )
        self.client.login(username='mohamed', password='12345') 
        self.snack = Snack.objects.create(
            title='hot dog',
            purchaser=5,
            reviewer=self.user,
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'hot dog')

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_snack_list(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertContains(response, self.snack.title)

def test_create_view(self):
    url = reverse('snack_create')
    data = {
        "title": "hot dog", 
        "reviewer": self.user.id,
        "purchaser": 1
    }

    response = self.client.post(path=url, data=data, follow=True)
    self.assertTemplateUsed(response, 'snack_detail.html')
    self.assertEqual(len(Snack.objects.all()), 2)
    self.assertRedirects(response, reverse('snack_detail', args=[2]))
    new_snack = Snack.objects.get(id=2)
    self.assertEqual(new_snack.title, "new snack") 

    def test_update_view(self):
        url = reverse('snack_update', args=[self.snack.id])
        data = {
            "title": "beef",  
            "purchaser": self.snack.purchaser,
            "reviewer": self.snack.reviewer.id,
            "description": "yummy"  
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)  
        updated_snack = Snack.objects.get(id=self.snack.id)
        self.assertEqual(updated_snack.title, "beef")
        self.assertEqual(updated_snack.description, "yummy")

    def test_delete_view(self):
        url = reverse('snack_delete', args=[self.snack.id])
        response = self.client.get(url, follow=True)
        self.assertContains(response, f"Are you sure you want to delete {self.snack.title}")



