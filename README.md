# Сайт с покемонами

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Предметная область

Сайт для помощи по игре [Pokemon GO](https://www.pokemongo.com/en-us/). Это игра про ловлю [покемонов](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).


![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

### Как запустить

Для запуска сайта вам понадобится Python версии 3.7-3.10

Cкачайте архив с кодом на компьютер или склонируйте репозиторий:
```bash
$ git clone git@github.com:IlyaG96/pokemon_map.git
```
Создайте в папке с репозиторием виртуальное окружение:
```bash
$ python3 -m venv [полный путь до папки pokemon_map без квадратных скобочек] env
```
```bash
$ cd pokemon_map
$ source env/bin/activate
$ pip install -r requirements.txt
```
Произведите миграции и создайте базу данных командами:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
Создайте суперпользователя (админа). Он будет необходим для добавления покемонов на карту:
```sh
$ python manage.py creaatesuperuser
```
Запустите разработческий сервер:
```sh
python3 manage.py runserver
```
Для доступа в админку перейдите [сюда](http://127.0.0.1:8000/admin).  
Сайт доступен [здесь](http://127.0.0.1:8000/).  

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта.


