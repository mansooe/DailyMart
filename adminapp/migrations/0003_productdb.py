# Generated by Django 4.0.4 on 2022-07-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_rename_categorytyname_categorydb_categoryname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200, null=True)),
                ('productimg', models.ImageField(null=True, upload_to='media')),
                ('productcategory', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
