from django.db import models


# Create your models here.

class Test(models.Model):
    title = models.CharField('TITLE', max_length=100)
    create_date = models.DateTimeField('Create_DateTime', auto_now_add=True)
