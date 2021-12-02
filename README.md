# Космический Телеграм

Используйте _fetch_spacex.py_ и _fetch_nasa.py_ для сбора изображений космоса.
_space_image_bot.py_ - для постинга изображений в телеграм-канал. Автопостинг через DELAY секунд

# Как установить

Для _fetch_nasa.py_ получите NASA_API_KEY здесь: https://api.nasa.gov/

Для постинга изображений вам понадобится:
1. создать свой бот в @BotFather и получить token
2. Содать свой канал @your_channel_name и добавить своего бота туда как Администратора

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```

# Пример использования
### Для сбора изображений

```python fetch_nasa.py```
или
```python fetch_spacex.py```

### Для рассылки изображений в Телеграмм-канал

```python spaxe_image_bot.py```


# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
