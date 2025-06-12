from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)

    def __str__(self):
        return self.email

# Guard model
class Guard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    skills = models.TextField()
    guardImage = models.ImageField(upload_to='guards/', null=True, blank=True)
    availability_status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')],
        default='Available'
    )

    def __str__(self):
        return self.user.first_name or self.user.email

# Service model
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    serviceIcon = models.ImageField(null=True)

    def __str__(self):
        return self.service_name

# Booking model
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.user.first_name or self.user.email


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name