# Generated by Django 3.2.9 on 2021-11-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_wefunderimg_img_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='WefunderSql',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to='upload/')),
                ('img_file', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='wefunder',
            name='project_Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
