from django.db import models

class GarbageRequest(models.Model):
    location = models.CharField(max_length=255)
    request_date = models.DateField(auto_now_add=True)
    is_collected = models.BooleanField(default=False)

    def __str__(self):
        return f"Garbage Request #{self.id}"



class CompanyRegistrationModel(models.Model):
    company_name = models.CharField(max_length=255)
    company_contact_person = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField()
    company_phone_number = models.CharField(max_length=20, blank=True, null=True)
    company_ID = models.CharField(max_length=50, unique=True)
    company_description = models.TextField()
    company_password = models.CharField(max_length=128)

    def __str__(self):
        return self.company_name

