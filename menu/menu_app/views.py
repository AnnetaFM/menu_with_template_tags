from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Menu
from .templatetags.menumaker_tags import render_menu


def draw_menu(request, menu_name):
    menu = Menu.objects.filter(title=menu_name).first()
    if menu:
        menu_html = render_menu(menu)
        return render(request, 'menumaker/menu_template.html', {'menu_html': menu_html})

    return render(request, 'menumaker/menu_template.html', {'menu_html': 'Menu not found'})


def get_children(menu_item):
    children = menu_item.menu_set.all()
    if children:
        return [{'title': child.title, 'url': child.url, 'children': get_children(child)} for child in children]
    return []
