# Generated by Django 3.2.8 on 2021-10-31 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]