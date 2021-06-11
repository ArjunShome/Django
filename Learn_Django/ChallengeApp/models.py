from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Individual_Detail(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    User_Img = models.ImageField(upload_to='Profile_pic')
    Address = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    PinCode = models.IntegerField()
    MobileNumber = models.IntegerField(unique=True)
    Gender = models.CharField(max_length=1, choices=[('M','M'), ('F','F')])
    DOB = models.DateField()

    def __str__(self) -> str:
        return self.User.username

class Gadget(models.Model):
    GadgetType = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.GadgetType

class Individual_Gadget_Detail(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Type = models.ForeignKey(Gadget, on_delete=models.CASCADE)
    Brand = models.CharField(max_length = 20)
    Buy_Date = models.DateField()
    BoughtFrom = models.CharField(max_length=50)
    Price = models.FloatField()

    def __str__(self):
        return self.Brand
