# Generated by Django 4.1.4 on 2023-04-25 11:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_new_delete_post_delete_post1_delete_tft'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
