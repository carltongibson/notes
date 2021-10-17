
(interlink-to-django)=
# Using Intersphinx to link to the Django docs

Preparing the docs for [Button](https://btn.dev/), I found myself needing to link to the Django docs. Specifically to settings that folks needs to expose to environment variables that Button will provide.

Sphinx provides this ability via the built-in [Intersphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html) — you can link to Django, Python, wherever.

In order to set it up, I needed to make Django available in the Sphinx `conf.py`. There's a `djangodocs` Sphinx extension that defines custom roles, such as the `:settings:` role I was after.

I have Django checked out locally, and a `DJANGO_PATH` environment variable set that points to that. The extension lives in `docs/_ext` so I needed to add that to `sys.path`:

```python
# Add the djangodocs Sphinx extension.
# Assume path to Django checkout is in DJANGO_PATH.
sys.path.append(
    os.path.join(os.environ["DJANGO_PATH"], 'docs/_ext')
)
```

Then add the `djangodocs` extension:

```python
extensions = [
    "djangodocs",
    ...
]
```

Finally I needed to add the location of Django's _Object Inventory_ file, which gives the defined symbols, such as `:settings:`DATABASES`, and so on.

```python
intersphinx_mapping = {
    ...
    'django': (
        'http://docs.djangoproject.com/en/stable/',
        'http://docs.djangoproject.com/en/stable/_objects/'
    ),
}
```

This last one was tricky. By default Sphinx will look for an `objects.inv` file at the URL given by the first item of the tuple there. Django though serves it at the Django-esque `/_objects/` URL. i'd fetched that locally and saved as a `django-inv.txt` ([similar to the docs example](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration)) but [Eric Holscher helped me out on Twitter](https://twitter.com/ericholscher/status/1449019514054582284) with the hint that you can put the whole URL in as the second tuple item. Thanks Eric!

With that in place it was all working — links to Django working nicely.

Once it's settled I'll likely add a `intersphinx_cache_limit`, so we don't refetch on every build.
