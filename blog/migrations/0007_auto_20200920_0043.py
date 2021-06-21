# Generated by Django 2.2.6 on 2020-09-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rawproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawproject',
            name='done',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='rawproject',
            name='link',
            field=models.URLField(blank=True, verbose_name="Project's GitHub Link"),
        ),
    ]
