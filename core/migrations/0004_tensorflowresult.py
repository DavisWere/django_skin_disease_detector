# Generated by Django 5.0.2 on 2024-03-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TensorflowResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.CharField(max_length=4)),
                ('skin_diseases', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]