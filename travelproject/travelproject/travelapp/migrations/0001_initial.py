# Generated by Django 4.1.5 on 2023-01-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meet_the_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='Meet_the_Team')),
                ('description', models.TextField()),
            ],
        ),
    ]