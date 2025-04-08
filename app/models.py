from django.db import models
import uuid
import os
def rename_image(instance, filename):
    """Rename the uploaded image file to a unique name."""
    ext = filename.split('.')[-1]  # Get file extension
    new_filename = f"{uuid.uuid4().hex}.{ext}"  # Generate a unique name
    return os.path.join('images/', new_filename)  # Specify the upload path
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=10)
    category=models.CharField(max_length=100)
    rating=models.FloatField(max_length=10)
    image=models.ImageField(upload_to=rename_image)
    description=models.TextField()
    def __str__(self):
        return self.name
# Create your models here.
