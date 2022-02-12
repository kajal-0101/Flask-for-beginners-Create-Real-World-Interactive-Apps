### What is Flask?
* Flask is a lightweight framework for developing web applications using Python.
* A framework is a scaffold that you can build applications around.
* Flask is designed to enable you to build and scale applications quickly.
* Extensions can be extend the functionality of flask.

### Pros and Cons of using Flask

**Pros**
* Easy to get started
* Customizable
* WSGI (Web Server Gateway Interface) compatible

**Cons**
* Limited functionality from the box
* No database setup

### Technologies Used in the Hands on Projects
* Python
* Pip
* Virtual environment
* Good Text Editor (e.g. Atom)
* Command Line Interface (Command Prompt | Terminal)
* HTML | CSS | JavaScript | Bootstrap
* JSON
* SQLAlchemy
* PostgreSQL Database
* Git and GitHub

### What is a Python Module?
* A python module is a file with a .py file extension.
* It can contain python definitions and statements.


### What is a Python Package?
* A python package is a directory with Python files.
* It contains a file name `__init__.py`
* The `__init__.py` file makes Python treat directories as packages.
* A package can contain several python modules.

### To check if python is installed
* `py` - interactive python shell interface
* `python --version` - shows the version of python if it is installed

### What is Pip?
* Pip is a package management system used to install and manage software packages written in python.

**Updating Pip**
* If you have Python version 2.4 or later, PIP is included by default
* Pip gets updated quite a bit so it is best to keep up the latest version.
To update
* python -m pip install --upgrade pip (windows)
* Internet connection mandatory

### What is a Virtual Environment?
* A virtual environment is an isolated Python environment
* Virtual environments allows you to install Python packages in an isolated self-contained environment.
* A virtual environment is a copy of the Python interpreter into which you can install packages privately, without affecting the global Python interpreter installed in your system.
* An interpreter is a program that reads and executes your code.

### Usefulness of Virtual Environment
* Prevent package clutter
* Prevent version conflicts in the system's Python interpreter.
* Creating a virtual environment for each project ensures that applications have access only to the packages that they use, while the global interpreter remains neat and clean and serves only as a source from which more virtual environmets can be created.

**Creating a virtual environment**
* There are different packages that can be used to create a virtual environment. Example is the virtualenv package. This has to be installed before it can be used.
* Python has a built-in module called venv that can be used to create and manage virtual environments. You do not have to install it to use.

**Create a virtual environment using _venv_ module**
* Create a project directory and cd into it.
* Mac | Unix: `python3 -m venv <env-name>`
* Windows: `python -m venv <env-name>`

**Activating a virtual environment**

* (Mac | Linux): `source venv/bin/activate`
* (Windows): `venv\Scripts\activate`

**To deactivate virtual environment**
* type `deactivate`

**What is Virtualenv Tool?**
* Virtualenv is a tool used to create isolated Python environments
* It allows you to install python packages specific to a project.

**Installing Virtualenv Tool**
* Mac | Linux | Windows: `pip install virtualenv`

To check the list of pip packages: pip list

### Function | Class | Object
* A function is a block of code that performs a specific tasks
* Functions may contain zero or some parameters.
* Functions are created with def keyword followed by the name of the function.
* functions have to be called to get them to perform a specified task.
* Parameter is what is declared in the function, while an argument is what is passed through when calling the function.
* A class is a code template (blueprint) for creating objects. To create a class, use the keyword class.
* An object is a collection of data (variables) and methods (functions) that act on those data objects.
* A Method is like a function except it is associated with objects and classes. Methods in objects are functions that belong to the object. Methods are implicitly used for an object for which it is called. Mathods are accessible to data that is contained within the class.
* A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in a class.
* The `__init__()` is built-in function in Python which is called automatically every time the class is being called to create a new object. It is used to assign values to object properties, or other operations that are necessary to do when object is being created.
* The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
* Initiating a class means you are creating an object from that class.
* The first letter for the name of a class is always in uppercase.
* A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in a class.


## Creating a minimal flask application
Requirements
* Plain Text Editor
* Pre-installed software
	* Python
	* Flask
* Virtual Environment and Project Directory


### Development Server
* Flask framework includes a development server for running and testing your flask application.
* Environment variables have to be set for the server so it knows what module or package contains your flask application. Also you have to set it to run in development mode so you can see any errors and also your code changes are applied with restarting the server.
* Environment variables can be set inside your command line interface session or inside a `.flaskenv` file. Environment variables set inside command line sessions are lost when you close the seesion of the command line interface. To activate the environment variable stored inside `.flaskenv` file you have to install the package called `python-dotenv`.
* **MAC Terminal**
	```
	export FLASK_APP=<file-name>
	export FLASK_ENV=development
	```
