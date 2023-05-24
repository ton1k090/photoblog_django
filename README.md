Описание проекта: Фотоблог

Инструменты разработки Стек:

Python >= 3.9 Django == 3.2.4 sqlite3 Разработка

Поставить звездочку)
Клонировать репозиторий git clone https://github.com/DJWOMS/cook_blog.git
Создать виртуальное окружение cd cook_blog
python -m venv venv

Активировать виртуальное окружение Linux
source venv/bin/activate Windows

./venv/Scripts/activate

Устанавливить зависимости: pip install -r req.txt
Выполнить команду для выполнения миграций python manage.py migrate
Создать суперпользователя python manage.py createsuperuser
Запустить сервер python manage.py runserver
Ссылки Сайт http://127.0.0.1:8000/
Админ панель http://127.0.0.1:8000/admin
