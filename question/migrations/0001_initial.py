# Generated by Django 4.0.5 on 2022-10-04 14:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplina', '0001_initial'),
        ('prova', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('issue', models.TextField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplina.disciplinamodel')),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova.provamodel')),
            ],
        ),
    ]
