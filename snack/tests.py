from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse
# Create your tests here.
class Snacktest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='mohamed',email='mogamed@gmail.com',
            password='12345'
        )
        self.snack = Snack.objects.create(
            title = 'hot dog',
            purchaser=5,

            reviewer = self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'hot dog')

    def test_detail_view(self):
        url = reverse('snack_detail',args=[self.snack.id])  
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_detail.html')


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




