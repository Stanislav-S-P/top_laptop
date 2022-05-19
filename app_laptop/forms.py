from typing import List

from django.forms import ChoiceField, forms
from .models import Laptop


def unique_name(model: List, name: str) -> List:
    """Функция - фильтрует параметры из БД, возвращает список элементов  для select формы"""
    objects_set = set()
    objects_set.add('Выбрать')
    for elem in model:
        if name == 'brand':
            objects_set.add(elem.brand)
        elif name == 'processor':
            objects_set.add(elem.processor.split()[0])
        elif name == 'ram':
            objects_set.add(elem.ram.split()[0])
        elif name == 'video_card':
            objects_set.add(elem.video_card.split()[0])
        elif name == 'drive':
            objects_set.add(elem.drive.split()[0] + ' ' + elem.drive.split()[1])
    objects_list = list()
    for i_object in objects_set:
        objects_list.append((i_object, i_object))
    objects_list = sorted(objects_list, key=lambda x: x[1], reverse=True)
    return objects_list


class LaptopForm(forms.Form):
    """Класс - форма поисковика"""
    brand = ChoiceField(choices=unique_name(Laptop.objects.all(), 'brand'))
    processor = ChoiceField(choices=unique_name(Laptop.objects.all(), 'processor'))
    ram = ChoiceField(choices=unique_name(Laptop.objects.all(), 'ram'))
    video_card = ChoiceField(choices=unique_name(Laptop.objects.all(), 'video_card'))
    drive = ChoiceField(choices=unique_name(Laptop.objects.all(), 'drive'))
