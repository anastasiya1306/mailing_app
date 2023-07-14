from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Контактный email')
    fullname = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    DAILY = 'раз в день'
    WEEKLY = 'раз в неделю'
    MONTHLY = 'раз в месяц'

    FREQUENCY_CHOICES = [
        (DAILY, 'раз в день'),
        (WEEKLY, 'раз в неделю'),
        (MONTHLY, 'раз в месяц'),
    ]

    CREATED = 'Создана'
    LAUNCHED = 'Запущена'
    COMPLETED = 'Завершена'

    SELECT_STATUS = [
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    mailing_time = models.TimeField(verbose_name='Время рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    frequency = models.CharField(max_length=100, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, default=CREATED, choices=SELECT_STATUS, verbose_name='Статус рассылки')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'



