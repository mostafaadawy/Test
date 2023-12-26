# Creating Django App Step By Step

Note using Windows terminal Git Bash

# Django - Create Virtual Environment

```sh
 cd W3Shcool/Django/
 py -m venv myworld
```

- we can cahnge our virtual enviroment world to any name so here we create it with name myworld
- to activate it

```sh
myworld\Scripts\activate.bat
```

- if it works we will see venv name (myworld) between () if not seen this it is not activated and any dependancy you will install will be added to the main python placeholder/path
- if not seen (myworld try)

```sh
source myworld/Scripts/activate
```

- now you can install to your virtual enviroment folder

```sh
py -m pip install Django
```

- Check Django Version

```sh
django-admin --version
```

## Django Create Project

```sh
django-admin startproject my_tennis_club
```

- run the project

```sh
cd my_tennis_club/
py manage.py runserver
```

## Create App that is equivelent to module inside yoyr project for every bussnes function

```sh
py manage.py startapp members
```

## Django Views

views in Django acts as controllers in mvc where Django uses MVT model view template

- edit the view inside memeber `my_tennis_club/members/views.py:`

```sh
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
```

## View without Url will not work Create Url

- in the app folder create file with name urls.py `my_tennis_club/members/urls.py`

```sh
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]
```

## Editing The main Url

- in the main app which is the same name of the project that contains settings as configuration and other issues and contains sepearte file for all routes so we need to edit this main url to include our new app url `my_tennis_club/my_tennis_club/urls.py:`

```sh
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
```

- after runniong the server by `py manage.py runserver`
  now we can check using the browser link [127.0.0.1:8000/members](http://127.0.0.1:8000/members)
