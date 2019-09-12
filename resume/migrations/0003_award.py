# Generated by Django 2.2 on 2019-07-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20190721_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('organization', models.CharField(max_length=256)),
                ('year', models.IntegerField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
