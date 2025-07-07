# Testing with Playwright

Playwright's tagline:

> [Fast and Reliable End-to-End Testing for Modern Web Apps](https://playwright.dev/python/)

A couple of great videos to get you warmed up:

* [End-to-End Testing Django Applications Using Pytest With Playwright](https://djangotv.com/videos/djangocon-europe/2025/djancocon-europe-2025-end-to-end-testing-django-applications-using-pytest-with-playwright/) by Jacob Rief
* [Playwright for Django Demo - Workshop Content](https://www.youtube.com/watch?v=SmW8p3sDhzM) by Sheena O'Connell.

Then some links:

* [Hello Playwright.md](https://github.com/Guild-of-Educators/tutorial-modern-frontend-django-htmx/blob/main/tutorial/04.%20Hello%20Playwright.md). Again from Sheena. Part of her multipart Modern frontends with Django and HTMX tutorial.
* [Pytest-Django Documentation](https://pytest-django.readthedocs.io/en/latest/index.html)
* [Playwright Python Docs](https://playwright.dev/python/docs/intro)
* [Pytest Documentation](https://docs.pytest.org/en/6.2.x/contents.html)


And an example `tox` config to get up and running:

```ini
[testenv:playwright]
basepython = python3.13
skip_install = true
deps =
    -r requirements.txt
    pytest
    pytest-django
    pytest-playwright

commands=
    playwright install
    python -Wall -m pytest --reuse-db {posargs}
```
