# Generated by Django 3.0.7 on 2020-06-06 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='studentclass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Studentclass'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='studentclass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Studentclass'),
        ),
    ]
