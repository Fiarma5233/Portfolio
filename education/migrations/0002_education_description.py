# Generated by Django 5.1.6 on 2025-02-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
