# Generated by Django 2.2 on 2019-07-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190721_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
