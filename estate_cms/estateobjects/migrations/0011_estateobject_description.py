# Generated by Django 5.0.2 on 2024-02-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estateobjects', '0010_alter_store_collection_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='estateobject',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
