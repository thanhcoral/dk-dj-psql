from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    