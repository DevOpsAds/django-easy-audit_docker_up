# Generated by Django 4.2.11 on 2024-04-17 23:25

import alack_cookiecutter_1_01_audit.users.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', alack_cookiecutter_1_01_audit.users.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='username'),
        ),
    ]
