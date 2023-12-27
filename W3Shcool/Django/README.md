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

- Template Variables: In Django templates, you can render variables by putting them inside`{{ }}`brackets
- Django Template Tags: In Django templates, you can perform programming logic like executing if statements and for loops. These keywords, if and for, are called "template tags" in Django. To execute template tags, we surround them in {% %} brackets.
-

```sh
{% if greeting == 1 %}
  <h1>Hello</h1>
{% else %}
  <h1>Bye</h1>
{% endif %}
```

- Django Code
  The template tags are a way of telling Django that here comes something else than plain HTML. The template tags allows us to to do some programming on the server before sending HTML to the client.

```sh
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>
```

## Tag Reference: A list of all template tags:

<table>
<tbody>
<tr><th>Tag</th><th>Description</th><th><th></tr>
<tr><th>autoescape</th><th>Specifies if autoescape mode is on or off</th></tr>
<tr><th>block</th><th>Specifies a block section</th></tr>
<tr><th>comment</th><th>Specifies a comment section</th></tr>
<tr><th>csrf_token</th><th>Protects forms from Cross Site Request Forgeries</th></tr>
<tr><th>cycle</th><th>Specifies content to use in each cycle of a loop</th></tr>
<tr><th>debug</th><th>Specifies debugging information</th></tr>
<tr><th>extends</th><th>Specifies a parent template</th></tr>
<tr><th>filter</th><th>Filters content before returning it</th></tr>
<tr><th>firstof</th><th>Returns the first not empty variable</th></tr>
<tr><th>for</th><th>Specifies a for loop</th></tr>
<tr><th>if</th><th>Specifies a if statement</th></tr>
<tr><th>ifchanged</th><th>Used in for loops. Outputs a block only if a value has changed since the last iteration</th></tr>
<tr><th>include</th><th>Specifies included content/template</th></tr>
<tr><th>load</th><th>Loads template tags from another library</th></tr>
<tr><th>lorem</th><th>Outputs random text</th></tr>
<tr><th>now</th><th>Outputs the current date/time</th></tr>
<tr><th>regroup</th><th>Sorts an object by a group</th></tr>
<tr><th>resetcycle</th><th>Used in cycles. Resets the cycle</th></tr>
<tr><th>spaceless</th><th>Removes whitespace between HTML tags</th></tr>
<tr><th>templatetag</th><th>Outputs a specified template tag</th></tr>
<tr><th>url</th><th>Returns the absolute URL part of a URL</th></tr>
<tr><th>verbatim</th><th>Specifies contents that should not be rendered by the template engine</th></tr>
<tr><th>widthratio</th><th>Calculates a width value based on the ratio between a given value and a max value</th></tr>
<tr><th>with</th><th>Specifies a variable to use in the block</th></tr>
</tbody>
</table>

### autoescape

```sh
{% autoescape off %}
  <h1>{{ heading }}</h1>
{% endautoescape %}
```

When escape is on, these characters are escaped:

- < is converted to &lt;
- symbole > is converted to &gt;
- ' is converted to '
- " is converted to "
- & is converted to &amp;

### block

Define a section in a master template that should be replaced by a section in a child template:

```sh
<!DOCTYPE html>
<html>
<body>
<h1>Welcome</h1>

{% block userinfo %}
  <h2>Not registered yet</h2>
{% endblock %}

</body>
</html>
```

The block tag has two functions:

1. It is a placeholder for content.
2. It is content that will replace the placeholder.
   In master templates the block tag is a placeholder that will be replaced by a block in a child template with the same name.

In child templates the block tag is content that will replace the placeholder in the master template with the same name.

In the example above you see the content of a master template, it has a block called userinfo. This block will be replaced with a block called userinfo in a child template:

```sh
{% extends "mymaster.html" %}

{% block userinfo %}
  <h2>John Doe</h2>
  <p>Explorer of life.</p>
{% endblock %}
```

### comment

Insert a comment in the Django code:
Definition and Usage
The comment tag allows you to add comment sections that will be ignored by Django. Comments can be used to make the code more readable. Comments can be used to prevent execution when testing code. You can add an explanation to your comments to make them more understandable:

```sh
<h1>Welcome Everyone!</h1>

{% comment %}
  <h1>Greetings!</h2>
{% endcomment %}
```

Add an explanation to your comment:

