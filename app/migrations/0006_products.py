# Generated by Django 3.1 on 2020-08-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=100)),
                ('Pcategory', models.CharField(max_length=50)),
                ('Psize', models.CharField(max_length=50)),
                ('Ptype', models.CharField(max_length=50)),
                ('Pprice', models.IntegerField()),
                ('Pcolor', models.IntegerField()),
                ('Pimage', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
