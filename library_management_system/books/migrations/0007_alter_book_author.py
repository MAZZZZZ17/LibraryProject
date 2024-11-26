# Generated by Django 5.1.3 on 2024-11-26 11:49

import books.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_author_name_remove_book_authors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=books.models.get_default_author, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.author'),
        ),
    ]