```sh

<h1>Welcome Everyone!</h1>

{% comment "optional heading" %}
  <h1>Greetings!</h2>
{% endcomment %}
```

### csrf_token

```sh

```

### cycle

Add a new color for each iteration in a for loop

```sh
<ul>
{% for x in fruits %}
  <li style='color:{% cycle 'red' 'green' 'blue' 'pink' %}'>
    {{ x }}
  </li>
{% endfor %}
</ul>
```

Definition and Usage
The cycle tag returns different values for different iterations in a loop. The first iteration gets the first value, the second iteration gets the second value etc. You can have as many values as you like. If there are more iterations that values, the cycle resets and starts at value 1

```sh
<ul>
{% for x in fruits %}
  <li style='color:{% cycle 'red' 'blue' %}'>
    {{ x }}
  </li>
{% endfor %}
</ul>
```

`{% cycle arg1 arg2 arg3 etc. %}`

### debug

### extends

Specify that this template relies on a parent template

```sh
{% extends "mymaster.html" %}

{% block heading %}
  <h2>John Doe</h2>
  <p>Explorer of life</p>
{% endblock %}

{% block cars %}
  <li>Ford</li>
  <li>Volvo</li>
  <li>Audi</li>
{% endblock %}
```

Definition and Usage
The extends tag is used to specify that this template needs a parent template.

The extends tag takes one argument, which is the name of the parent template.

When a child template with a parent template is requested, Django uses the parent template as a "skeleton" and fills it with content from the child template, according to the matching block tags.

```sh
<!DOCTYPE html>
<html>
<body>

<h1>Welcome</h1>
<hr>

{% block heading %}
  <h2>No name</h2>
{% endblock %}

<h2>My Cars</h2>

<ul>
  {% block cars %}
    <li>No cars</li>
  {% endblock %}
</ul>

</body>
</html>
```

`{% extends parenttemplate %}`

### filter

Output text in upper case:

```sh
<h1>Welcome Everyone!</h1>

{% filter upper %}
  <p>Have a great day!</p>
{% endfilter %}
```

Definition and Usage
The filter tag allows you to run a section of code through a filter, and return it according to the filter keyword(s).

To add multiple filters, separate the keywords with the pipe | character.

```sh
{% filter keyword %}
  ...
{% endfilter %}
```

Parameters
The filter tag takes any of these keywords as parameter(s):

<table>
<tbody>

