# Generated by Django 3.2.8 on 2021-10-30 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_toolinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toolinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]