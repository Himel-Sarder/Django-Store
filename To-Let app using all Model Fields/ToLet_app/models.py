from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='property_images/')
    is_available = models.BooleanField(default=True)
    price = models.IntegerField()
    size = models.FloatField()
    property_type = models.CharField(max_length=20, choices=[('flat', 'Flat'), ('house', 'House'),('office','Office')])
    # amenities = models.CharField(max_length=100, choices=[('gym', 'Gym'), ('pool', 'Pool'), ('garden', 'Garden')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
