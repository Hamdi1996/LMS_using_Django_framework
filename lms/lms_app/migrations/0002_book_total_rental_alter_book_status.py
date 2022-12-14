# Generated by Django 4.0.6 on 2022-08-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'Available'), ('rental', 'Rental'), ('sold', 'Sold')], max_length=55, null=True),
        ),
    ]
