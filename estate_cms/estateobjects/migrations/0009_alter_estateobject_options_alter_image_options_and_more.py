# Generated by Django 5.0.2 on 2024-02-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estateobjects', '0008_bid_bidder_estateobject_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estateobject',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='estateobject',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
    ]