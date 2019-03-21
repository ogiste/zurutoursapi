# ZuruToursAPI
[![Build Status](https://travis-ci.org/ogiste/zurutoursapi.svg?branch=backend-api)](https://travis-ci.org/ogiste/zurutoursapi)


API for a Web-based tours and travel website.

## Running API  ##
Clone this repo to your machine

 ``` git clone https://github.com/ogiste/zurutoursapi.git ```

Then change the directory to the project by

``` cd zurutoursapi/zurutoursapi ```

to make sure all the packages needed to run the project present in your machine,
we'll create a virtual environment and install the packages there


* [Install Pipenv](https://pipenv.readthedocs.io/en/latest/)

* Install the environment package

    ```pipenv install```

* Activate environment

    ```pipenv shell```

* Export the necessary environment variables (The following are sample names)
``` 
export DB_NAME=zuru_tour_dbname'
export DB_HOST='127.0.0.1'
export DB_USER='postgres username'
export DB_PASS='postgres password'
export DB_PORT='5432'
```
# run
To test our project on your terminal run

``` python manage.py runserver```

Current API endpoints :


 | METHOD        | ENDPOINT                    | DESCRIPTION |
 | ---|---| ---|
 | POST          | /api/tours/           | Used to create a tour record |
 | GET           | /api/tours/          | Used to read all tour records |
 | GET           | /api/tours/<int:id>/  | Used to view a particular tour record |
 | PATCH           | /api/tours/<int:id>/  | Used to update the tour details |
 | DELETE        | /api/tours/<int:id>/  | Allows an administrator to delete a specific tour record |
 | POST        | /api/auth/  | Allows user to login with username and password |
 | POST        | /api/users/  | Allows user to create an account |
 | GET        | /api/users/<int:id>/  | Allows user to view their profile |
 | GET        | /api/users/  | Allows admin to view all user profiles |
 | POST          | /api/bookings/           | Used to create a booking record |
 | GET           | /api/bookings/          | Used to read all bookings records as an admin |
 | GET           | /api/bookings/<int:id>/  | Used to view a particular bookings record |
 | PATCH           | /api/bookings/<int:id>/  | Used to update the bookings details as an administrator |
 | DELETE        | /api/bookings/<int:id>/  | Allows an administrator to delete a specific booking record |


View the [published collection](https://documenter.getpostman.com/view/764347/RzffJ9Y8
) for more details


 # **Built with**
```
Python 3.7
Django 2.1
Django REST Framework 3.9.2
```
# **Versioning**

[Blueprints](https://sanic.readthedocs.io/en/latest/sanic/blueprints.html) was used for versioning

# **Authors**

Alfred Opon

# **Contributing**

Though this project is open to feedback and suggestions all contributions are restricted to the main author as the project is for learning purposes