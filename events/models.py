from django.db import models

class RequestModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.id} - {self.name} - {self.email}'
