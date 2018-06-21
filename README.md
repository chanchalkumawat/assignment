Features
Python 3.5
Latest Django 2.0.6
Support for Dajngo Rest Framework
SQLite for Database
Prometheus for monitoring the api’s

Quickstart
Install Python 3.5
Install virtualenv using : pip install virtualenv
Create a virtualenvironment using below command:
virtualenv nameofenvironment
Activate the environment : source nameofenvironment/bin/activate
Download the zipped folder from github link provided for project and extract it.
Navigate to Assignment folder and run below mentioned commands:
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Configured URLs:
localhost:8000/admin
Username: root
password: admin123
Description: URL for django admin panel. Enter localhost:8000/admin on 	browser and click on demoapp and users.In the search box you can 	filter the users by email,city,firstname and date.

localhost:8000/users
Description: URL to search and create new users. 
Usage: localhost:8000/users will give all users
       locahost:8000/users/?userid=1 will filter user according to userid.
	   locahost:8000/users/?date=2018-06-20 will filter users according to date.
  	   localhost::8000/users/?city=pune will filter users according to city.

To create new user :

Hit localhost:8000/users/ from tool postman or restclient
Select post method and in body enter the data.
Sample json data will be :

{
	"first_name": "sampleuser",
	"last_name": "test",
	"email": "c7@gmail.com",
	"city": "banglore"
}

Note: Refer to screenshot folder for screenshot of api's output



	





