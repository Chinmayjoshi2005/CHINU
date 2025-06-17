from django.db import models


class Register(models.Model):  # Renamed from 'register'
    regid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    course = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    status = models.IntegerField()
    role = models.CharField(max_length=30)
    info = models.CharField(max_length=30)
    verification_token = models.CharField(max_length=32, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    
    
# class Sharenotes(models.Model):
#     docid=models.AutoField(primary_key=True)
#     title=models.CharField(max_length=50)
#     category=models.CharField(max_length=50)            
#     description=models.CharField(max_length=500)
#     filename=models.CharField(max_length=100)
#     uid=models.CharField(max_length=50)
#     info=models.CharField(max_length=50)



class Sharenotes(models.Model):
    docid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)            
    description = models.CharField(max_length=500)
    filename = models.FileField(upload_to='notes/')  # 🔁 FIXED HERE!
    uid = models.CharField(max_length=50)
    info = models.CharField(max_length=50)


class Payment(models.Model):
    txnid=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=50)
    amt=models.CharField(max_length=50)            
    info=models.CharField(max_length=50)