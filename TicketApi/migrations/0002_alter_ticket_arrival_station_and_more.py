# Generated by Django 4.2.8 on 2023-12-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='arrival_station',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='arrival_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='departure_station',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='departure_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passenger_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passenger_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='train_class',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
