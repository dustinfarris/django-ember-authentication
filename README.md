# Django/Ember Authenticate

A simple how-to-do-it app that demonstrates one way to perform session-based authentication
in Ember using Django as a backend.  This application uses the latest builds of:

*  [Django][]
*  [Ember][]
*  [Ember Data][]
*  [Ember Data Django REST Adapter][]


You should have [virtualenvwrapper][] installed.

## Installation

```console
git clone git@github.com:dustinfarris/django-ember-authentication.git
mkvirtualenv django-ember-authentication
cd django-ember-authentication
make develop
```

## Run the tests

```console
make
```

## Fire up a temp server

```console
make run
```

Navigate to http://localhost:8000 and log in with username **dustin** and password **correct**.


[Django]: https://github.com/django/django/releases/tag/1.6b4
[Ember]: http://emberjs.com/builds/#/beta/latest
[Ember Data]: http://emberjs.com/builds/#/canary/latest
[Ember Data Django REST Adapter]: https://github.com/toranb/ember-data-django-rest-adapter/tree/ember1.0
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/

