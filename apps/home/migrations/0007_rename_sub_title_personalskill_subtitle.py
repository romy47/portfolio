# Generated by Django 5.0.3 on 2024-04-09 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_personalskill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalskill',
            old_name='sub_title',
            new_name='subtitle',
        ),
    ]
