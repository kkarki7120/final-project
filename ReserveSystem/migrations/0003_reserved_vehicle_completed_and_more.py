# Generated by Django 4.1.7 on 2023-05-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReserveSystem', '0002_alter_reserved_vehicle_payment_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserved_vehicle',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reserved_vehicle',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
