# Generated by Django 5.0.3 on 2024-04-09 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_education_specialization'),
        ('programming', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='projects',
        ),
        migrations.AddField(
            model_name='publication',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experienceactivity',
            name='programming_tools',
            field=models.ManyToManyField(blank=True, related_name='experience_activities', to='programming.programmingtool'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]