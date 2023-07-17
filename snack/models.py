from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse
class Snack(models.Model):
    title = models.CharField(max_length=255 , help_text='title name')
    purchaser = models.IntegerField()
    description = models.TextField(default="no desc available")
    reviewer = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-pk']

    def get_absolute_url(self):
        return reverse('snack_detail',args=[self.id])