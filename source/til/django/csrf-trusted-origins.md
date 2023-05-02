# CSRF and Trusted Origins in Django 4.x+

The Django 4.0 release notes had a little entry on [`CSRF_TRUSTED_ORIGINS` changes](https://docs.djangoproject.com/en/4.2/releases/4.0/#csrf-trusted-origins-changes) in the _Backwards incompatible changes in 4.0_ section.

> Values in the `CSRF_TRUSTED_ORIGINS` setting must include the scheme (e.g. `'http://'` or `'https://'`) instead of only the hostname.

Further up, there’s a note on changes to CSRF:

> CSRF protection now consults the Origin header, if present. To facilitate this, _some changes_ to the `CSRF_TRUSTED_ORIGINS` setting are required.

(The _some changes_ they’re linking back to the previous.)

In basic setups you shouldn’t have to set `CSRF_TRUSTED_ORIGINS` at all.
From [the docs](https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-trusted-origins):

> For requests that include the Origin header, Django’s CSRF protection requires that header match the origin present in the Host header.

… which, unless you’re doing stuff with subdomains or whatnot, it just should.

Nonetheless, when you’re upgrading from Django 3.2 you might find you hit CSRF errors:

> Origin checking failed - https://your-site.com does not match any trusted origins.

Hmmm 🤔

Some head scratching and a few searches later, throwing some values into `CSRF_TRUSTED_ORIGINS` might seem to resolve it:

```python
# Don't do this. ❌
CSRF_TRUSTED_ORIGINS = [
    'https://your-site.com',
    'http://your-site.com',
]
```

The CSRF check compares the `Host` header, which looks like `'your-site.com'` with the `Origin`, which looks like `'https://your-site.com'`, by using the value of `request.is_secure()` to determine the scheme.

From [the docs](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.is_secure):

> `HttpRequest.is_secure()`¶
> Returns True if the request is secure; that is, if it was made with HTTPS.

If you’re doing SSL termination at your web server, **maybe** your problem is that `request.is_secure()` is returning `False`, even though you’re serving with HTTPS, and so your Origin header is `https://...` whilst the CSRF middleware check is looking for `http://...`.

The standard way to resolve this is to set [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/4.2/ref/settings/#secure-proxy-ssl-header) to a tuple with two elements – the name of a header to look for and a required value that the web server will set to tell Django that the request used HTTPS.

Something like:

```python
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
```

[But do go read the warnings there](https://docs.djangoproject.com/en/4.2/ref/settings/#secure-proxy-ssl-header).

I don’t know what weird setups you kids are using these days 🥳 So if you can’t set up that header, then you can use a WSGI middleware to specify that you’re using HTTPS:

```
# In wsgi.py
django_app = get_wsgi_application()


def https_app(environ, start_response):
    environ["wsgi.url_scheme"] = "https"
    return django_app(environ, start_response)


application = https_app
```

Here we override the WSGI [`wsgi.url_scheme` environment value](https://peps.python.org/pep-0333/#environ-variables), which in the scenario here is likely `http`, because that was the protocol your (SSL terminating) web server made the request to your WSGI application using.

Again, do this only as long as you actually are always using HTTPS, but that’s now nearly standard these days, I think.

Suddenly, now that Django knows it’s using HTTPS, the CSRF errors again go away.

May your Hosts (and Schemes) match your Origins! Happy hunting 🎁
