# Generated by Django 4.0.6 on 2022-09-15 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_teacher_mat_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='num_attended',
        ),
    ]
