# Generated by Django 4.2.7 on 2023-11-17 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_roomdetails_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomdetails',
            old_name='price',
            new_name='price_0',
        ),
        migrations.AddField(
            model_name='roomdetails',
            name='price_100',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roomdetails',
            name='price_30',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roomdetails',
            name='price_50',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_details', to='main.room'),
        ),
    ]