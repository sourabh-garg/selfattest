# Generated by Django 3.0.5 on 2020-06-28 09:20

import common.uuid
from django.db import migrations, models
import selfattest.storage


class Migration(migrations.Migration):

    replaces = [('media_photo', '0001_initial'), ('media_photo', '0002_auto_20200628_0711'), ('media_photo', '0003_auto_20200628_0835')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(storage=selfattest.storage.PublicMediaStorage(), upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhotoMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=common.uuid.unique_uuid4, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('photo_url', models.TextField()),
                ('photo_height', models.PositiveIntegerField()),
                ('photo_width', models.PositiveIntegerField()),
                ('photo_name', models.TextField(blank=True)),
                ('photo_size', models.PositiveIntegerField()),
                ('content_type', models.TextField(null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='userphotometa',
            index=models.Index(fields=['external_id'], name='media_photo_externa_c9deb6_idx'),
        ),
        migrations.AlterField(
            model_name='tempphoto',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.RemoveField(
            model_name='userphotometa',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='userphotometa',
            name='photo_height',
        ),
        migrations.RemoveField(
            model_name='userphotometa',
            name='photo_name',
        ),
        migrations.RemoveField(
            model_name='userphotometa',
            name='photo_size',
        ),
        migrations.RemoveField(
            model_name='userphotometa',
            name='photo_width',
        ),
    ]
