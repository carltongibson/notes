# The Single Folder Django Project Layout

How I start a Django project.
Tl;dr: By having just a single project folder, and without a separate app folder.

## Use Django’s default project template

I create a lot of Django projects. Projects for reproducing issue reports are the most common. But there are plenty of actual projects too. And for every one of those they’ll be a host of _tracer bullet_ projects where I’m testing out ideas.

I’ve done this **a lot** over the years, and, as with all these things, I have a way I like to do it. (I’d call this _an opinion_, except I’m not in the least vested in whether other people do it differently—there’s no, even implicit, claim of _correctness_.)

First, and foremost, I don’t use a custom project template. It’s Django’s barebones `startproject` template all the way for me. I know the customisations I want to make. It’s really **not** a big deal to make them. (If I was running an agency, with a much higher new project rate, and juniors in play, this would change, but I’m not.)

I certainly don’t use the likes of `django-cookiecutter`, as great as that is (and similar projects are) for many people.

The older I get, the longer I’ve been doing it, the less I want in the way, so no custom template. (I am happy to **read** custom templates. It’s always good to see what folks what to include. But **using** them is something else.)

## Too Many Folders

The standard flow here, which is [straight from the tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) I think, is to run `startproject`, followed almost immediately by a `startapp`. (`django-admin startproject mysite`, `cd mysite`, `./manage.py startapp polls`.) That’s all great but it’s too many files, too many folders.

If I’m starting a new project named `cakeshop`, I then need to come up with a decent app name for my models, but I already used it. I end up with something like `core` or `base`. Meh.

For the life of the project, I then spend almost all my time in the `core` directory, except when I need my settings file, which is somewhere else entirely. Double Meh.

## The Single Folder Layout

Better (for me) is to keep everything in the (perfectly named) `cakeshop` directory.

Step 1 is to add `cakeshop`  _as an app_ to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
     "django.contrib.sessions",
     "django.contrib.messages",
     "django.contrib.staticfiles",
+
+    "cakeshop",
 ]

```

Then I can just add a `models.py` (and an `admin.py` if I fancy) and I’m off to the races. 🏇

The whole project looks like this:

```
cakeshop:
	cakeshop:
		__init__.py
		asgi.py
		models.py
		settings.py
		urls.py
		wsgi.py
	manage.py
```

To begin I’ll throw my views into `urls.py`. I’ll sprout a `views.py` when that gets out of hand. Maybe we grow a `forms.py`, a `managers.py` and so on, but this is the structure I’ll almost always start with these days. It’s just a little more _dense_ than having the extra (to my eye idle ) app directory.

## Growing a Second App
…And Beyond

Let’s not be silly. The Single Folder Layout is about how you start, not how you continue.

At some point you’ll have a neat vertical (related models, views, and so on) of behaviour that you want in a separate app. When this happens, use `startapp` as normal and put your code there. This is the Django way.

## fin
This is how I do it. You might do it  differently. 😜


