# Generated by Django 2.2.3 on 2019-07-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_conta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]