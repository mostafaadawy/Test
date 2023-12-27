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

## Returning Templates

- Create a templates folder inside the members folder, and create a HTML file named myfirst.html `my_tennis_club/members/templates/myfirst.html`

```sh
<!DOCTYPE html>
<html>
<body>

<h1>Hello World!</h1>
<p>Welcome to my first Django project!</p>

</body>
</html>
```

- Modify the View `my_tennis_club/members/views.py` to use `django.template import loader` insteadof `django.http import HttpResponse`

```sh
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
```

## Change Settings

- Setting needs to be adjusted to return output files so it needs to include the app first `my_tennis_club/my_tennis_club/settings.py`

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]
```

we can also migrate the required tables where as in setting file the db is connected to mysqlite3 file

```sh
py manage.py migrate
```

- now run the server and check the members <p style="color:red">not mail url but members</p>

## Django Models

data is created in objects, called Models, and is actually tables in a database.

## Create Table (Model)

- navigate to `my_tennis_club/members/models.py`

```sh
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
```

- till now the edit is on the model to allow ORM functions on it but table still not exist so in order to make that affect reflectes into tables we can use django command to create or edit the tables for that model or model edition by the next command that will create a corresponding file in the migration folder:

```sh
py manage.py makemigrations members
```

- then we should run the command to add the created table to the tabels in our case in sqlite

```sh
py manage.py migrate
```

- where we can check the sql view by next command

```sh
py manage.py sqlmigrate members 0001
```

## How to Insert Update Delete records in our DB

we can do all of the next CRUD operation from the view or controller and using the model but for now we will use shell offered by `manage.py` Dajango as tinker in laravel to check the model crude operations

### Insert Data

- enter the shell `py manage.py shell`
- import our required model `>>> from members.models import Member`
- using the model we required to get all its records `>>> Member.objects.all()` which in the first time will responce by empty array query
- now insert one record `member = Member(firstname='Emil', lastname='Refsnes')` and do not forget to save `member.save()`
- if you try to get the records or its values try `Member.objects.all().values()`
- now we can add multiple records as follows:

```sh
>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>>   x.save()
>>> Member.objects.all().values()
```

- To update the existing data or fields in record first we import the model then taget certain record from the table then assign to its fild the value then save as follows

```sh
from members.models import Member
x = Member.objects.all()[4]
x.firstname = "Stalikken"
x.save()
```

- To delete a record first we import the model then taget certain record from the table then delete it as follows

```sh
from members.models import Member
x = Member.objects.all()[5]
x.delete()
```

## If we have a model how to add fileds to it ?

To add a field to a table after it is created, open the models.py file, and make your changes `my_tennis_club/members/models.py`

```sh
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField()
  joined_date = models.DateField()
```

- as we edit the model so we need to create new migration for this modification `py manage.py makemigrations members`
- creating the modification especialy when adding columns that was not exists to table has values so it need initial values for the already existing records to this new field so it will ask you Qyuit and edit yourself or eh will sey defaults for your columns in previous recors so we select 2 Quite
- edit the file again to contain the default values as follows `my_tennis_club/members/models.py`:

```sh
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
```

- then make migration for the table and then run migrate

```sh
py manage.py makemigrations members
py manage.py migrate
```

- now we can access the new fields using `py manage.py shell`

```sh
from members.models import Member
x = Member.objects.all()[0]
x.phone = 5551234
x.joined_date = '2022-01-05'
x.save()
Member.objects.all().values()
```

## Display Data and Templating

we will create other templates to show list of members and then linking them to detailed pages for every one we will show how extending layout or master

- Create Template `my_tennis_club/members/templates/all_members.html`

```sh
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>
```

- the `{% %}` brackets inside the HTML document? They are Django Tags, telling Django to perform some programming logic inside these brackets.
- Modify View to include function for the new endpoint `my_tennis_club/members/views.py`

```sh
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
```

- Create Details Template `my_tennis_club/members/templates/details.html`

```sh
<!DOCTYPE html>
<html>

<body>

<h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>

<p>Phone: {{ mymember.phone }}</p>
<p>Member since: {{ mymember.joined_date }}</p>

<p>Back to <a href="/members">Members</a></p>

</body>
</html>
```

- Add Link in all-members Template `my_tennis_club/members/templates/all_members.html`

```sh
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>

<ul>
  {% for x in mymembers %}
    <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
  {% endfor %}
</ul>

</body>
</html>
```

- need for new template new view method `my_tennis_club/members/views.py`

```sh
my_tennis_club/members/views.py
```

- add urls for the new templates and view methods `my_tennis_club/members/urls.py`

```sh
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
```

## Layout/Master Template Django Add Master Template

- Django provides a way of making a "parent template" that you can include in all pages to do the stuff that is the same in all pages. and then extending it
- creating a template called `my_tennis_club/members/templates/master.html`

```sh
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>
```

- Modify Templates `my_tennis_club/members/templates/all_members.html`

```sh
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}
  <h1>Members</h1>

  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

