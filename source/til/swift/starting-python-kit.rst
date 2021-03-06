==============================
Getting Started with PythonKit
==============================

.. meta::
    :description: Swift: Getting started with PythonKit
    :keywords: Swift, Python

``PythonKit`` allows calling Python code from Swift.

That sounds pretty amazing. Let's give it a go.

Repo: https://github.com/pvieito/PythonKit

.. note::
    You need to set **Enable Hardened Runtime** to **No** in your Xcode project
    to get PythonKit to work properly.

    I've talked about `Fighting with macOS’s System Integrity Protection
    <https://noumenal.es/posts/weeknotes-wk-40/PX/>`_ before if you want the
    details, but macOS is quite particular about library paths otherwise, and
    you'll likely end up with the system copy of Python 2.7!

Let's set up a little Python that we want to call from Swift::

  # In ~/Desktop/greeting.py
  def hello(name):
    return f"Hello, {name}! (From Python 💃)"

Then we set a ``PYTHON_LIBRARY`` environment variable, with the path to our
Python install. (I'm sure the macOS system Python is all very well and good…)

Now in Swift we can, quite miraculously I think, just import it and call our
Python code:

.. code-block:: swift

  import PythonKit

  let sys = Python.import("sys")
  print("Python \(sys.version_info.major).\(sys.version_info.minor)")
  print("Python Version: \(sys.version)")
  print("Python Encoding: \(sys.getdefaultencoding().upper())")

  let dirPath = "/Users/carlton/Desktop"

  func callPython() {
      sys.path.append(dirPath)
      let greeting = Python.import("greeting")
      let message = greeting.hello("Carlton")
      print(message)
  }

  callPython()

Here we import the **Python** ``sys`` module and print some basic info, before
setting ``sys.path``, importing our code and calling that.

Output will be this::

  Python 3.8
  Python Version: 3.8.7 (default, Jan 26 2021, 11:56:32)
  [Clang 12.0.0 (clang-1200.0.32.28)]
  Python Encoding: UTF-8
  Hello, Carlton! (From Python 💃)

There's so much goodness to be had in this.
