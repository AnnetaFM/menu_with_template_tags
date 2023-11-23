from django import template
from menu_app.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.filter(title=menu_name).first()
    if menu:
        return render_menu(menu)
    return ''


def render_menu(menu_item):
    result = f'<ul><li><a href="{menu_item.url}">{menu_item.title}</a>'
    children = menu_item.menu_set.all()
    if children:
        result += '<ul>'
        for child in children:
            result += render_menu(child)
        result += '</ul>'
    result += '</li></ul>'
    return result
