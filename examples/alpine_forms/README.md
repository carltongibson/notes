# Alpine Enhanced Form Example

Demo code for _Enhancing your Django 5.0 Forms with Alpine.js_ talk, to Django Paris
Meetup, Tuesday April 23, 2024.

Blog post to follow.

## Running the example

To view the example:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

Visit http://127.0.0.1:8000 in you browser.

## Key things to note:

* `INSTALLED_APPS` and `FORM_RENDERER` settings in settings.py.
* Overridden Django templates in `templates/django/forms` directory.
* Form class defined in `urls.py`.
* Form template, with field partials, in `templates/example-form.html`.
