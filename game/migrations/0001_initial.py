# Generated by Django 3.1.7 on 2021-05-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('question1', models.CharField(max_length=50)),
                ('question2', models.CharField(max_length=50)),
                ('vote1', models.IntegerField()),
                ('vote2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('card_img', models.ImageField(upload_to='')),
                ('flag', models.BooleanField()),
                ('flip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('initial', models.CharField(max_length=2)),
                ('fg_color', models.CharField(max_length=8)),
                ('bg_color', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_nickname', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=10)),
                ('flag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('chat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.chatuser')),
            ],
        ),
    ]