<tr><th>Keyword</th><th>Description</th></tr>
<tr><th>add	</th><th>Adds a specified value.</th></tr>
<tr><th>addslashes</th><th>	Adds a slash before any quote characters, to escape strings.</th></tr>
<tr><th>capfirst</th><th>	Returns the first letter in uppercase.</th></tr>
<tr><th>center	</th><th>Centers the value in the middle of a specified width.</th></tr>
<tr><th>cut	</th><th>Removes any specified character or phrases.</th></tr>
<tr><th>date	</th><th>Returns dates in the specified format.</th></tr>
<tr><th>default	</th><th>Returns a specified value if the value is False.</th></tr>
<tr><th>default_if_none	</th><th>Returns a specified value if the value is None.</th></tr>
<tr><th>dictsort	</th><th>Sorts a dictionary by the given value.</th></tr>
<tr><th>dictsortreversed	</th><th>Sorts a dictionary reversed, by the given value.</th></tr>
<tr><th>divisibleby	</th><th>Returns True if the value can be divided by the specified number, otherwise it returns False.</th></tr>
<tr><th>escape	</th><th>Escapes HTML code from a string.</th></tr>
<tr><th>escapejs	</th><th>Escapes JavaScript code from a string.</th></tr>
<tr><th>filesizeformat	</th><th>Returns a number into a file size format.</th></tr>
<tr><th>first	</th><th>Returns the first item of an object (for Strings, the first character is returned).</th></tr>
<tr><th>floatformat	</th><th>Rounds floating numbers to a specified number of decimals, default one decimal.</th></tr>
<tr><th>force_escape	</th><th>Escapes HTML code from a string.</th></tr>
<tr><th>get_digit	</th><th>Returns a specific digit of a number.</th></tr>
<tr><th>iriencode	</th><th>Convert an IRI into a URL friendly string.</th></tr>
<tr><th>join	</th><th>Returns the items of a list into a string</th></tr>
<tr><th>json_script	</th><th>Returns an object into a JSON object surrounded by <script></script> tags.</th></tr>
<tr><th>last	</th><th>Returns the last item of an object (for Strings, the last character is returned).</th></tr>
<tr><th>length	</th><th>Returns the number of items in an object, or the number of characters in a string.</th></tr>
<tr><th>length_is	</th><th>Returns True if the length is the same as the specified number</th></tr>
<tr><th>linebreaks	</th><th>Returns the text with <br> instead of line breaks, and <p> instead of more than one line break.</th></tr>
<tr><th>linebreaksbr	</th><th>Returns the text with <br> instead of line breaks.</th></tr>
<tr><th>linenumbers	</th><th>Returns the text with line numbers for each line.</th></tr>
<tr><th>ljust	</th><th>Left aligns the value according to a specified width</th></tr>
<tr><th>lower	</th><th>Returns the text in lower case letters.</th></tr>
<tr><th>make_list	</th><th>Converts a value into a list object.</th></tr>
<tr><th>phone2numeric	</th><th>Converts phone numbers with letters into numeric phone numbers.</th></tr>
<tr><th>pluralize	</th><th>Adds a 's' at the end of a value if the specified numeric value is not 1.</th></tr>
<tr><th>pprint	 </th><th></th></tr>
<tr><th>random	</th><th>Returns a random item of an object</th></tr>
<tr><th>rjust	</th><th>Right aligns the value according to a specified width</th></tr>
<tr><th>safe	</th><th>Marks that this text is safe and should not be HTML escaped.</th></tr>
<tr><th>safeseq	</th><th>Marks each item of an object as safe and the item should not be HTML escaped.</th></tr>
<tr><th>slice	</th><th>Returns a specified slice of a text or object.</th></tr>
<tr><th>slugify	</th><th>Converts text into one long alphanumeric-lower-case word.</th></tr>
<tr><th>stringformat	</th><th>Converts the value into a specified format.</th></tr>
<tr><th>striptags	</th><th>Removes HTML tags from a text.</th></tr>
<tr><th>time	</th><th>Returns a time in the specified format.</th></tr>
<tr><th>timesince	</th><th>Returns the difference between two datetimes.</th></tr>
<tr><th>timeuntil	</th><th>Returns the difference between two datetimes.</th></tr>
<tr><th>title	</th><th>Upper cases the first character of each word in a text, all other characters are converted to lower case.</th></tr>
<tr><th>truncatechars	</th><th>Shortens a string into the specified number of characters.</th></tr>
<tr><th>truncatechars_html	</th><th>Shortens a string into the specified number of characters, not considering the length of any HTML tags.</th></tr>
<tr><th>truncatewords	</th><th>Shortens a string into the specified number of words.</th></tr>
<tr><th>truncatewords_html	</th><th>Shortens a string into the specified number of words, not considering any HTML tags.</th></tr>
<tr><th>unordered_list	</th><th>Returns the items of an object as an unordered HTML list.</th></tr>
<tr><th>upper	</th><th>Returns the text in upper case letters.</th></tr>
<tr><th>urlencode	</th><th>URL encodes a string.</th></tr>
<tr><th>urlize	</th><th>Returns any URLs in a string as HTML links.</th></tr>
<tr><th>urlizetrunc	</th><th>Returns any URLs in a string as HTML links, but shortens the links into the specified number of characters.</th></tr>
<tr><th>wordcount	</th><th>Returns the number of words in a text.</th></tr>
<tr><th>wordwrap	</th><th>Wrap words at a specified number of characters.</th></tr>
<tr><th>yesno	</th><th>Converts Booleans values into specified values.</th></tr>
<tr><th>i18n	</th><th></th></tr> 
<tr><th>l10n	</th><th></th></tr> 
<tr><th>tz	 </th><th></th></tr>
</tbody>
</table>

### firstof

Return the first of the three variables (x, y, z) whose value is not empty or false

```sh
<h1>
{% firstof x y z %}
</h1>
```

Definition and Usage
The firstof tag returns the first argument that is not an empty variable.

Empty variables can be an empty string "", or a zero number 0, or a boolean false.

```sh
<h1>
{% firstof x y z %}
</h1>
```

`{% firstof var1 var2 var3 etc. %}`

### for

Loop through a list and display the values

```sh
<ul>
  {% for x in fruits %}
    <li>{{ x }}</li>
  {% endfor %}
</ul>
```

