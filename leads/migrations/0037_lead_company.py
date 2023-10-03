# Generated by Django 4.2.4 on 2023-09-25 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0036_company_remove_lead_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to='leads.company'),
        ),
    ]
