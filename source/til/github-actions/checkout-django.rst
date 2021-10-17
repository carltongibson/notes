======================================
Checking out Django in a GitHub Action
======================================

In order to use :ref:`Sphinx interlinks to Django <interlink-to-django>`, I need
a checkout of Django for the ``djangodocs`` extension it uses.

That works fine locally, where I've got a Django checkout, but I needed the same
in my GitHub Action to automatically build and deploy the built docs.

GitHub already gives us the `checkout` action that you'll use in ≈ every

workflow to get your source code::

    - uses: actions/checkout@v2

We need to re-use that to also checkout Django::

    - name: Fetch Django
        uses: actions/checkout@v2
        with:
        repository: django/django
        path: django

This goes **after** you checkout your main repo, since there's a nice *delete
everything* step, which catches you otherwise.

The ``path`` is relative to the `cwd`, so Django goes into `./django`. To use
this I set ``DJANGO_PATH: ./django`` in the ``env`` when building the docs.

You can set it up to checkout into sibling directories, but then you'd need to adjust
the `cwd` for all your action steps. Having `django` in the top dir was fine for me,
so nested it is.

The `action repo`_ has a whole load of options for more complex cases.

.. _action repo: https://github.com/actions/checkout
