# Generated by Django 4.2.4 on 2023-08-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0011_feedbacks_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='feedback_content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
