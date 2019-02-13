# Generated by Django 2.1.5 on 2019-02-13 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(default='', max_length=255)),
                ('deskripsi', models.TextField(default='', max_length=255)),
                ('images', models.ImageField(upload_to='Media/img')),
                ('komentar', models.IntegerField(default=0)),
                ('waktu_update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]