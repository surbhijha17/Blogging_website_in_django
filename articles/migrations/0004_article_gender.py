# Generated by Django 2.1 on 2019-03-29 20:01

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gender',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='DRAFTS', max_length=100, no_check_for_status=True),
        ),
    ]
