# Generated by Django 4.1.6 on 2023-02-05 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('describe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('describe', models.TextField()),
                ('image', models.ImageField(upload_to='images_uploader_folder')),
                ('add_date', models.DateTimeField()),
                ('catgry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_handler.category')),
            ],
        ),
    ]