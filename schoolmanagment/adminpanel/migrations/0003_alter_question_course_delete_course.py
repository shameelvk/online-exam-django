# Generated by Django 5.0 on 2023-12-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
