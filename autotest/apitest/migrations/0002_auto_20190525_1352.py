# Generated by Django 2.2.1 on 2019-05-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apistep',
            name='apiresponse',
        ),
        migrations.RemoveField(
            model_name='apitest',
            name='apitestdesc',
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apimethod',
            field=models.CharField(max_length=200, verbose_name='方法'),
        ),
    ]
