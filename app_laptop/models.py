from django.db import models


class Laptop(models.Model):
    """Класс - модель ноутбука БД"""
    brand = models.CharField(max_length=25, verbose_name='Бренд')
    title = models.CharField(max_length=400, verbose_name='Заголовок')
    price = models.CharField(max_length=15, verbose_name='Цена')
    image = models.CharField(max_length=200, verbose_name='Изображение')
    processor = models.CharField(max_length=200, verbose_name='Процессор')
    cores = models.CharField(max_length=3, verbose_name='Количество ядер')
    cache_memory = models.CharField(max_length=200, verbose_name='Кэш-память')
    ram = models.CharField(max_length=200, verbose_name='Оперативная память')
    screen = models.CharField(max_length=200, verbose_name='Экран')
    resolution = models.CharField(max_length=200, verbose_name='Разрешение')
    video_card = models.CharField(max_length=200, verbose_name='Видеокарта')
    sound = models.CharField(max_length=200, verbose_name='Звук')
    drive = models.CharField(max_length=200, verbose_name='Накопитель')
    wireless_connection = models.CharField(max_length=200, verbose_name='Беспроводная связь')
    ports = models.CharField(max_length=200, verbose_name='Порты')
    additional_devices = models.CharField(max_length=200, verbose_name='Дополнительные устройства')
    input_devices = models.CharField(max_length=200, verbose_name='Устройства ввода')
    housing_material = models.CharField(max_length=200, verbose_name='Материал корпуса')
    cover_material = models.CharField(max_length=200, verbose_name='Материал крышки')
    weight = models.CharField(max_length=200, verbose_name='Вес')
    battery = models.CharField(max_length=200, verbose_name='Батарея')

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
