from django.db import models

class RequestModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f'{self.id} - {self.name} - {self.email}'
