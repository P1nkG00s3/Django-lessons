# Generated by Django 5.0.2 on 2024-02-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridgeo', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('receipt', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]