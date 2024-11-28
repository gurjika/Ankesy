from django.db import models

# Create your models here.


class ScamType(models.TextChoices):
    PRIZE = 'PRZ', 'Prize'
    PHISHING = 'PHI', 'Phishing'
    TECH_SUPPORT = 'TSP', 'Tech Support Scam'
    ROMANCE = 'ROM', 'Romance Scam'
    INVESTMENT = 'INV', 'Investment Fraud'
    CHARITY = 'CHA', 'Fake Charity'
    LOTTERY = 'LOT', 'Lottery Scam'
    IMPOSTER = 'IMP', 'Imposter (e.g., posing as a family member or friend)'
    JOB = 'JOB', 'Fake Job Offer'
    DELIVERY = 'DEL', 'Fake Delivery Notice'
    GOVERNMENT = 'GOV', 'Fake Government Request'



class Report(models.Model):
    opened = models.BooleanField()
    id_number = models.BooleanField(null=True)
    credit_card = models.BooleanField(null=True)
    address = models.BooleanField(null=True)
    phone_number = models.BooleanField()
    email = models.BooleanField(null=True) 
    bank_account = models.BooleanField(null=True) 
    password = models.BooleanField(null=True) 
    social_media = models.BooleanField(null=True) 
    medical_info = models.BooleanField(null=True)  
    personal_photos = models.BooleanField(null=True)  

    parent_email = models.EmailField()


    type = models.CharField(
        max_length=3, 
        choices=ScamType.choices
    )



