# Generated by Django 5.0.2 on 2024-02-10 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estateobjects', '0001_squashed_0004_alter_estateobject_asking_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='position',
        ),
    ]
