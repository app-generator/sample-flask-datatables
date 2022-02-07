# [Flask DataTables Sample](https://blog.appseed.us/flask-data-tables-open-source-sample/)

Open-source sample provided by [AppSeed](https://appseed.us). The project implements [paginated access to data using Flask](https://blog.appseed.us/flask-data-tables-open-source-sample/) and **Simple-DataTables**, a lightweight, extendable, dependency-free javascript HTML table plugin (no jQuery dependency).

<br />

> Features:

- DataTables managed by `Simple-DataTables`  (Vanilla) JS
- Stack: Flask, SqlAlchemy, Flask-Migrate, Flask-RestX
- Data Tables Implementation(s):
  - Loaded from `Data` table by a controller (route)
  - Served by `/api/data` API node and consumed from JS
  - Loaded without any processing from a file:
    - `app/static/datatables/data.json`
  - Inline Edit / Delete
- UI Kit: **Volt Dashboard** (Free Version) by **Themesberg**
- Deployment scripts: Docker, Gunicorn/Nginx, HEROKU
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Links:

- 👉 [Flask DataTables Sample](#) - LIVE Demo (coming soon)
- 👉 More [Free Samples](https://appseed.us/admin-dashboards/open-source) - provided by AppSeed

<br />

## ✨ Quick Start in `Docker`

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-volt-datatables.git
$ cd flask-volt-datatables
```

> Start the app in Docker

```bash
$ docker-compose up --build 
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

![Flask DataTables Sample - Open-Source Sample Project provided by AppSeed.](https://user-images.githubusercontent.com/51070104/152824173-a55c9ddd-e282-4dac-bd59-07b27c41269a.gif)

<br />

## ✨ How to use it

> Clone Sources (this repo)

```bash
$ git clone https://github.com/app-generator/flask-volt-datatables.git
$ cd flask-volt-datatables
```

<br />

> Install Modules using a Virtual Environment

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

Or for **Windows-based Systems**

```bash
$ virtualenv env
$ .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
```

<br />

> Set up the environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

Or for **Windows-based Systems**

```bash
$ # CMD terminal
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Load Sample Data `media/data.csv`

```bash
$ flask load_data  # randomize the timestamp
// OR
$ flask load_random_data  # randomize the timestamp and values
```

<br />

> Start the APP

```bash
$ flask run 
```

The paginated information is available in three ways: 

- Loaded from `Data` table by a controller (route)
- Served by `/api/data` API node and consumed from JS
- Loaded without any processing from a file:
  - `app/static/datatables/data.json`  

<br />
## Code-base structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- app/__init__.py
   |-- app/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |  index.html                      # The default page
   |    |  login.html                      # Auth Login Page
   |    |  register.html                   # Auth Registration Page
   |    |  page-404.html                   # Error 404 page (page not found)
   |    |  page-500.html                   # Error 500 page (server error)
   |    |    *.html                        # All other pages provided by the UI Kit
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd app/base/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp
```

The generated files (css, min.css) are saved in `static/assets/css` directory.

<br /> 

## Deployment

The project comes with a basic configuration for [Docker](https://www.docker.com/), [HEROKU](https://www.heroku.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Heroku](https://www.heroku.com/)
---

Steps to deploy on **Heroku**

- [Create a FREE account](https://signup.heroku.com/) on Heroku platform
- [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) that match your OS: Mac, Unix or Windows
- Open a terminal window and authenticate via `heroku login` command
- Clone the sources and push the project for LIVE deployment

```bash
$ # Clone the source code:
$ git clone https://github.com/app-generator/jinja-volt-dashboard.git
$ cd jinja-volt-dashboard
$
$ # Check Heroku CLI is installed
$ heroku -v
heroku/7.25.0 win32-x64 node-v12.13.0 # <-- All good
$
$ # Check Heroku CLI is installed
$ heroku login
$ # this commaond will open a browser window - click the login button (in browser)
$
$ # Create the Heroku project
$ heroku create
$
$ # Trigger the LIVE deploy
$ git push heroku master
$
$ # Open the LIVE app in browser
$ heroku open
```

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website

<br />

---
[Flask DataTables Sample](https://blog.appseed.us/flask-data-tables-open-source-sample/) - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
