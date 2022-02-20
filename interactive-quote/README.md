# Interactive Quote Project

## Creating project-directory
* Commands (Windows)
	`mkdir <project-name>`

## Creating a Virtual Environment
### Creating a virtual environment using **_venv_** module
* Create project directory and cd (change directory) into it.
* Commands
	* MAC | Unix: `python3 -m venv <virtual-env-name>`
	* Windows: `python -m venv <virtual-env-name>`

### Activating the virtual environment
* Commands
	* MAC | Unix: `source venv/bin/activate`
	* Windows: `<virtual-env-name>\Scripts\activate`

### Deactivating the Virtula Environment
* type `deactivate`

## Managing Python Packages
### Managing Python Packages with the help of **_pip_**
* _Pip_ is used to manage Python packages.
* Pip is a python package manager used to install, uninstall and upgrade packages.
* Pip is automatically installed with Python 3x but gets updated often.
* Commands to upgrade Pip
	* Windows: `python -m pip install --upgrade pip`
	* MAC: `python3 -m pip install --upgrade pip`
* Command to install package using using pip: `pip install <package-name>`
* Command to uninstall package using pip: `pip uninstall package`
* Command to upgrade package: `pip install --upgrade package`
* Command to list all packages: `pip list`
* Command to display information about a package: `pip show <package-name>`

### Python Modules and Packages
* A Python **_module_** is a single Python file with a **_.py_** file extension.
* A Python **_package_** is a collection of modules inside a directory that also contains a file named `__init__.py`

## Installing Flask
* Command to install flask: `pip install flask`

## Setting up Flask Environment Variables
* Install Package to invoke variables
	* `pip install python-dotenv`
* Create a file with `.flaskenv`
* Set the variables inside `.flaskenv`
	* `FLASK_ENV=development`
	* `FLASK_APP=<python-module-name>`
* Other required key variables can also be added as per the requirement.

## Creating a minimal flask app
* Create a python module (file) and save it with `.py` extension.
* Import the class `Flask` and instantiate it (The first letter of a class name is always Uppercase)
* Create a default route
* Run the app

## What are endpoints?
* **Endpoints** refers to the name of the view function.
* A _view_ function is the function that responds to request from your application.

## Rendering Templates
* Templates lets you separate Front End Coding from Python Code.
* Flask looks for templates in a folder named `templates` in your project folder.
* The methods named `render_template` is used to render templates.
* Flask has a built-in template engine named `jinja {{  }}` which enales you to pass variables into HTML templates.

## Conditional Statements
* Conditional statments are statements that will execute a block of code based on if a condition is true or false.
* Examples of conditional statements are **if** and **else** statements.
* Example
	```
	a = 10
	b = 5

	if a > b:
		print("a is greater than b")
	else:
		print("b is less than a")
	```
## Using a for loop
* A `for` loop is used for iterating over a sequence like a list.
* `for` loop executes a set of statements, once for each item in a list.
* Example
	```
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
		print(x)
	```
## Favourite Quotes Templates
* Create `static` folder
* Add Bootstrap CSS
* Modify `index.html`
* Add inline CSS
* Create `quotes.html` template
* Add form to `quotes.html` template 

## Container class
* `container` class is used to create boxed content.
* `theme-showcase`: This is a template showcasing the optional theme stylesheet included in Bootstrap.
* The `role` attribute describes the role of an element to programs that can make use of it, such as screen readers or magnifiers.
* `main`: identifies the main content of a document.

**Note:** The `form-group` class is the easiest way to add some structure to forms. `Form controls` class automatically receive some global styling with Bootstrap.

## Database Integration
### Psycopg2 and SQLAlchemy
* **psycopg2** is a database driver or database adapter that facilitates the communication between Python programs and databases
* **SQLAlchemy** is a library used as an Object Relation Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.
* Installation commands:
	* psycopg2: `pip install psycopg2`
	* SQLAlchemy: `pip install Flask-SQLAlchemy`

## Database Configuration
* `import SQLAlchmey from flask_sqlalchemy`
* app configuration settings
	* `app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:password@localhost/<db-name>'`

## Creating a Table
* Create an instance of SQLAlchemy
* `db = SQLAlchemy(app)`
```
class Favquotes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))
```
## To create the table 
* Enter python shell and add following commands
	```
	from quote import db
	db.create_all()
	```
## WSGI (Web Server Gateway Interface)
* It is a protocol for web servers to forward requests to web applications or frameworks written in the Python.
### What is Gunicorn?
* Gunicorn is a Python WSGI HTTP Server that facilitates communication between your web application and the web server.
* Install command: `pip install gunicorn`

## Deploying the App to the cloud
### Deploying Steps
* Create a Procfile for the project
	* A **Procfile** specifies the commands to be executed when the web application starts.
* Create a **requirements.txt** file
* Create a **.gitignore** file
	* **.gitignore** is a text file that tell git what to ignore in the app project when pushing code from the project directory to remote repository on GitHub.
* Create **app** on Heroku.


## Screenshots of the Application
### Opening Page
![Opening Page](ss-images/opening-page.PNG)
### Adding Quote Page
![SAdding Quote Page](ss-images/add-quote-page.PNG)