- Modify Templates `my_tennis_club/members/templates/details.html`

```sh
{% extends "master.html" %}

{% block title %}
  Details about {{ mymember.firstname }} {{ mymember.lastname }}
{% endblock %}


{% block content %}
  <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>

  <p>Phone {{ mymember.phone }}</p>
  <p>Member since: {{ mymember.joined_date }}</p>

  <p>Back to <a href="/members">Members</a></p>

{% endblock %}
```

- run the server

## Django Add Main Index Page

- adding view for the nmain `127.0.0.1:8000/.`
- create `my_tennis_club/members/templates/main.html`
- - Create new View `my_tennis_club/members/views.py`

```sh
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
```

- Add URL `my_tennis_club/members/urls.py`

```sh
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
```

- Add Link Back to Main `my_tennis_club/members/templates/all_members.html`

```sh
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}

  <p><a href="/">HOME</a></p>

  <h1>Members</h1>

  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

## Django 404 (page not found)

Page Not Found
If you try to access a page that does not exist (a 404 error), Django directs you to a built-in view that handles 404 errors. In the browser window, type 127.0.0.1:8000/masfdfg/ in the address bar. You will get one of two results:

- if got error not 404 page this means that debug is true so we need to edit it in the seeting as follows to see 404 page `my_tennis_club/my_tennis_club/settings.py`

```sh
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
```

## Customize The 404 Template

Django will look for a file named 404.html in the templates folder, and display it when there is a 404 error. If no such file exists, Django shows the "Not Found" that you saw in the example above.

To customize this message, all you have to do is to create a file in the templates folder and name it 404 `my_tennis_club/members/templates/404.html`.html, and fill it with whatever you want:

```sh
<!DOCTYPE html>
<html>
<title>Wrong address</title>
<body>

<h1>Ooops!</h1>

<h2>I cannot find the file you requested!</h2>

</body>
</html>
```

## Django Add Test View

Test code without destroying the main project.

- Add View Start by adding a view called "testing" in the `my_tennis_club/members/views.py`

```sh
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))
```

- We have to make sure that incoming urls to /testing/ will be redirected to the testing view `my_tennis_club/members/urls.py`

```sh
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
```

- Create Test Template `my_tennis_club/members/templates/template.html`

```sh
<!DOCTYPE html>
<html>
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

<p>In views.py you can see what the fruits variable looks like.</p>

</body>
</html>
```

## Admin

Django Admin is a really great tool in Django, it is actually a CRUD\* user interface of all your models!
It is free and comes ready-to-use with Django:

- maybe need to set in `setting.py the debug to true` to allaow styling while it will resultrd in missing the routing to 404
- [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Create User: To be able to log into the admin application, we need to create a user. This is done by typing this command in the command view

```sh
py manage.py createsuperuser
```

## Django Admin - Include Modules (members)

- in the admin now we did not see the member app so we need to tell django admin about it
- To include the Member model in the admin interface, we have to tell Django that this model should be visible in the admin interface.
- This is done in a file called admin.py, and is located in your app's folder, which in our case is the members folder.
- Insert a couple of lines here to make the Member model visible in the admin page `my_tennis_club/members/admin.py`

```sh
from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.register(Member)
```

- now we should see the module in the admin panel

## Make the List Display More Reader-Friendly

When you display a Model as a list, Django displays each record as the string representation of the record object, which in our case is "Member object (1)", "Member object(2)" etc

<p style="color:red">Note in python main principle when you check the type of a variavle and it was a class the reurn from the class is object nature may be in readable so to return something readable we can use '__str__' where we can define the data returned when this class is called and we also need to note the use of __iter__ that is used in iteration with next() that make array or list iteratable such as __init__ as a constructor for OOP</P>
To change this to a more reader-friendly format, we have two choices:

Change the string representation function, `__str__()` of the Member Model
Set the list_details property of the Member Model `my_tennis_club/members/models.py`

```sh
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
```

- Defining our own **str**() function is not a Django feature, it is how to change the string representation of objects in Python.

- Set list_display : We can control the fields to display by specifying them in in a list_display property in the admin.py file.
- First create a MemberAdmin() class and specify the list_display tuple, like this `my_tennis_club/members/admin.py`

```sh
from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Member, MemberAdmin)
```

## Update Members

- Now we are able to create, update, and delete members in our database, and we start by giving them all a date for when they became members from the admin panel

## Django Syntax

Template Variables
In Django templates, you can render variables by putting them inside`{{ }}`brackets
