# Generated by Django 4.1.13 on 2024-07-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='culturauser',
            name='comment_connoisseur',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='content_creator',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='cultura_contributor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='explorer_extraordinaire',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='guide_guru',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='knowledge_seeker',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='like_leader',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='share_star',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='culturauser',
            name='trend_setter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
