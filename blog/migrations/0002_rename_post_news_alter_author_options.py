# Generated by Django 4.1.7 on 2023-03-07 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
    ]