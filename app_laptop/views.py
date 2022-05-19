from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Laptop
from .forms import LaptopForm


def key_objects(key, i_object):
    """Вспомогательная функция, для search_choices.
    Возвращает необходимый объект с ключом модели"""
    if key == 'brand':
        return i_object.brand
    elif key == 'processor':
        return i_object.processor
    elif key == 'ram':
        return i_object.ram
    elif key == 'video_card':
        return i_object.video_card
    elif key == 'drive':
        return i_object.drive


def search_choices(form) -> List:
    """Функция - совершающая логику поиска ноутбука"""
    flag = True
    object_list = []
    for i_object in Laptop.objects.all():
        for key, value in form.cleaned_data.items():
            check_objects = key_objects(key, i_object)
            if check_objects.startswith(value) or value == 'Выбрать':
                flag = True
            else:
                flag = False
                break
        if flag is True:
            object_list.append(i_object)
        else:
            flag = True
    return object_list


def search_view(request):
    """Представление поисковика и результатов поиска (GET, POST)"""
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            object_list = search_choices(form)
            context = {'laptop': object_list, 'count_obj': len(object_list)}
            return render(request, 'laptop/laptop_list.html', context)
    else:
        form = LaptopForm
        content = {'form': form}
        return render(request, 'laptop/index.html', content)


class LaptopListView(ListView):
    """Представление общего списка ноутбуков"""
    paginate_by = 10
    model = Laptop
    template_name = 'laptop/all_laptops.html'
    context_object_name = 'laptop'


class LaptopDetailView(DetailView):
    """Представление детальной страницы"""
    model = Laptop
    template_name = 'laptop/detail_laptop.html'
    context_object_name = 'laptop'
    queryset = Laptop.objects.all()
