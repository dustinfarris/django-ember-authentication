# Django/Ember Authenticate

A simple how-to-do-it app that demonstrates one way to perform authentication
in Ember using Django as a backend.

You should have [virtualenvwrapper][] installed.

## Installation

```bash
git clone git@github.com:dustinfarris/django-ember-authentication.git
mkvirtualenv django-ember-authentication
cd django-ember-authentication
make develop
```

## Run the tests

```bash
make
```

### Fire up a temp server

```bash
make run
```

Navigate to http://localhost:8000 and log in with username **dustin** and password **correct**.


[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/