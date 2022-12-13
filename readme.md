# Team 13 Message Board Website
- Team Lead: Gift Olatunji (@giftolatunji)
- Erich Carrasco (@eacarrasco)
- John Clear (@LofiTurtle)

## Introduction

This is an app where you can send messages and have everyone else on the website see them. Initially, users see the splash page. Then they can create an account or login to an existing one. After that, they will see all the messages that have been sent so far, and be able to send new ones. They can also search for messages and other users.

## Installation

Install by cloning this git repository. You will need Python 3 installed, and you will need to install the following python packages via pip:
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-WTF
- Werkzeug
- requests

## Usage

Run this website by navigating to the `flask-project/` directory, and run the server by issuing the command `python3 run.py`. A URL will be printed to the terminal. Navigate to this URL in your web browser to visit the website. You will then have access to all the functionality described in the next section.

Additionally, if you'd like to initialize the database with specific data, you can use the `create-db.py` file. Create and commit any database objects you'd like, and run the file to recreate the database. 

## Functional Requirements

We chose to implement the following functional requirements. Each requirement is listed under the group member who was responsible for it.

- **Gift:**
	- Login
	- Logout
	- Create new account
	- delete account
- **Erich:**
	- User home page (users can see all messages)
	- Send messages
- **John:**
	- Search for user
	- Search messages
	- Splash page
	- Connect with any external API

## Technologies Used

This website was made in Python using the Flask web framework and its related modules. It also uses the "requests" python package to make HTTP requests to Unsplash.com's API. It uses Unsplash's API to retrieve the randomly selected images used as the background for the splash page. 