Definition and Usage
The for tag allows you to iterate over items in an object.

Objects can be array-like objects like a Python list or object-like objects like a Python dictionary:

```sh
{% for x, y in mycar.items %}
  <p>The {{ x }} is {{ y }}.</p>
{% endfor %}
```

`{% for item in object %}
...
{% endfor %}`

Built-in for Variables
There are some built-in variables you can use inside for loops:

<table>
<tbody>
<tr><th>Variable</th><th>Description</th></tr>	
<tr><th>forloop.counter</th><th>The current iteration, starting at 1.</th></tr>	
<tr><th>forloop.counter0</th><th>The current iteration, starting at 0.</th></tr>	
<tr><th>forloop.first</th><th>Check if this iteration is the first iteration.</th></tr>	
<tr><th>forloop.last</th><th>Check if this iteration is the last iteration.</th></tr>	
<tr><th>forloop.parentloop</th><th>Refers to the parent loop.</th></tr>	
<tr><th>forloop.revcounter</th><th>The current iteration, counting backwords, ending at 1.</th></tr>	
<tr><th>forloop.revcounter0</th><th>The current iteration, counting backwords, ending at 0.</th></tr>
</tbody>
</table>

### if

Display a header if the value of the myvar variable is 1:

```sh
{% if myvar == 1 %}
  <h1>Hello!</h1>
{% endif %}
```

Definition and Usage
The if tag allows you to write conditional statements.

Use if statements to output a block of code if a condition is true.

You can use else or elif (short for "else if") to specify what to do when the if condition is false.

```sh
{% if myvar == 1 %}
  <h1>Hello!</h1>
{% else %}
  <h1>Greetings!</h1>
{% endif %}
```

Display a third heading if none of the conditions are true

```sh
{% if myvar == 1 %}
  <h1>Hello!</h1>
{% elif myvar == 2 %}
  <h1>Welcome!</h1>
{% else %}
  <h1>Greetings!</h1>
{% endif %}
```

`{% if condition %}
...
{% endif %}`

Operators
There are some built-in operators you can use when evaluating if statements:

<table>
<tbody>
<tr><th>Variable</th><th>Description</th></tr>	
<tr><th>==</th><th>is equal to</th></tr>	
<tr><th>!=</th><th>is not equal to</th></tr>	
<tr><th><</th><th>is less than</th></tr>	
<tr><th><=</th><th>is less than, or equal to</th></tr>	
<tr><th>></th><th>is greater than</th></tr>	
<tr><th>>=</th><th>is greater than, or equal to</th></tr>	
<tr><th>and</th><th>condition1 and condition2 must be true</th></tr>	
<tr><th>or</th><th>condition1 or condition2 must be true</th></tr>	
<tr><th>in</th><th>an item must be present in an object</th></tr>	
<tr><th>is</th><th>is the same value as</th></tr>	
<tr><th>is</th><th>not	is not the same value as</th></tr>	
<tr><th>not</th><th>in	is not in</th></tr>
</tbody>
</table>

### ifchanged

Loop through a list, but display the value only if it has changed since the last iteration

```sh
<ul>
  {% for x in mylist %}
    {% ifchanged %}
      <li>{{ x }}</li>
    {% endifchanged %}
  {% endfor %}
</ul>
```

Definition and Usage
The ifchanged tag allows you to check a value in a loop and output a code if the value has changed since the last iteration.

If the iteration object has many values per iteration, you can specify which value to check, and the block of code will only displayed if that value has changed since the last iteration

Loop through the members object and check if the brand property has changed

```sh
{% for x in cars %}
  {% ifchanged x.brand %}
    <h1>{{ x.brand }}:</h1>
  {% endifchanged %}
  <p>{{ x.model }}, {{ x.year }}</p>
{% endfor %}
```

You can also define an {% else %} clause for content that should be displayed if the value has not changed

```sh
{% for x in mylist %}
  {% ifchanged %}
    <p>New value: {{ x }}</p>
  {% else %}
    <p>Same value: {{ x }}</p>
  {% endifchanged %}
{% endfor %}
```

`{% ifchanged property %}
...
{% endifchanged %}`

### include

Include a template inside the template

```sh
<!DOCTYPE html>
<html>
<body>

{% include mymenu.html %}

<h1>Welcome</h1>

<p>This is my webpage</p>

</body>
</html>
```

