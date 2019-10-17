# Generated by Django 2.2.6 on 2019-10-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answer_text', models.CharField(max_length=500)),
                ('difficulty_level', models.IntegerField(default=0)),
            ],
        ),
    ]