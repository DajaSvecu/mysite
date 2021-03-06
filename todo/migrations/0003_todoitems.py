# Generated by Django 3.2.5 on 2021-07-25 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_delete_todoitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todoitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
        ),
    ]