* **Windows Terminal**
	```
	set FLASK_APP=<file-name>
	set FLASK_ENV=development
	```
* **start server**: `flask run`
* **stop server**: `press CTRL + C`

### What is a URL?
* URL (Uniform Resource Locator)
* Also known as a web address
* Example: 
	```
	https://www.google.com
	https://www.you-application.com [root URL('/')]
	https ://www.you-application.com/profile(endpoint)
	```

## Basic components of a Flask Application

* `from flask import Flask` => importing class 'Flask' from the module flask
* All flask applications must create an application instance.
* `app = Flask(__name__)`
 	The required argument `__name__` that the instance of the flask class needs is the name of the module or package that contains the application. 
* `@app.route('/')`
	Every Flask application requires at least one route and a view function.
* The route decorator tells Flask what URL (web address) should trigger a function. 
* Route decorator takes the url as an argument and maps or binds
it to a view function when it receives a request to the application.
* The view function contains the response to the request your application receives. 
```
def index():
	return '<h1>Hello World!</h1>'
```
* The function is given a name which is used to generate URLs for that particular function.
* the association between a URL and the function that hanldes it is called a route.
* the view function returns a response to be displayed by the web browser following a request to the application.


### Creating Dynamic Routes.
* Dynamic routes are created by adding variable sections to your routes enclosed in angle brackets <>
* The function receives the `<variable_name>` as a keyword argument.
* The dynamic component in routes are strings(text) by default but other data types can be used like:
	* Int: Positive integers: 1 2 3, etc
	* Float: Positive floating point: 2.5, 4.1, etc
	* Path: Like strings(text) but accepts slashes: abc \

### Running Server in debug mode
* By default, the debug mode is disabled on the development server.
* Use environment variable to set the server to run in development which enables the debug mode.
* Debug mode contains two useful modules:
	* Reloader: This automatically restarts the server when changes occur in your code.
	* Debugger: This is a web tool that displays errors in your browser when something goes wrong in your application.

### What are Templates?
* Templates are files that contain static data as well as placeholders for dynamic data.
* Flask looks for templates in a templates subdirectory located inside the main application directory.
* Flask comes configured with a template engine called jinja2 that allows you to integrate dynamic data with static HTML. `{{ }}` jinja2 autoescape any data rendered in HTML templates.
* Flask has a function called `render_template()` that integrates with the jinja2 template engine to render templates. The function takes the template name as its first argument.
* Any additional arguments for the `render_template()` function are key-value pairs that represent values for variables referenced in the template.

#### Creating Templates Directory
* Flask will look for templates in the templates folder. If your application is a module, this folder is next to that module, if its's a package it's actually inside your package.

```
Case-1:
/application.py
/templates
	/hello.html
```
```
Case-2:
/application
	/__init__.py
	/templates
		/hello.html
```

### Business | Presentation Logic
* Business logic deals with the processing that takes place in the background which is invisible to the user (Application Code)
* Presentation Logic consists of the visual appearance the user sees in their web browser or other client used to view the application (Application Templates)
* Mixing business and presentation logic in the same files can make your code hard to maintain.
* MOving presentation logic into templates helps improve the mainatainability of the application.

### Jinja2 
* The `{{ name }}` constructor used in the user.html template references a variable, a special placeholder that tells the jinja2
 template engine that the value that goes in that place should be obtained from data provided at the time the template is rendered.
* Jinja2 recognizes variables of any type, even complex types such as lists, dictionaries and objects.

* Variables can be modified with filters, which are added after the varbale name with a pipe character as separator. For example, the user.html template can capitalize the first letter of the name variable:
Hello, `{{ name|capitalize }}`

* The complete list of filters can be obtained from the official Jinja2 documentation.

### Using control structures in templates
* Jinja2 template engine allows you to use control structure's in your template.
* A control structure (or flow of control) is a block of programming that analyses variables and chooses a direction in which to go based on given parameters.
* A control structure (or flow of control) is a block of programming that analyses variables and chooses a direction in which to go based on given parameters.
* A program's control flow is the order in which the program's code executes.
* A set of actions can define the flow of events of a program.
* Control structures can be used to alter the flow of a template.
* examples of control flow structures include:
	* conditional statements
	* for loops

