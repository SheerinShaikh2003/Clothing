# Generated by Django 5.0.1 on 2024-01-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_cusorders_delete_cusratingfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Mumbai', max_length=100),
        ),
    ]
