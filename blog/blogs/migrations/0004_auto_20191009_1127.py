# Generated by Django 2.2.6 on 2019-10-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'blogposts'},
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='topic',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]