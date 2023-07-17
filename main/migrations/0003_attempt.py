# Generated by Django 4.2.3 on 2023-07-14 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mailing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_mailing', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')),
                ('status', models.CharField(choices=[('доставлено', 'доставлено'), ('не доставлено', 'не доставлено')], verbose_name='Статус попытки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера')),
                ('sending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Статистика (попытка)',
                'verbose_name_plural': 'Статистики (попытки)',
            },
        ),
    ]
