# Generated by Django 3.2.16 on 2025-03-10 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_employer_email'),
        ('main', '0003_jobstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobstatus',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_statuses', to='main.employee'),
        ),
        migrations.AlterField(
            model_name='jobstatus',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_statuses', to='employer.job'),
        ),
    ]
