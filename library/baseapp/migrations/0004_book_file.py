# Generated by Django 4.2 on 2023-04-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]