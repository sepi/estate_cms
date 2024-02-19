# Generated by Django 5.0.2 on 2024-02-11 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estateobjects', '0007_contact_remove_bid_bidder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estateobjects.contact', blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estateobject',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='owner', to='estateobjects.contact'),
        ),
        migrations.AddField(
            model_name='estateobject',
            name='reserved_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='reserved_for', to='estateobjects.contact'),
        ),
    ]
