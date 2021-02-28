=============================
Technical Writing with Sphinx
=============================

Sphinx is a documentation builder. It powers the docs for lots of projects,
including both Django and Python.

* `Sphinx homepage`_

.. _Sphinx homepage: https://www.sphinx-doc.org/en/master/

.. admonition:: Opinion

   Sphinx has everything. Powerful, best-in-class features such as,
   cross-referencing, ToC and index generation, and multiple output-format
   support, make it the best documentation builder available.

   There are others. I don't often say that there's a clear best choice in a
   domain, but with documentation there is. It's Sphinx. Use it.

reStructuredText vs Markdown
============================

reStructuredText and Markdown are both lightweight markup languages, that are
simpler to write than, say, HTML.

This file is written in reStructuredText. You can look at it's `source`_.

.. _source: https://github.com/carltongibson/notes/tree/main/source/sphinx/index.rst

Sphinx was built with reStructuredText support. When Markdown became popular
Sphinx lost a bit of popularity as people went in search of solutions that
didn't require them to use a different markup language.

Two points to make here:

* **reStructuredText is not hard**. It's almost the same as Markdown but offers
  a lot more, so it can seem more complex.

  I think links are the bit that catch people (more below.)

* **You don't have to choose**. These days there are a few options for parsing
  Markdown with Sphinx. I like the `MyST Parser`_: it opens up the full
  possibilities of Sphinx directives and roles within Markdown.

Links
-----

Try as I might, it took me years to remember the syntax for a Markdown link::

  [anchor text](http//some-url.com/page.html)

.. admonition:: Aside

  Ultimately it was learning Objective-C for iPhoneOS development that made it
  stick for me. Objective-C uses square-brackets for method calls::

    NSString *path = @"~/Desktop/cheapest-data-store.data"
    NSArray *myArray = [NSArray arrayWithContentsOfFile:path];

  Here we load our app data using the ``NSArray`` ``arrayWithContentsOfFile:``
  class-method.

  So, given the Markdown link format ``[anchor text](target url)``, in
  pseudo-code we're calling the function pointer returned by the Objective-C
  method call.

  Somewhat pointless, but I didn't forget it after that.

I remember coming to reStructuredText and having a massive block over the
differing link syntax. But if we look, it's not too different; it's worth the
effort committing it to memory.

Both formats allow defining reference and embedded links.

Reference links
~~~~~~~~~~~~~~~

Reference links allow you to define link targets in a separate list after the
main text.

.. tabs::

   .. group-tab:: reStructuredText

      .. code-block::

        Visit `Button`_

        .. _Button: https://btn.dev

   .. group-tab:: Markdown

      .. code-block::

        Visit [Button][BTN]

        [BTN]: https://btn.dev

You can see that there is very little difference between the two languages.
With Markdown you define an ID for the link which is used later to provide the
details. With reStructuredText you re-use the anchor text.

Embedded links
~~~~~~~~~~~~~~

With embedded links, the URL is right next to the anchor text.

.. tabs::

   .. group-tab:: reStructuredText

      .. code-block::

        Visit `Button <https://btn.dev>`_

   .. group-tab:: Markdown

      .. code-block::

        Visit [Button](https://btn.dev)

Here, again almost identical.

For the reStructuredText link, note the single ``_`` at the end.

On both reference and embedded links, reStructuredText also allows the use of a
double ``__`` to create an **anonymous target**, where you wouldn't need to
repeat the anchor text for the target. These can be handy if you're linking a
long phrase, but they can easily lead to confusion as to which link leads
where.

Use the single ``_`` versions to begin. Save the ``__`` anonymous versions for
when you're comfortable.

.. admonition:: Which link style should I use?

  Likely, reference links take a moment more time to write the first time
  around. But things are read more than they're written.

  Embedded links are harder to read and harder to maintain. It's worth
  preferring reference style links.

reStructuredText resources
==========================

A few key URLs:

* The Sphinx docs have a `full guide to reStructuredText`_, the first section
  of which is a `reStructuredText Primer`_.

.. _full guide to reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _reStructuredText Primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks

* Simon Willison has a nice post summarizing `the subset of reStructuredText
  worth committing to memory`__.

.. __ : https://simonwillison.net/2018/Aug/25/restructuredtext/

* The official docs are `part of the Docutils site`__. Of this, there's a
  `Quick reStructuredText`_ reference that I find myself at time and time
  again.

.. __: https://docutils.sourceforge.io/rst.html
.. _Quick reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html

Getting started tips
====================

* The `official Getting Started guide`_ is the place to begin, but::

    pip install sphinx
    sphinx-quickstart

  …and you're off!

  During `sphinx-quickstart` I like to say ``Y`` to separate `build` and
  `source` directories. Nothing much hangs on this. You get a nested `_build`
  directory if you say ``N``. Either way, add your build directory to your
  ``.gitignore``.

* Install `sphinx-autobuild`_::

    pip install sphinx-autobuild

  Then, assuming you said ``Y`` to the separate `build` and `source`
  directories, you can do monitor watch for changes and live-reload a browser
  window with::

    sphinx-autobuild source build/html

  I add a directive to the project ``Makefile``::

    watch:
	    sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

  Then it's ``make watch`` to run.

* The `furo theme`_ is very nice.

* As soon as you're up and running, spending an hour or so getting going with
  `cross-references`_, and the `autodoc`_ and `intersphinx`_ extensions. These
  will show you the road to unlocking the real power of Sphinx.

.. _MyST Parser: https://myst-parser.readthedocs.io/en/latest/
.. _official Getting Started guide: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _sphinx-autobuild: https://pypi.org/project/sphinx-autobuild/
.. _furo theme: https://github.com/pradyunsg/furo
.. _cross-references: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc
.. _intersphinx: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx
