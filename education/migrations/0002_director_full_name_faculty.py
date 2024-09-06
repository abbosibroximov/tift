# Generated by Django 4.0 on 2024-09-02 03:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='full_name',
            field=models.CharField(default='Full name', max_length=150),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', ckeditor.fields.RichTextField()),
                ('degree', models.CharField(choices=[('master', 'Magistratura'), ('bachelors', 'Bakalavr')], max_length=20)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.director')),
            ],
        ),
    ]
