# Generated by Django 4.0.1 on 2022-11-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pricingrule_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='costumer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
