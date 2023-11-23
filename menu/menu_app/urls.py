from django.urls import path, re_path
from . import views
from .models import Menu

app_name = 'menu_app'


def generate_menu_urls():
    menu_urls = []
    menus = Menu.objects.all()
    for menu in menus:
        menu_urls.append(path(f'menu/{menu.title}/', views.draw_menu, name=f'draw_menu_{menu.title}'))
    return menu_urls


urlpatterns = [
    path('menu/draw_menu/<str:menu_name>/', views.draw_menu, name='draw_menu'),
] + generate_menu_urls()
