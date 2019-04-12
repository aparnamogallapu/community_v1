from django.db import models

class UserRegister(models.Model):
    block_name=models.CharField(max_length=5)
    flat_type=models.CharField(max_length=10)
    flat_no=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=100)
    occupation=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class UserPayment(models.Model):
    block_name=models.CharField(max_length=5)
    flat_no = models.CharField(max_length=5,primary_key=True)
    flat_type=models.CharField(max_length=5)
    total_amt = models.IntegerField()
    type_of_payment = models.CharField(max_length=50)
    date = models.DateField()

class Booking(models.Model):
    flat_no = models.CharField(max_length=10,primary_key=True)
    flat_type=models.CharField(max_length=5)
    block_name=models.CharField(max_length=3)
    name=models.CharField(max_length=50)
    booking_purpose = models.CharField(max_length=50)
    booking_date = models.DateField()
    email = models.EmailField(max_length=100)
    message=models.CharField(max_length=200)

class ElectricityBill(models.Model):
    amount=models.IntegerField()
    date=models.DateField(primary_key=True)

class WaterBill(models.Model):
    amount = models.IntegerField()
    date = models.DateField(primary_key=True)

class SalaryBill(models.Model):
    manager_name=models.CharField(max_length=50)
    manager_salary=models.DecimalField(max_digits=10,decimal_places=2)
    incharege1_name=models.CharField(max_length=50)
    incharege2_name=models.CharField(max_length=50)
    incharege3_name=models.CharField(max_length=50)
    incharege4_name=models.CharField(max_length=50)
    incharege1_salary=models.DecimalField(max_digits=10,decimal_places=2)
    incharege2_salary=models.DecimalField(max_digits=10,decimal_places=2)
    incharege3_salary=models.DecimalField(max_digits=10,decimal_places=2)
    incharege4_salary=models.DecimalField(max_digits=10,decimal_places=2)
    total_security=models.IntegerField()
    security_salary=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField(primary_key=True)
    # total_all_salary=models.DecimalField(max_digits=10,decimal_places=2,default=None)
    total_sal=models.DecimalField(max_digits=10,decimal_places=2,default=False)


class Complaint(models.Model):
    flat_no=models.CharField(primary_key=True,max_length=10)
    flat_type=models.CharField(max_length=10)
    block_name=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    complaint=models.CharField(max_length=500)
    date=models.DateField()