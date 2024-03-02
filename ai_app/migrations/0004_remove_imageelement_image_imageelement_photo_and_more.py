# Generated by Django 4.0 on 2024-03-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_app', '0003_imageelement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageelement',
            name='image',
        ),
        migrations.AddField(
            model_name='imageelement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mediaphoto'),
        ),
        migrations.AlterField(
            model_name='imageelement',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='imageelement',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]