# Generated by Django 5.1.3 on 2024-11-24 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_borrowhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BorrowHistory',
        ),
    ]
