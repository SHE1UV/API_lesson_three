# Обрезка ссылок с помощью Битли

Этот код поможет Вам сократить любую ссылку и покажет сколько было переходов по сокрещенной ссылке.

### Как установить

Ваш API-ключ можно получить, зарегестрировавшись на [официальном сайте](https://bitly.com/a/sign_in).
API-ключ выглядит примерно вот так: 17c09e22ad155405159ca1977542fecf00231da7.
После вам надо придумать название для своей переменой, и в файле .env запишите ее и приравняйте ваш API-ключ.


Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для 
установки зависимостей:

```
pip install -r requirements.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).