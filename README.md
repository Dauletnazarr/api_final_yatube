# api_final
api final

### Описание:

Этот проект представляет собой API для платформы Yatube, предназначенной для публикации постов, комментариев и взаимодействия между пользователями. API позволяет пользователям:

* Создавать и редактировать посты.
* Оставлять комментарии к постам.
* Подписываться на других пользователей и управлять своими подписками.
* Просматривать список групп и связанные с ними посты.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Dauletnazarr/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:
```
cd yatube_api
```
```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```

## Примеры запросов к API
### 1. Получение списка постов
Запрос:

http
Копировать код
GET /api/v1/posts/
Пример ответа:

```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "user1",
            "text": "Первый пост",
            "pub_date": "2024-11-13T12:34:56Z",
            "image": null,
            "group": null
        }
    ]
}
```

## 2. Создание комментария к посту
### Запрос:
```
POST /api/v1/posts/{post_id}/comments/
Content-Type: application/json
Authorization: Bearer <Ваш токен>
```

### Тело запроса:
```
{
    "text": "Это комментарий"
}
```
### Пример ответа:
```
{
    "id": 1,
    "author": "user1",
    "text": "Это комментарий",
    "created": "2024-11-13T12:35:00Z",
    "post": 1
}
```
## 3. Подписка на пользователя
### Запрос:
```
POST /api/v1/follow/
Content-Type: application/json
Authorization: Bearer <Ваш токен>
```
### Тело запроса:
```
{
    "following": "user2"
}
```
### Пример ответа:
```
{
    "user": "user1",
    "following": "user2"
}
```
## Технологии
* Django — основной фреймворк для разработки.
* Django REST Framework — для создания API.
* SQLite3 (рекомендуется) — в качестве базы данных.
* JWT — для аутентификации пользователей.
## Авторы
Проект разработан Dauletnazar Mambetnazarov.