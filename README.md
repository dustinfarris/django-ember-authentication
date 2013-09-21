# Django/Ember Authenticate

![CircleCI build status](https://circleci.com/gh/dustinfarris/django-ember-authentication.png)

A simple how-to-do-it app that demonstrates one way to perform session-based authentication
in [Ember](http://emberjs.com) using [Django](http://djangoproject.com/) as a backend.  This 
application uses the latest builds of:

*  [Django][]
*  [Ember][]
*  [Ember Data][]
*  [Ember Data Django REST Adapter][]


You should have [virtualenvwrapper][] installed.

### Installation

```console
git clone git@github.com:dustinfarris/django-ember-authentication.git
mkvirtualenv django-ember-authentication
cd django-ember-authentication
make develop
```

### Run the tests

```console
make
```

### Fire up a temp server

```console
make run
```

Navigate to http://localhost:8000 and log in with username **dustin** and password **correct**.

## Summary

Authentication is probably one of the biggest initial hurdles when putting Ember to practical use. At
least that has been my experience. Fortunately, with the right architecture, authenticating can be
implemented with minimal code, and pain-free.

I chose session-based authentication because it is built into Django and it relieves me of having to
hack together token variables and remembering to include them on all my headers etc..  Most of the
token-based solutions I've seen to date have not been pretty. Django's session backend does the 
majority of the work for you, really your only responsibility is the check the username and password
(which Django has helpers for as well).

### Session

A challenge I encountered every way I tried this was preserving the "current user" after successful 
authentication.  Since the current user is really just a manifestation of the current session, I
decided to call the resource "session" which, in my Ember implementation, has user properties. If
this sounds confusing it will make sense when you look at the code.

The session is its own resource, with its own route mapping and controller.  On the server side,
Django responds to three HTTP methods at the /session/ endpoint: GET, POST, and DELETE. GET gets the
current session (if there is one), POST checks username/password credentials and then creates a
session. DELETE logs the user out. Using regular HTTP methods this way makes it easy to integrate
with both Ember and Django REST Framework.

When Ember successfully authenticates, it queries the appropriate user and sets the session model to
be that user.  The user's properties then become instantly available to the session template,
and to anything else with access to the SessionController.

## Notes

I've found that having the "current user" readily available is actually not all that important. With
a well-built backend, all data will be pre-filtered to the active user before it hits Ember.

## Acknowledgements

Big thank you to the Ember team and [Tom Christie][] for Django REST Framework.  These two projects 
have had a profound impact on modern web development and are very very exciting to work with.

Also thanks to [Toran Billups][] for creating Ember Data Django REST Adapter without which combining
Django and Ember would not be possible—or at least not as straight-forward. Also his [screencast] on 
integration testing Ember is an absolute must-watch.


[Django]: https://github.com/django/django/releases/tag/1.6b4
[Ember]: http://emberjs.com/builds/#/beta/latest
[Ember Data]: http://emberjs.com/builds/#/canary/latest
[Ember Data Django REST Adapter]: https://github.com/toranb/ember-data-django-rest-adapter/tree/ember1.0
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/
[Tom Christie]: https://github.com/tomchristie
[Toran Billups]: https://github.com/toranb
[screencast]: http://www.toranbillups.com/blog/archive/2013/07/21/Integration-testing-your-emberjs-app-with-QUnit-and-Karma/