**Conditional Statements**
* Conditional statements are statements that will execute a block of code based on if a condition is true or false.
* Examples of conditional statements are if and else statements.
	```
	a=10
	b=5

	if a > b:
		print("a is greater than b")
	else:
		print("b is less than a")
	```
**Using a for loop**
* A for loop is used for iterating over a sequence like a list.
* for loop executes a set of statements, once for each item in a list.

* Example
	```
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
		print(x)
	```
### Template Inheritance
* Template Inheritance allows you to extend component contents from a base template into other templates.
* The contents of the base templates are defined in blocks with names which have a start and end blocks.
* The base template blocks can be over-ridden by derived templates.

* The Jinja2 block and endblock directives define blocks of content that are added to the base template.
* Important to close blocks properly to avoid template errors.
* The extends directive declares that this template derives from base.html. This directive is followed by new definitions for the blocks defined in the base template, which are inserted in the proper places.
* When a block has some content in both the base and derived templates, the content from the derived template is used.
* When a block has some content in both the base and derived templates, the content from both the derived template is used. Within this block, the derived template can call super() function to reference the contents of the block in the base template.

### Installing and Initializing Bootstrap
* Using Flask Bootstrap extension to integrate Bootstrap
* pip install falsk-bootstrap
* Flask-Bootstrap initialization:
	```
	from flask_bootstrap import Bootstrap
	bootstrap = Bootstrap(app)
	```
* Bootstrap has its own base template
* Initialize bootstrap by instantiating the Bootstrap class and passing the application instance as an argument in the constructor.
* Once Falsk-Bootstrap is initialized, a base template that includes all the Bootstrap files and general structure is available to the application. The application then takes advantage of Jinja2's template inheritance to extend this base template.

#### Flask-Bootstrap's base.html template blocks
* block name -> description
* doc -> The entire HTML document
* html_attribs -> Attributes inside the `<html>` tag
* html -> The contents of the `<html>` tag
* head -> The contents of the `<head>` tag
* title -> The contents of the `<title>` tag
* metas -> The list of `<meta>` tags
* styles -> CSS definitions
* body_attribs -> Attributes inside the `<body>` tag
* navbar -> User-defined navigation bar
* content -> User-defined page content
* scripts -> JavaScript declarations at the bootom of the document
* body -> The contenst of the `<body>` tag

#### Some Bootstrap Classes
**Bootstrap Class -> Description**
* `.navbar` -> Creates a navigation bar
* `.navbar-nav` -> Container for navigation links inside the .navbar container
* `.navbar-brand` -> Added to link or header element inside navbar for logo or header
* `.navbar-collapse` -> Collapses navbar
* `.navbar-toggle` -> Styles the button that opens navbar
* `.sr-only` -> hides an element on all devices except screen readers
* `.page-reader` -> adds a horizontal line under the heading 
* `.container` -> Bootstrap containers are used to establish the width for the layout
* `navbar-header` -> It wraps both navbar brand and navbar toggle button and renders them properly.
* `navbar-inverse` -> Create an inverted navbar with a black backgrund and renders them properly
* `.icon-bar` -> Used for responsive layouts to create a button
* `.collapse` -> Collapse class indicates a collapsible elements

* Many of the blocks in the table are used by Fals-Bootstrap itself, so overriding them directly would cause problems. FAOr example, the styles and scripts are where the Bootstrap CSS and JavaScript files are declared. If the application needs to add its own content to a block that already has some content, then Jinja's super() function must be used.
Ex:
```
{{% block scripts %}}
	{{ super() }}
	<script type="text/javascript" src="my-script.js"></script>
{{ % endblock % }}
```
* The Jinja2 extemds directive implements the template inheritance by referencing bootstrap/base.html from Flask-Bootstrap. The base template from Flask-Bootstrap provides a skeleton web page that includes all the Bootstrap CSS and JavaScript files.

### Creating Custom Error Pages
* Flask allows an application to define custom error pages that can be based on templates, like regular routes.
* The two most common error codes are 404 and 500.
* The 404 is triggered when the client requests a page or route that is not known.
* The 500 is triggered when there is an unhandled exception in the application.

### What is HTTP?
* HyperTest Transfer Protocol (HTTP)
* HTTP is a protocol used for communication, usually used to communicate with internet resources or any application with a web browser client.
* HTTP works as a request-response protocol between a client and server.
* The most common HTTP methods are: GET and POST.

