# Generated by Django 2.1.2 on 2018-10-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_quiz_times_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('i', 'In Progress'), ('r', 'In Review'), ('p', 'Published')], default='i', max_length=1),
        ),
    ]
