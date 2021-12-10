# Generated by Django 3.2.8 on 2021-12-09 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fantasy_football', '0008_alter_team_userplayer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentboard',
            name='User',
        ),
        migrations.RemoveField(
            model_name='team',
            name='UserPlayer',
        ),
        migrations.RemoveField(
            model_name='userplayer',
            name='User',
        ),
        migrations.AddField(
            model_name='commentboard',
            name='user',
            field=models.ForeignKey(blank=True, db_column='userId', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='userPlayer',
            field=models.ForeignKey(db_column='userPlayerId', null=True, on_delete=django.db.models.deletion.CASCADE, to='fantasy_football.userplayer'),
        ),
        migrations.AddField(
            model_name='userplayer',
            name='user',
            field=models.ForeignKey(blank=True, db_column='userId', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
