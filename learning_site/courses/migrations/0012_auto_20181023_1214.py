# Generated by Django 2.1.2 on 2018-10-23 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quizs',
            new_name='quiz',
        ),
    ]