**GET Method**
* GET is used to request data from a specified resource.
* GET is one of the most common HTTP methods.
* GET requests can be cached.
* GET requests remain in the browser history.
* GET requests can be bookmarked.
* GET requests should never be used when dealing with sensitive data.
* GET requests have length restrictions.

**POST Method**
* POST is used to send data to server to create/update a resource.
* POST requests are never cached.
* POST requests do not remain in the browser history.
* POST requests cannot be bookmarked.
* POST requests have no restrictions on data length.

**_redirect_ and _url_for_ functions**
* The `redirect()` function is used to redirect a usre to a specified location.
* The `url_for()` function is used to build a URL to a specific function.
* The `url_for()` accepts the name of the function as its first argument and then any number of keyword arguments.

### What is JSON?
* JSON stands for JavaScript Object Notation
* JSON is a light-weight data-interchange format.
* JSON is a syntax for storing and exchanging data.
* JSON Format is text only.

**JSON Syntax Rules**
* Data is in name/value pairs
* Data is separated by commas
* Curly braces hold objects
* Square brackets hold arrays.

### Variable Rules
* Used to add variable sections to a URL
`@app.route('<string:code>')`

### Session and Cookies
* A seesion is the time interval when a client logs into a server and logs out of it.
* A session with each client is assigned a session ID.
* To use a session your app needs a secret key.
* The session object in flask is used to set and get session data.
* The data for the session is stored in the client browser as a cookie.
* It's purpose is to remember and track data pertaining to a client's usage.

### What is an API?
* API: Application Programming Interface
* Set of rules (code) and specification that software programs follow to communicate with each other.

### What are static files?
* Static files are files that do not change.
* Example include: CSS files, JavaScript files, Images, Audio files, logo etc.
* Flasks looks for static files inside a static directory of your project.
* Example: Flask Static Path
	* **CSS:**
	`<link rel="stylesheet" href="{{url_for('static', filename='bootstrap.min.css')}}">`
	* **JS:**
	`<script src="{{url_for('static', filename='bootstrap.min.js')}}"></script>`

### What is Bootstrap?
* Bootstrap is a free, open source HTML|CSS|JavaScript framework for building responsive webistes
* A framework is a scaffold that you can use to build applications around.
* Responsive webistes are designed to automatically adjust temselves to look good on all devces from small phones, tablets, desktops.
* Bootstrap is compatible with all modern web browsers.
* Bootstrap includes HTML and CSS based design templates for:
	* Typography
	* Forms
	* Buttons
	* Tables
	* Navigation
	* Modals
	* Image Carousels, etc

### Bootstrap Installation Options
* Download
* Source Files
* Bootstrap CDN (COntent Delivery Network)
* Package Managers

**Bootstrap Dependencies**
* Dependency is when a software relies on other software to perform some of it's functionalities.
* Bootstrap has two dependencies: jQuery and popper.js
* jQuery is a JavaScript library which simplifies JavaScript by using less code to do more.
* Popper.js is a positioning engine used to calculate the position of an element.

**pros of using CDN**
* It should be delivered faster to the browsers, which means it should load faster.
* If your visitor was on a different webiste that also loaded Bootstrap from that CDN, its likely their browser cached a version of it, and instead of reloading the exact same thing, it'll just used the cached version, increasing the perceived speed of your site.

**Cons of uisng CDN**
* If the CDN is down, you don't have access to Bootstrap.

### WSGI (Web Server Gateway Interface)
* It is a protocol for web servers to forward requests to web applications or frameworks written in Python

**Framework - Example:**
* Flask
* Django

**Servers - Example:**
* Gunicorn
* uWSGI

### What is Git and GitHub?
* Git is a version control system that lets you manage and keep track of your source code. It has to be installed locally.
* GitHub is a cloud-based hosting service used to manage your source code and projects.

### What is Heroku?
* Heroku is a container - based cloud platform where you can deploy and manage your apps.

### What is a Procfile?
* A Procfile specifies the commands that are executed by the app on startup.
* You can use a procfile to declare a variety of process such as your app's web server

### What is a Requirement.txt?
* This is a text file used for specifying the Python packages required to run a project.
* It is typically created at the root of your project.
Command to get all the python modules requirements is `pip freeze > requirement.txt`

### What is a Repository?
* A repository is like a folder for your project.
* It contains all of your project's files.
* It stores each files' revision history.

### Git Commands
* git init
* git add README.md
* git commit -m "First Commit"
* git remore ass origin <git-clone url>
* git push -u origin master