Definition and Usage
The include tag allows you to include content from another template.

Place the include tag exactly where you want the content to be displayed.

This is useful when you have the same content for many pages.

You can also send variables into the template, by using the with keyword

If the include file looks like this

`<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>`

The template can send variable values into the include like this

```sh
<!DOCTYPE html>
<html>
<body>

{% include mymenu.html with me="ALEXANDER" sponsor="W3SCHOOLS" %}

<h1>Welcome</h1>

<p>This is my webpage</p>

</body>
</html>
```

`{% include template %}`

or

`{% include template with key=value%}`

### load

### lorem

Insert 50 words of random text

```sh
<!DOCTYPE html>
<html>
<body>

{% lorem 50 w %}

</body>
</html>
```

Definition and Usage
The lorem tag inserts a specified amount of random text.

The "random" text is the famous "Lorum ipsum" text, in lower case letters

Insert 5 paragraphs of random text

```sh
<!DOCTYPE html>
<html>
<body>

{% lorem 5 p %}

</body>
</html>
```

```sh
{% lorem count method random %}
```

### now

Add the current date

```sh
<!DOCTYPE html>
<html>
<body>

<h1>{% now "Y-m-d" %}</h1>

</body>
</html>
```

Definition and Usage
The now tag inserts the current date and/or time, according to the specified format.

Example Add the current date and time

```sh
<!DOCTYPE html>
<html>
<body>

<h1>{% now "Y-m-d G:i:s" %}</h1>

</body>
</html>
```

`{% now format %}`

<table>
<tbody>
<tr><th>Value</th><th>Description</th></tr>
<tr><th>format</th><th>Required. A string with any combination of these characters:</th></tr>
<tr><th>Character</th><th>Description</th></tr>
<tr><th>y</th><th>Year, 2 digits (00-99)</th></tr>
<tr><th>Y</th><th>Year, 4 digits (0001-9999)</th></tr>
<tr><th>L</th><th>Returns whether now is a leap year or not (True-False)</th></tr>
<tr><th>m</th><th>Month, 2 digits (01-12)</th></tr>
<tr><th>n</th><th>Month, 1 or 2 digits (1-12)</th></tr>
<tr><th>M</th><th>Month, 3 letters (Jan-Dec)</th></tr>
<tr><th>b</th><th>Month, 3 lower case letters (jan-dec)</th></tr>
<tr><th>E</th><th>Month, text in local language</th></tr>
<tr><th>F</th><th>Month, full text (January-December)</th></tr>
<tr><th>N</th><th>Month, max 5 letters, if month name has more, use proper abbreviation (Jan. Dec.)</th></tr>
<tr><th>t</th><th>Number of days in month (28-31)</th></tr>
<tr><th>d</th><th>Day of month (01-31)</th></tr>
<tr><th>D</th><th>Day of week (Sun-Sat)</th></tr>
<tr><th>j</th><th>Day of month (1-31)</th></tr>
<tr><th>l</th><th>Day of week (Sunday-Saturday)</th></tr>
<tr><th>S</th><th>Ending of number (st-nd-rd-th)</th></tr>
<tr><th>w</th><th>Day of week (0-6)</th></tr>
<tr><th>z</th><th>Day of year (1-366)</th></tr>
<tr><th>W</th><th>Week of year (ISO-8601) (1-53)</th></tr>
<tr><th>g</th><th>Hour (1-12)</th></tr>
<tr><th>G</th><th>Hour (0-23)</th></tr>
<tr><th>h</th><th>Hour (01-12)</th></tr>
<tr><th>H</th><th>Hour (00-23)</th></tr>
<tr><th>i</th><th>Minutes (00-59)</th></tr>
<tr><th>s</th><th>Seconds (00-59)</th></tr>
<tr><th>u</th><th>Microseconds (000000-999999)</th></tr>
<tr><th>a</th><th>Meridiem (a.m. or p.m.)</th></tr>
<tr><th>A</th><th>Meridiem (A.M. or P.M.)</th></tr>
<tr><th>f</th><th>The Time (9:45). If the time is precisely (on the minute) nine, it returns only the hour (9)</th></tr>
<tr><th>P</th><th>The Time (9:45 p.m.). If the time is precisely (on the minute) nine, it returns (9 p.m.). If the time is precisely 0:00, it returns (midnight). If the time is precisely 12:00 it returns (noon).</th></tr>
<tr><th>e</th><th>Name of time zone, like (GMT) or (UTC)</th></tr>
<tr><th>I</th><th>Returns whether we are in daylight saving time or not (1 or 0)</th></tr>
<tr><th>O</th><th>The difference to GMT (+0500)</th></tr>
<tr><th>T</th><th>Local time zone, like (UTC) or (EST)</th></tr>
<tr><th>Z</th><th>Difference to GMT, in seconds (3600)</th></tr>
<tr><th>c</th><th>Current date in ISO 8601 format (2022-04-05T12:38:30.797643+00:00)</th></tr>
<tr><th>r</th><th>Current date in RFC 5322 format (Tue, 05 Apr 2022 12:39:24 +0000)</th></tr>
<tr><th>U</th><th>Seconds since January 1 1970 00:00:00</th></tr>
</tbody>
</table>

