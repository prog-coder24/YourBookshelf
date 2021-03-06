# Generated by Django 3.2.5 on 2021-07-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadingRootsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='Genres',
            field=models.ManyToManyField(related_name='gbooks', to='ReadingRootsApp.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Languages',
            field=models.ManyToManyField(related_name='lbooks', to='ReadingRootsApp.Language'),
        ),
    ]
