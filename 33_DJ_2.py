# ---------- sampsite/views.py ----------

from django.http import HttpResponse

import random


# This is our View function which receives info
# on the request
def hello_world(request):
    # Return a response object with the text Hello World
    return HttpResponse("Hello World")


def root_page(request):
    return HttpResponse("Root Home Page")


# Receives the number passed in the url and then returns
# a random number
def random_number(request, max_rand=100):
    # Calculate a random number between 0 and the number passed
    random_num = random.randrange(0, int(max_rand))

    # Place the string and decimal in the output
    msg = "Random Number Between 0 and %s : %d" % (max_rand, random_num)

    return HttpResponse(msg)


# ---------- NOW ON TO SETTINGS ----------

# ---------- settings.py ----------

"""
Django settings for sampsite project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1$(46qw^uc2q&c)gad(*4^y)a8g2^dbr$%)nlvyf3jygfbv70('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [# - The Django admin system
    'django.contrib.admin',

    # - The authentication system
    'django.contrib.auth',

    # - Framework for content types
    'django.contrib.contenttypes',

    # - Session Framework
    'django.contrib.sessions',

    # - Message Framework
    'django.contrib.messages',

    # - Manages static files
    'django.contrib.staticfiles',

    # 4 Include our polls app
    # 4 Run python3 manage.py makemigrations polls
    # 4 to notify Django that you have updated your Model
    # 4 Run python3 manage.py sqlmigrate polls 0001 to see
    # 4 the SQL used to create the DB
    # 4 Run python3 manage.py migrate to create the DB
    # 4 Create the models in polls/models.py
    'polls.apps.PollsConfig', ]

# 6 We can add data to the DB using the Python shell
# - python3 manage.py shell
# - Import Models : from polls.models import Question, Choice
# - Display Questions : Question.objects.all()
# - Create a Question
# - from django.utils import timezone
# - q = Question(question_text="What's New?", pub_date=timezone.now())
# - Save to the DB : q.save()
# - Get the questions id : q.id
# - Get the questions text : q.question_text
# - Get the pub date : q.pub_date
# - Change the question : q.question_text = "What's Up?"
# - Save the change : q.save()
# - Display Questions : Question.objects.all()

# 6 Change polls/models.py to provide more info on question and choice

MIDDLEWARE = ['django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', ]

ROOT_URLCONF = 'sampsite.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages', ], }, }, ]

WSGI_APPLICATION = 'sampsite.wsgi.application'

# 4 Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# 4 We'll use the default database of SQLite3
# - You can use other DBs, but must add USER, PASSWORD and HOST
# - django.db.backends.mysql
# - django.db.backends.postgresql
# - django.db.backends.oracle

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), }}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', }, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', }, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }, ]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

# - Change the time zone to yours using
# - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# - Add a path for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# ---------- sampsite/urls.py ----------

"""sampsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# url matches the URL in the browser to a module
# in your Django project
from django.conf.urls import url

# Loads URLs for Admin site
from django.contrib import admin

# Reference my hello_world function
from sampsite.views import hello_world, root_page, random_number

# 3 include allows you to reference other url files
# in our project
from django.conf.urls import include

# Lists all URLs
# Add the directory in the URL you want tied to
# the hello_world function
# The r means we want to treat this like a raw string
# that ignored backslashes
# Then we define a regular expression where ^ is the
# beginning of a string, then we have the text to match
# The $ signifies the end of a Regex string

# We can pass data to a function by surrounding the part
# of the Regex to send with parentheses
# If they didn't enter a number I provide a default max
urlpatterns = [url(r'^admin/', admin.site.urls), url(r'^helloworld/$', hello_world), url(r'^$', root_page), url(r'^random/(\d+)/$', random_number), url(r'^random/$', random_number),

    # 3 Reference the root of the polls app
    url(r'^polls/', include('polls.urls')), ]

# 3 Test that the polls URL works by running the server
# python3 manage.py runserver
# Go to localhost:8000/polls/

# 3 Setup the database in settings.py

# ---------- polls/views.py ----------

# 1 Create the polls app inside our project
# 1 python3 manage.py startapp polls
# 1 You can have multiple apps in your project
# 1 Now we will create a view

from django.http import HttpResponse


def index(request):
    return HttpResponse("You're in the polls index")


# 1 Now attach the view to a url in urls.py

# ---------- polls/urls.py ----------

from django.conf.urls import url

from . import views

# 2 Add a reference to the view and assign it to
# the root URL for polls

urlpatterns = [url(r'^$', views.index, name='index'), ]

# 2 Now point the root URL file to the polls app

# ---------- polls/models.py ----------

# 5 Here you define the names and data types for
# 5 the information you are storing in your database

from django.db import models

import datetime
from django.utils import timezone


# 5 Create your models here.
# 5 Each model is a class with class variables that
# 5 represent fields in your database
# 5 After setting the column names an data types the DB
# 5 can create the table

class Question(models.Model):
    # 5 Define a DB column called question_text which
    # 5 contains text with a max size of 200
    question_text = models.CharField(max_length=200)

    # 5 This contains a date and the text passed is an
    # 5 optional human readable name
    pub_date = models.DateTimeField('date published')

    # 7 Return the text for the question when the Question
    # 7 is called by editing __str__

    def __str__(self):
        return self.question_text

    # 7 Here is a custom method for returning whether
    # 7 the question was published recently
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # 5 Define that each choice is related to a single
    # 5 Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 7 Return the Choice text as well
    def __str__(self):
        return self.choice_text

        # 7 Let's test our changes : python3 manage.py shell
        # 7 from polls.models import Question, Choice
        # 7 Get a detailed list of questions
        # 7 Question.objects.all()

        # 7 Get the Question with the matching id
        # 7 Question.objects.filter(id=1)

        # 7 Get the question that starts with What
        # 7 Question.objects.filter(question_text__startswith='What')

        # 7 Get Question published this year
        # 7 from django.utils import timezone
        # 7 current_year = timezone.now().year
        # 7 Question.objects.get(pub_date__year=current_year)

        # 7 If you request something that doesn't exist you
        # 7 raise an exception
        # 7 Question.objects.get(id=2)

        # 7 Search for primary key
        # 7 Question.objects.get(pk=1)

        # 7 Test was_published_recently()
        # 7 q = Question.objects.get(pk=1)
        # 7 q.was_published_recently()

        # 7 Show choices for matching question
        # 7 q.choice_set.all()

        # 7 Add new choices
        # 7 q.choice_set.create(choice_text='Not Much', votes=0)
        # 7 q.choice_set.create(choice_text='The Sky', votes=0)
        # 7 q.choice_set.create(choice_text='The Clouds', votes=0)

        # 7 Display choices
        # 7 q.choice_set.all()

        # 7 Display number of choices
        # 7 q.choice_set.count()

        # 7 Show all choices for questions published this year
        # 7 Use __ to separate relationships
        # 7 Choice.objects.filter(question__pub_date__year=current_year)

        # 7 Delete a choice
        # 7 c = q.choice_set.filter(choice_text__startswith='The Clouds')

        # 5 After defining the model we include the app in our project
        # 5 under INSTALLED_APPS in settings.py