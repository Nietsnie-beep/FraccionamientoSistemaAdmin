# Generated by Django 3.0.5 on 2023-05-02 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20230428_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bloqueo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='house_notes',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
