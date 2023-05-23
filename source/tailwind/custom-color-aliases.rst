============================================
Adding Custom Colour Aliases to Tailwind CSS
============================================

The Tailwind docs have a whole page on `Customizing Colors`_.

.. _Customizing Colors: https://tailwindcss.com/docs/customizing-colors

Under *Using the default colors* they have examples for only allowing a subset of colors, **and** for adding aliases, **and** for adding additional colors.

As a good starting point, I want **aliases as additional colors**, so that I can adjust the color scheme used, but still have the full default color gamut available.

.. tip::

    Colors you don't use don't end up in the final CSS, so unless you're at a stage where you're sure you want to exclude a color, there's no real need.

The trick is to take the **aliases** example, but use it with `extend`, rather than replacing the `colors` key entirely:

.. code-block:: javascript
    :caption: tailwind.config.js

    const colors = require('tailwindcss/colors')

    module.exports = {
      theme: {
        extend: {
          colors: {
            primary: colors.indigo,
            secondary: colors.blue,
            tertiary: colors.green,
            aspect: colors.orange
          },
        },
      },
    }

So here we can use `text-primary-900` and so on, beginning with the Tailwind purple, and swap that out when we're ready to experiment and settle on the final scheme.

I'm happy to use the default color names for the various grays, and the rest. I just need these few adjustable aliases.

Note: Maybe I never change them — knowing I can is enough to stop me worrying about that. 😊
