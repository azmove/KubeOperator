# Generated by Django 2.1.2 on 2019-02-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0002_cluster_current_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployexecution',
            name='operation',
            field=models.CharField(blank=True, choices=[('install', 'install'), ('upgrade', 'upgrade'), ('uninstall', 'uninstall')], default='install', max_length=128),
        ),
    ]