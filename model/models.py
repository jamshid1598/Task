from django.db import models

class Model_3d(models.Model):
    name = models.CharField(max_length=20)
    model = models.FileField(upload_to="models")
    img = models.ImageField(upload_to="pics")
    price = models.IntegerField()

    def __str__(self):
        return self.name