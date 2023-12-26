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


