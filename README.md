# Django Tree Menu Project

Пример Django-проекта с древовидным меню, реализованным через template tag.

---

## Структура проекта

- **tree_menu_project/** – корень проекта  
  - **manage.py** – точка входа  
  - **tree_menu_project/** – конфигурация Django  
    - settings.py  
    - urls.py  
    - wsgi.py  
    - asgi.py  
  - **menu/** – приложение для меню  
    - admin.py – настройка админки  
    - apps.py  
    - models.py – модели Menu и MenuItem  
    - views.py – view для index.html  
    - **templatetags/**  
      - draw_menu.py – реализация template tag  
      - \_\_init\_\_.py  
    - **templates/menu/**  
      - index.html – главная страница  
      - menu.html – шаблон отрисовки меню  

---

## Установка и запуск

1. Клонировать проект:
   ```bash
   git clone <repo_url>
   cd tree_menu_project
   ```
   
2. Создать и активировать виртуальное окружение:
   ```
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   ```
3. Установить зависимости:
   ```
   pip install django
   ```
4. Применить миграции:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Создать суперпользователя
   ```
   python manage.py createsuperuser
   ```
6. Запустить сервер
   ```
   python manage.py runserver
   ```

Использование на страницах

В любом шаблоне необходимо поключить библиотеку тегов и вызвать:
   ```
   {% load draw_menu %}
   {% draw_menu 'main_menu' %}
   ```
Меню строится в виде дерева:
* раскрываются все уровни над активным пунктом;
* также раскрывается первый уровень вложенности под активным пунктом;
* активный пункт определяется по текущему URL (request.path).

Требования

* Python 3.10+
* Django 5.2+
