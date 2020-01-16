from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HealthProfessional(models.Model):
    """Represents details of a health professional"""
    name = models.CharField(max_length=70)
    designation = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='IN')
    email_id = models.EmailField(blank=True, default='')
    remarks = models.TextField(default='', blank=True)

    def __str__(self):
        return f'HealthProfessional(name={self.name}, designation={self.designation}, location={self.location}, ' \
               f'phone_number={self.phone_number}, email_id={self.email_id}, remarks={self.remarks})'

    @classmethod
    def create(cls, name: str, designation: str, location: str, phone_number: str, email_id: str = '',
               remarks: str = ''):
        return cls(name, designation, location, phone_number, email_id, remarks)
