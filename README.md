# FART
_Fucking Awesome Reporting Toolkit_

The goal of FART is to reproduce the feature set of Lockheed Martin's 
[DART (Documentation and Reporting Toolkit)](https://github.com/lmco/dart).

## Prerequisites

* [Yarn](https://yarnpkg.com/)
* [Python](https://python.com) >= 3.5
* [virtualenv](https://pypi.python.org/pypi/virtualenv)
  (`pip install virutalenv`)

## Setup

There is a PowerShell script to activate `virtualenv`, but you can do it
manually via `python3 -m virtualenv ./venv --no-download`, use the appropriate
activation method for your shell, and then `pip install -r requirements` to
install Django.

You can then install the Yarn packages with `yarn install`.

## Running

`python3 ./manage.py runserver`

Navigate to `http://localhost:8000`.

There is also an admin page at `http://localhost:8000/admin` that can be used
to manually create missions, quotes, test cases, etc, however you'll need to 
reset the Admin password from the Django shell (`python3 ./manage.py shell`):

```py
from django.contrib.auth.models import User
users = User.objects.all()
user = users[0] # or the appropriate index
user.set_password('new_password')
user.save()
```