# Generated by Django 3.2.8 on 2021-11-05 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-publish_date']},
        ),
    ]
