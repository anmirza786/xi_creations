# Generated by Django 4.1 on 2022-08-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_ourclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('message', models.TextField(verbose_name='Message')),
                ('is_contacted', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
