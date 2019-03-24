# Task Manager App

In the final week of my coding bootcamp I built this web app, which allows users to add tasks to their to do list and then update and remove these tasks as they are completed. 


## Development

I created a database with SQLite, and wrote SQL queries to add, modify and delete tasks in the database. I then used Python (including the requests library) and Flask to build a RESTful API to handle requests for JSON data from the database. 

I used Jinja to connect the back end to a front end that I created with HTML, CSS and Bootstrap.


## Design
When the app is running, the home page displays tasks in the order of their due date, and high priority tasks are shown in red. Users can click a link to add new tasks, or can click on buttons on each individual task to edit or delete those tasks.


## Technologies
* Python
* Flask
* Jinja
* SQL
* SQLite
* HTML
* CSS
* Bootstrap


## Installation

Clone the repository.

```$ git clone https://github.com/hpellis/task_manager_app```

Navigate to the directory. 

```$ cd task_manager_app```

Install Flask.

```$ pip install Flask```

Run the app file.

```$ python task_app.py```

Navigate to the local host address in your browser to see the app running. 

![image of application home page](/final_images/final_version.png?raw=true "Task Manager")
