# Обрезка ссылок с помощью Битли

Этот код поможет Вам сократить любую ссылку и покажет сколько было переходов по сокрещенной ссылке.

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtual/venv](https://docs.python.org/3/library/venv.html)

Перед запуском программы не забудьте склонировать проект или скачать его архив.
В папке с проектом не забудьте создать .env файл, где вы укажите ваш собственный токен Битли([Создать токен.](https://app.bitly.com/settings/api/))

```
APIKEY_BITLY = ваш токен с bitly
```

## Как запустить файл

Для сокращения ссылки необходимо запустить файл, где в качестве аргумента будет ваша ссылка:
```
python main.py https://dvmn.org/modules/
```

Для подсчета переходов по ссылке Битли необходимо запустить файл, где в качестве аргумента будет ваш Битлинк:
```
python main.py https://bit.ly/3N9ThBf
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
