from django import template
from menu.models import Menu, MenuItem
from django.urls import resolve

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu = Menu.objects.filter(name=menu_name).first()
    if not menu:
        return {'tree': []}

    items = list(menu.items.all())

    def build_tree(parent=None, visited=None):
        if visited is None:
            visited = set()
        tree = []
        for item in items:
            if item.parent == parent:
                if item.id in visited:
                    continue  # пропускаем, чтобы не уйти в цикл
                visited.add(item.id)
                tree.append({
                    'item': item,
                    'children': build_tree(item, visited),
                    'is_active': current_url.startswith(item.get_url() or ''),
                })
        return tree

    print("draw_menu called for:", menu_name)
    return {'tree': build_tree()}
