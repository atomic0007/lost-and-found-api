from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    report_type = models.CharField(max_length=10, choices=[('lost', 'Lost'), ('found', 'Found')])
    date_time = models.DateTimeField()
    contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
