# Generated by Django 2.0.6 on 2018-09-08 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_course_abc_to_mti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseold',
            name='speakers',
        ),
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]