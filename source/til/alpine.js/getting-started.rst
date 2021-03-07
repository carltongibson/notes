==============================
Getting Started with Alpine.js
==============================

.. meta::
   :description: Getting started with Alpine.js.
   :keywords: Alpine.js

`Alpine.js`_:

  Alpine.js offers you the reactive and declarative nature of big frameworks like Vue or React at a much lower cost.

  You get to keep your DOM, and sprinkle in behavior as you see fit.

  Think of it like Tailwind for JavaScript.

Very firmly in the modern batch of "JavaScript Sprinkles" libraries. The
Tailwind folks say of it:

  [Alpine.js] is without a doubt what I'd recommend if you'd otherwise be
  writing jQuery or vanilla JS.

With that kind of intro, we've got to give it a go.

Basics
======

You include from the CDN, then declare a component.

.. code-block:: html

  <div x-data="{ state: false }">
    <p>State: <span x-text="state ? 'true' : 'false'"></span></p>

    <button x-on:click="state = !state">Toggle</button>

    <div x-bind:class="{ 'blue': state }">@class</div>
  </div>

The `x-data` is what causes the component to be defined. The attribute can be
empty, but it's the on-switch, you need it there.

Then the button toggles the class on the div.

More complex
============

You can extract your logic and use an object:

.. code-block:: html

  <script>
      function stateObj() {
          return {
              active: false,
              toggle() {
                  this.active = !this.active;
                  this.setClass()
              },
              setClass() {
                if (this.active) {
                  this.$refs.targetDiv.classList.add('blue')
                } else {
                  this.$refs.targetDiv.classList.remove('blue')
                }
              }
          }
      }
  </script>
  <div x-data="stateObj()">
    <p>Another way, using more JS.</p>
    <p>State: <span x-text="active"></span></p>

    <button x-on:click="toggle">Toggle</button>

    <div x-ref="targetDiv">@class</div>
  </div>

Pretty simple as these things go.

`Examples on CodePen`__

.. _Alpine.js: https://github.com/alpinejs/alpine
.. __: https://codepen.io/carltongibson/pen/GRNBxKV?editors=1100
