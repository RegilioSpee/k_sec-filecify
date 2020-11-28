![Logo Filecify](https://i.imgur.com/AXLg8Sr.png)

[![MADE BY Django](https://img.shields.io/badge/MADE%20WITH%20Django-000000.svg?style=flat&logo=Next.js&labelColor=000)](https://www.djangoproject.com/)

Project gemaakt voor het vak K-sec op het Mediacollege

Applicatie om video's te uploaden op de meest veilige manier mogelijk. Wanneer het project word gecloned is het ook mogelijk
om onder andere video's te verwijderen of aan te passen via het admin paneel.

Project gemaakt met Python framework Django in Visual Studio Code.

## Demo

Gebruik de onderstaande code om het project lokaal te runnen na het te hebben gecloned via Github.

```
$ python manage.py runserver
```

## Features

- **Cross site scripting (XSS) protection**: XSS attacks allow a user to inject client side scripts into the browsers of other users.
- **Cross site request forgery (CSRF) protection**: CSRF attacks allow a malicious user to execute actions using the credentials of another user without that user’s knowledge.
- **SQL injection protection**: SQL injection is a type of attack where a malicious user is able to execute arbitrary SQL code on a database.

## Dependencies

- [TypeScript](https://www.typescriptlang.org/)
- [Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

## Structure

Hieronder is de structuur van het project te zien. 

```
mysite/
    manage.py
    mysite/
        ├── init.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
```

## References

- [Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

## License

MIT
