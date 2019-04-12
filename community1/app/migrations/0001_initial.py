# Generated by Django 2.1.1 on 2018-12-14 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('flat_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('flat_type', models.CharField(max_length=5)),
                ('block_name', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('booking_purpose', models.CharField(max_length=50)),
                ('booking_date', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('flat_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('flat_type', models.CharField(max_length=10)),
                ('block_name', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('complaint', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricityBill',
            fields=[
                ('amount', models.IntegerField()),
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryBill',
            fields=[
                ('manager_name', models.CharField(max_length=50)),
                ('manager_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('incharege1_name', models.CharField(max_length=50)),
                ('incharege2_name', models.CharField(max_length=50)),
                ('incharege3_name', models.CharField(max_length=50)),
                ('incharege4_name', models.CharField(max_length=50)),
                ('incharege1_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('incharege2_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('incharege3_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('incharege4_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_security', models.IntegerField()),
                ('security_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('total_all_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('block_name', models.CharField(max_length=5)),
                ('flat_no', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('flat_type', models.CharField(max_length=5)),
                ('total_amt', models.IntegerField()),
                ('type_of_payment', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('block_name', models.CharField(max_length=5)),
                ('flat_type', models.CharField(max_length=10)),
                ('flat_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('occupation', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBill',
            fields=[
                ('amount', models.IntegerField()),
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
    ]