### regroup

Display all the cars with a new header for each brand

```sh
{% regroup cars by brand as newlist %}

{% for x in newlist %}
  <h1>{{ x.grouper }}</h1>
  {% for y in x.list %}
    <p>{{ y.model }}: {{ y.year }}</p>
  {% endfor %}
{% endfor %}
```

Definition and Usage
The regroup tag returns a new object grouped by a specified value.

The result is divided into one GroupedResult object for each group, making the newlist object from the example above, looking like this

The result from {% regroup cars by brand as newlist %}

```sh
[
  GroupedResult(
    grouper='Ford',
    list=[
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964'
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970'
      },
      {
        'brand': 'Ford',
        'model': 'Sierra',
        'year': '1981'
      }
    ]
  ),
  GroupedResult(
    grouper='Volvo',
    list=[
      {
        'brand': 'Volvo',
        'model': 'XC90',
        'year': '2016'
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964'
      }
    ]
  )
]
```

<p style="color:yellow">Note: Make sure the object is sorted correctly before regrouping, otherwise you will end up with groups with the same grouper name</p>

`{% regroup object by object.property as newname %}`

<table>
<tbody>
<tr><th>Value</th><th>Description</th></tr>
<tr><th>object	Required.</th><th> A list or object taht you want to regroup</th></tr>
<tr><th>object.property	Required.</th><th> The name of the property you want to group by</th></tr>
<tr><th>newname</th><th>	Required. A new name for the returned object</th></tr>
</tbody>
</table>

### resetcycle

Reset the cycle if the fruit is "Banana":

```sh
<ul>
  {% for x in fruits %}
    <li style='color:{% cycle 'red' 'green' 'blue' 'pink' %}'>
      {{ x }}
    </li>
    {% if x == "Banana" %}
      {% resetcycle %}
    {% endif %}
  {% endfor %}
</ul>
```

Definition and Usage
The resetcycle tag is used inside a cycle, and resets the cycle, making it start at the beginning.

It does not reset the loop, only the cycle.

If you have multiple cycles, you can specify which one to reset with the name argument

Reset the mybg cycle if the fruit is "Banana"

```sh
<ul>
  {% for x in fruits %}
    <li style='
      color:{% cycle 'red' 'green' 'blue' 'pink' as mycolor %};
      background:{% cycle 'grey' 'beige' 'coral' 'brown' as mybg %};
    '>{{ x }}</li>
    {% if x == "Banana" %}
      {% resetcycle mybg %}
    {% endif %}
  {% endfor %}
</ul>
```

`{% resetcycle name %}`

### spaceless

Remove the space between the HTML tags

```sh
{% spaceless %}
  <ul>
    {% for x in fruits %}
      <li>{{ x }}</li>
    {% endfor %}
  </ul>
{% endspaceless %}
```

Definition and Usage
The spaceless tag is used to remove any space between tags, in the code.

The spaceless tag removes any whitespaces, new lines and tabs

`{% spaceless %}
...
{% endspaceless %}`

### templatetag

Output Django code without execute it

```sh
<h1>
  {% templatetag openblock %}
    extends
  {% templatetag closeblock %}
</h1>
```

Definition and Usage
The templatetag tag is used to display characters that are normally used to perform Django tasks.

Each tag character, like `{{, {% and {#, has their own name, see below`

`{% templatetag name %}`

Parameters

