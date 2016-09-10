# Django learning
[![Build Status](https://travis-ci.org/mpsk2/django-learning.svg?branch=master)](https://travis-ci.org/mpsk2/django-learning)
[![Coverage Status](https://coveralls.io/repos/github/mpsk2/django-learning/badge.svg?branch=master)](https://coveralls.io/github/mpsk2/django-learning?branch=master)

Set of applications in Django to learn Django. I have created that project for the purpose of learning basics of Django.

## Installation

```sh
sudo dnf install -y python3 python3-pip python3-devel sqlite3 sqlite3-devel
sudo pip install virtualenv
cd /path/to/project
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/dev.txt
python manage.py migrate
```
