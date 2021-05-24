from django.db import models

# Create your models here.
class Individual(models.Model):
    FirstName = models.CharField(max_length=20)
    SecondName = models.CharField(max_length=20)
    Mobile = models.IntegerField(unique=True)

    def __str__(self):
        return self.FirstName

class Gadget(models.Model):
    GadgetType = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.GadgetType

class Individual_Gadget_Detail(models.Model):
    Name = models.ForeignKey(Individual, on_delete=models.CASCADE)
    Type = models.ForeignKey(Gadget, on_delete=models.CASCADE)
    Brand = models.CharField(max_length = 20)
    Buy_Date = models.DateField()
    BoughtFrom = models.CharField(max_length=50)
    Price = models.FloatField()

    def __str__(self):
        return self.Brand
