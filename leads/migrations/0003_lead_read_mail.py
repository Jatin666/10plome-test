# Generated by Django 4.2.2 on 2023-08-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_priceentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='read_mail',
            field=models.BooleanField(default=False),
        ),
    ]