<table >
  <tbody><tr>
    <th >Value</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><em>name</em></td>
    <td>Required. A string specifying what to ouput.<br><br>
    <table class="plaintable">
    <tbody><tr>
    <th>Name</th>
    <th>Output</th>
    </tr>
    <tr>
    <td><code class="w3-codespan">openvariable</code></td>
    <td>{{</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">closevariable</code></td>
    <td>}}</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">openblock</code></td>
    <td>{%</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">closeblock</code></td>
    <td>%}</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">openbrace</code></td>
    <td>{</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">closebrace</code></td>
    <td>}</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">opencomment</code></td>
    <td>{#</td>
    </tr>
    <tr>
    <td><code class="w3-codespan">closecomment</code></td>
    <td>#}</td>
    </tr>
    </tbody></table>
  </td></tr>
</tbody></table>

### url

### verbatim

Output Django code without execute it

```sh
{% verbatim %}
  {% for x in fruits %}
    <p>{{ x }}</p>
  {% endfor %}
{% endverbatim %}
```

Definition and Usage
The verbatim tag is used to stop Django from executing code.

Anything between {% verbatim %} and {% endverbatim %} will not be executed, but rendered as output instead.

To be sure that you refer to the correct verbatim code block, you can add a name to it:

Example
When there can be more than one verbatim tag in a code block, use the name argument to specify which one you mean

```sh
{% verbatim mycode%}
  {% for x in fruits %}
    {% verbatim %}
       <p>{{ x }}</p>
    {% endverbatim %}
  {% endfor %}
{% endverbatim mycode%}
```

`{% verbatim name %}
...
{% endverbatim %}`

### widthratio

### with

Create a variable in the template, and use it

```sh
{% with firstname="Stalikken" %}
  <h1>Hello {{ firstname }}</h1>
{% endwith %}
```

Definition and Usage
The with tag is used to create variables in Django templates.

This can be useful when you need to ask for the same variable many times, like in a loop:

Example
Use the with tag to get the length of fruits only one time

```sh
{% with myvar=fruits|length %}
  {% for x in fruits %}
    <p>{{ x }} is one of {{ myvar }} fruits.</p>
  {% endfor %}
{% endwith %}
```

`{% with var1=val1 var2=val2 var3=val3 etc. %}
...
{% endwith %}`

<table>
<tbody>
<tr><th>Value</th><th>Description</th></tr>
<tr><th>var1=val1 var2=val2 var3=val3 etc.</th><th>Required. Declaring variable(s) and their value(s).</th></tr>
</tbody>
</table>

## Django QuerySet

A QuerySet is a collection of data from a database.

A QuerySet is built up as a list of objects.

QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.

In this tutorial we will be querying data from the Member table

Querying Data
In views.py, we have a view for testing called testing where we will test different queries.

In the example below we use the .all() method to get all the records and fields of the Member model

As you can see, our Member model contains 5 records, and are listed inside the QuerySet as 5 objects.

In the template you can use the mymembers object to generate content

`templates/template.html`

```sh
<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>
```

### Get Data

There are different methods to get data from a model into a QuerySet.

### The values() Method

The values() method allows you to return each object as a Python dictionary, with the names and values as key/value pairs:

ExampleGet your own Django Server `views.py`

```sh
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
```

### Return Specific Columns

The values_list() method allows you to return only the columns that you specify

Return only the records where firstname is 'Emil'

```sh
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.filter(firstname='Emil').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
```

### Django QuerySet - Filter

The filter() method is used to filter your search, and allows you to return only the rows that matches the search term.

As we learned in the previous chapter, we can filter on field names like this:

ExampleGet your own Django Server
Return only the records where the firstname is 'Emil'

- > mydata = Member.objects.filter(firstname='Emil').values()
- in sql
- > SELECT \* FROM members WHERE firstname = 'Emil';

### AND

The filter() method takes the arguments as \*\*kwargs (keyword arguments), so you can filter on more than one field by separating them by a comma.

Example
Return records where lastname is "Refsnes" and id is 2

- > mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
- in Sql
- > SELECT \* FROM members WHERE lastname = 'Refsnes' AND id = 2;

### OR

To return records where firstname is Emil or firstname is Tobias (meaning: returning records that matches either query, not necessarily both) is not as easy as the AND example above.

We can use multiple filter() methods, separated by a pipe | character. The results will merge into one model.

Example
Return records where firstname is either "Emil" or Tobias"

- > mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
- Another common method is to import and use Q expressions: Example Return records where firstname is either "Emil" or Tobias"

```sh
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def testing(request):
  mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
```

- In SQL, the above statement would be written like this
- > SELECT \* FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';

### Field Lookups

Django has its own way of specifying SQL statements and WHERE clauses.

To make specific where clauses in Django, use "Field lookups".

Field lookups are keywords that represents specific SQL keywords.

Example:
Use the \_\_startswith keyword

- > .filter(firstname\_\_startswith='L');
- in sql
- > WHERE firstname LIKE 'L%'
- The above statement will return records where firstname starts with 'L'

### Field Lookups Syntax

All Field lookup keywords must be specified with the fieldname, followed by two(!) underscore characters, and the keyword.

In our Member model, the statement would be written like this:

Example
Return the records where firstname starts with the letter 'L'

- > mydata = Member.objects.filter(firstname\_\_startswith='L').values()

### Field Lookups Reference

A list of all field look up keywords:

<table>
<tbody>
<tr><th>Keyword</th><th>Description</th></tr>
<tr><td>contains</td><td>Contains the phrase</td></tr>
<tr><td>icontains</td><td>Same as contains, but case-insensitive</td></tr>
<tr><td>date</td><td>Matches a date</td></tr>
<tr><td>day</td><td>Matches a date (day of month, 1-31) (for dates)</td></tr>
<tr><td>endswith</td><td>Ends with</td></tr>
<tr><td>iendswith</td><td>Same as endswidth, but case-insensitive</td></tr>
<tr><td></td><td>An exact match</td></tr>
<tr><td>iexact</td><td>Same as exact, but case-insensitive</td></tr>
<tr><td></td><td>Matches one of the values</td></tr>
<tr><td>isnull</td><td>Matches NULL values</td></tr>
<tr><td></td><td>Greater than</td></tr>
<tr><td>gte</td><td>Greater than, or equal to</td></tr>
<tr><td>hour</td><td>Matches an hour (for datetimes)</td></tr>
<tr><td>lt</td><td>Less than</td></tr>
<tr><td>lte</td><td>Less than, or equal to</td></tr>
<tr><td>minute</td><td>Matches a minute (for datetimes)</td></tr>
<tr><td>month</td><td>Matches a month (for dates)</td></tr>
<tr><td>quarter</td><td>Matches a quarter of the year (1-4) (for dates)</td></tr>
<tr><td>range</td><td>Match between</td></tr>
<tr><td>regex</td><td>Matches a regular expression</td></tr>
<tr><td>iregex</td><td>Same as regex, but case-insensitive</td></tr>
<tr><td>second</td><td>Matches a second (for datetimes)</td></tr>
<tr><td>startswith</td><td>Starts with</td></tr>
<tr><td>istartswith</td><td>Same as startswith, but case-insensitive</td></tr>
<tr><td>time</td><td>Matches a time (for datetimes)</td></tr>
<tr><td>week</td><td>Matches a week number (1-53) (for dates)</td></tr>
<tr><td>week_day</td><td>Matches a day of week (1-7) 1 is sunday</td></tr>
<tr><td>iso_week_day</td><td>Matches a ISO 8601 day of week (1-7) 1 is monday</td></tr>
<tr><td>year</td><td>Matches a year (for dates)</td></tr>
<tr><td>iso_year</td><td>Matches an ISO 8601 year (for dates)</td></tr>
</tbody>
</table>

### Django QuerySet - Order By

To sort QuerySets, Django uses the order_by() method:

ExampleGet your own Django Server
Order the result alphabetically by firstname

- > mydata = Member.objects.all().order_by('firstname').values()
- In SQL,
- > SELECT \* FROM members ORDER BY firstname;

### Descending Order

By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name:

Example
Order the result firstname descending

- > mydata = Member.objects.all().order_by('-firstname').values()
- in sql
- > SELECT \* FROM members ORDER BY firstname DESC;

### Multiple Order Bys

To order by more than one field, separate the fieldnames with a comma in the order_by() method:

Example
Order the result first by lastname ascending, then descending on id

- > mydata = Member.objects.all().order_by('lastname', '-id').values()
- in sql
- > SELECT \* FROM members ORDER BY lastname ASC, id DESC;
