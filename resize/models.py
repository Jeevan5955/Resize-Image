from django.db import models
from PIL import Image

# Create your models here.


class Resize(models.Model):
    Image = models.ImageField(upload_to='pics', blank=False, null=False)
    Width = models.BigIntegerField(blank=False, null=False,)
    Height = models.BigIntegerField(blank=False, null=False,)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Image.path)
        output_size = (self.Width, self.Height)
        img.thumbnail(output_size)
        img.save(self.Image.path)
