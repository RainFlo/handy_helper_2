# Generated by Django 2.2 on 2020-10-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='users',
            field=models.ManyToManyField(related_name='taken_jobs', to='main.User'),
        ),
        migrations.CreateModel(
            name='Real_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('jobs', models.ManyToManyField(related_name='real_categories', to='main.Job')),
            ],
        ),
    ]
