======================================
Progressively Enhance a Form with HTMX
======================================

.. meta::
    :description: HTMX: Progressively Enhance a Form
    :keywords: HTMX

With a Django form that I want to include in a page and use HTMX to process on
the `change` event:

.. code-block:: html

    <div hx-select=".my-form">
      <form method="post" action={{ form_action }} class="my-form"
          hx-boost="true"
          hx-target="this"
          hx-swap="outerHTML"
          hx-trigger="change">

          {% csrf_token %}
          {{ form|crispy }}

          {% if not request.htmx %}
            <input type="submit" name="Save" />
          {% else %}
            <img class="htmx-indicator" src="{% static 'img/three-dots.svg'%}" />
          {% endif %}
      </form>
    </div>

This would be embedded in a full template, using `hx-select` to swap out just
the form in the host page.

For a non-HTMX rendering I need to add the `submit`, so the form can be
normally processed.

But almost always I don't want that button to show. So we can remove it on page
load:

.. code-block:: javascript

    window.addEventListener("load", function () {
        if (htmx) {
            document.querySelector(
                '.my-form input[type=submit]'
            ).remove();
        }
    });

If `htmx` loaded, get rid of the input and let it handle the `change` event.

Where `htmx` doesn't manage to load, the form should still work.

Not perfect, but good enough.
