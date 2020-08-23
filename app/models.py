from django.db import models

# Create your models here.
class profile(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    AlternateMobileno = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode  = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)


class check(models.Model):
    Otp = models.IntegerField()


class user(models.Model):
    UserId =  models.ForeignKey(profile,on_delete=models.CASCADE)
    Email = models.CharField(max_length=50)
    Firstname = models.CharField(max_length=50)


class shippingaddress(models.Model):
    UserId = models.ForeignKey(profile,on_delete=models.CASCADE)
    Address1 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode  = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)

class products(models.Model):
    Pname = models.CharField(max_length=100)
    Pcategory = models.CharField(max_length=50)
    Psize = models.CharField(max_length=50)
    Ptype = models.CharField(max_length=50)
    Pprice = models.IntegerField()
    Pcolor = models.CharField(max_length=50)
    Pimage = models.ImageField(upload_to="image")
