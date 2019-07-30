# Generated by Django 2.2.3 on 2019-07-29 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messaging',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='messaging',
            name='message_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messaging',
            name='recevier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recevier', to='Chat.User'),
        ),
        migrations.AlterField(
            model_name='messaging',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='Chat.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
