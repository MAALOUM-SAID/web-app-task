# Generated by Django 4.0.3 on 2022-04-01 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0006_alter_task_begin_alter_task_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='begin',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('stading', 'stading'), ('sport', 'sport'), ('gaming', 'gaming')], default=('reading', 'reading'), max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('in progress', 'in progress'), ('pending', 'pending'), ('starting', 'starting'), ('Done', 'Done')], default=('in progress', 'in progress'), max_length=50, null=True),
        ),
    ]
