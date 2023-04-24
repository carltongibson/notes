# Using Django's template loaders to configure Tailwind

Tailwind has a config option to tell it where your HTML is:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],  // <--- Which files to scan?
  theme: {
    extend: {},
  },
  plugins: [],
}
```

So for a basic Django project you might think it's going to look something like this:

```javascript
    content: [
        '../../templates/**/*.html',  // Project level templates folder.
        '../../../**/templates/**/*.html',  // App template folders.
    ],
```

That double `../..` is bad enough: you're backing out of a project level `static/css` folder where you've got your `tailwind.config.js`. (_"I don't do it like that"_, you scream — it's only an example!)

You have nested folders, for includes and whatnot.

Then you have third-party apps which might be shipping templates too — are you really adding paths to you venv's `site-packages`?

Frankly it's a pain.

What you want is Django to tell Tailwind where your templates are. It knows.

## A list_templates command

First you need to list all templates. Django can do that:

```python
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.utils import get_app_template_dirs


class Command(BaseCommand):
    help = "List all template files"

    def handle(self, *args, **options):
        template_files = []
        app_template_dirs = get_app_template_dirs("templates")
        for app_template_dir in app_template_dirs:
            template_files += self.list_template_files(app_template_dir)
        template_files += self.list_template_files(settings.TEMPLATES[0]["DIRS"])

        self.stdout.write("\n".join(template_files))

    def list_template_files(self, template_dir):
        template_files = []
        # TODO: Look into using pathlib.Path.rglob() instead. 🤔
        for dirpath, _, filenames in os.walk(str(template_dir)):
            for filename in filenames:
                if filename.endswith(".html") or filename.endswith(".txt"):
                    template_files.append(os.path.join(dirpath, filename))
        return template_files
```

This would be a management command, so somewhere like `myapp/management/commands/list_templates.py`.


## Telling Tailwind

Then we need to use that in our Tailwind config.

Something like this in your `tailwind.config.js`:

```javascript
// Resolve path to directory containing manage.py file.
// This is the root of the project.
// Then assumed layout of <main-app>/static/css/tailwind.config.js, so up 3 levels.
// Adjust for your needs.
const path = require('path');
const projectRoot = path.resolve(__dirname, '../../..');

const { spawnSync } = require('child_process');

// Function to execute the Django management command and capture its output
const getTemplateFiles = () => {
  const command = 'python'; // Requires virtualenv to be activated.
  const args = ['manage.py', 'list_templates']; // Requires cwd to be set.
  const options = { cwd: projectRoot };
  const result = spawnSync(command, args, options);

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    console.log(result.stdout.toString(), result.stderr.toString());
    throw new Error(`Django management command exited with code ${result.status}`);
  }

  const templateFiles = result.stdout.toString()
    .split('\n')
    .map((file) => file.trim())
    .filter(function(e){return e});  // Remove empty strings, including last empty line.
  return templateFiles;
};

module.exports = {
  // Allow configuring some folders manually, and then concatenate with the
  // output of the Django management command.
  content: [].concat(getTemplateFiles()),
  theme: {
    extend: {},
  },
  plugins: [],
}
// console.log(module.exports)
```

Enough messing around. Enjoy! 🚀
