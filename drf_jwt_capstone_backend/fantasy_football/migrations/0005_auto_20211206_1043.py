# Generated by Django 3.2.8 on 2021-12-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_football', '0004_injuryreport_playerteam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='injuryreport',
            name='UserPlayer',
        ),
        migrations.AddField(
            model_name='injuryreport',
            name='playerName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
