# Generated by Django 4.1 on 2022-08-24 12:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='staff/images')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('introduction', ckeditor.fields.RichTextField()),
                ('description', models.TextField()),
                ('small_video', models.FileField(upload_to='work/videos')),
            ],
        ),
        migrations.CreateModel(
            name='WorkCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryTitle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='work/images')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work_image', to='core.work')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work_cats', to='core.workcategory'),
        ),
        migrations.CreateModel(
            name='BlogPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='blogPicturses')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_picture', to='core.blog')),
            ],
        ),
    ]