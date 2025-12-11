# events/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    role = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    features = models.TextField()  # comma-separated features
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def feature_list(self):
        return [f.strip() for f in self.features.split(',')]
