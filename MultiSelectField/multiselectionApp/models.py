from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class MyModel(models.Model):
    OPTIONS = (
        ('option1', 'Option1'),
        ('option2', 'Option2'),
        ('option3', 'Option3'),
    )

    name = models.CharField(max_length=100)
    options = MultiSelectField(choices=OPTIONS)

    def __str__(self):
        return self.name
