# Generated by Django 4.0.6 on 2022-09-15 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_subjects_num_attended'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('students', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.student')),
                ('subject', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.subjects')),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
