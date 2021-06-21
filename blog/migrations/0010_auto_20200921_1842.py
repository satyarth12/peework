# Generated by Django 2.2.6 on 2020-09-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_submitform_submission_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitform',
            name='submission_count',
        ),
        migrations.AlterField(
            model_name='rawproject',
            name='link',
            field=models.URLField(max_length=500, verbose_name="Project's GitHub Link"),
        ),
    ]
