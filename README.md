# Django-Test-Automation

This is a test framework for Resume Builder training application located at [Pythonanywhere hosting](http://yeroshchenko.pythonanywhere.com/).
Source code of Resume Builder located [here](https://github.com/AllaYeroshchenko/django).
It was written in Python, based on the pytest framework using the Selenium library.  


* [The goal](#The-goal)
* [Structure](#Structure)
* [Tests](#Tests)


# The goal
My goal is to find a job as a Quality Assurance Automation Engineer. The main purpose of this project is to demonstrate my ability to use the knowledge that I received from different courses and also my ability to work independently. I couldn't demonstrate my ability to work in a team, because I didn't have a team; I worked alone. But I will be happy to help somebody who is also a job seeker or anyone else who has any questions about this project. Feel free to write to me with any questions about this project, and you can use my code in your own projects.  
The application Resume Builder, which is tested by this framework, was also developed by me. I built it using Python, Django, JavaScript, and of course HTML  and CSS. For data storage I use mySQL database. But it could be any relational database; Django is very flexible.    
    

# Structure
```
DjangoTesting
├── README.md
├── requirements.txt
├── target.json
├── conftest.py
├── data
│   ├── resume_random_gen.json
│   ├── resumes.json
│   └── resumes_for_edit.json
├── generator
│   └── resumes.py
├── fixture
│   ├── application.py
│   ├── db.py
│   ├── resume.py
│   └── session.py 
├── models
│   ├── resume.py
│   ├── education.py
│   └── experience.py
└── test
    ├── test_add_resume.py
    ├── test_delete_resume.py
    └── test_edit_resume.py
```    

**requirements.txt**  
This is the list of packages that are used in the project.  
To install the depended packages in requirements.txt use:   
```
pip install -r requirements.txt
```
**target.json**  
This is the data that we need to run the project, the name of the domain, user log in and password, and all the data that we need to connect to the database from the local machine. In the case of Pythonanywhere I need to make an SSH tunnel to retrieve data from the database.  

**conftest.py**  
This is a specific file for pytest is used for defining and finalizing fixtures. There are two fixtures: app and db. The app fixture creates an instance of the Application class. It ensures all prerequisites for the test: run browser, go to the home page and log in. Another db fixture creates an instance for a database connection. After instantiating these two fixtures we are ready for testing. 
We have the possibility to run the project with parameters "--browser" and/or "--target". "--browser" can be "firefox", "chrome" or "ie". In "--target" we can connect files with different data, for example, if we need tests with different users. We can run tests like this:  
```
pytest --browser chrome --target another_target.json -s -vv
pytest --browser firefox -s -vv
pytest --browser ie -s -vv
```

**data**
This folder contains data for testing in JSON format. 

**generator**  
	- **resume.py**  
	This file contains a script for generating random resumes for tests. It's not for constant use, but sometimes it can be useful.  
	Use it like this:  
	```
	python generator\resume.py
	```

**fixture**   
	- **application.py**    
	This file contains a fixture Application that has all the necessary things to start a testing framework. It starts the browser, opens the start page and logs in, and it gets everything ready to start tests.     
	- **resume.py**  
	This file contains all functions which work with resumes.   
	- **session.py**  
	This file contains functions log in and logout.   
	- **db.py**  
	This file contains a fixture dbFixture that works with a database. In this case, we work with a MySQL database.    

**models**   
	- **resume.py**  
	This file contains a Resume object.  
	- **education.py**  
	This file contains an Education object.  
	- **experience.py**  
	This file contains an Experience object.  

**test**   
	- **test_add_resume.py**  
	This file contains a test that checks the functionality of adding a new resume.  
	- **test_delete_resume.py**  
	This file contains a test that checks the functionality of deleting a random resume.  
	- **test_edit_resume.py**  
	This file contains a test that checks the functionality of editing a random resume.  


# Tests

Framework checks the main functionality, just 3 test cases.

## Test Add a New Resume
This test is parametrized. It downloads the data from a JSON file and then runs a test for each resume from the file.
1. Get the last resume id from the database.
2. Add a new resume.
3. Check that the page has a message "Resume was added".
4. Get a new last resume id from the database.
5. Check that the last resume id has changed.
6. Get a new resume record from the database using the new last resume id.
7. Check that the new resume record in the database is equal to the added data.
8. Get new education records from the database using the new last resume id.
9. Check that new education records in the database are equal to the added data.
10. Get new experience records from the database using the new last resume id.
11. Check that the new experience records in the database are equal to the added data.

## Test Delete a Resume
1. Check the quantity of resumes for the current user in the database.
2. If the quantity is zero add a new resume.
3. Get the quantity of resumes before deleting.
4. Get a list of resumes from the web page.
5. Choose a random resume from the list.
6. Delete the random resume.
7. Get the quantity of resumes after deleting.
8. Check that the quantity of resume has decreased by 1.
9. Check that there are no records about the deleted resume in the database.
10. Check that there are no records about education connected with the deleted resume in the database.
11. Check that there are no records about experience connected with the deleted resume in the database.

## Test Edit a Resume
This test is parametrized. It downloads the data from a JSON file and then runs a test for each resume from the file. But there is just one resume in the example.
1. Check the quantity of resumes for the current user in the database.
2. If the quantity is zero add a new resume.
3. Get the quantity of resumes before deleting.
4. Get a list of resumes from the web page.
5. Choose a random resume from the list.
6. Edit the random resume with new data.
7. Check that the page has a message "Resume was edited".
8. Get the quantity of resumes for the current user in the database after deleting.
9. Check that the quantity of resumes hasn’t changed. 
10. Get an edited resume record from the database using the random resume id.
11. Check that the edited resume record in the database is equal to the data for editing.
12. Get edited education records from the database using the random resume id.
13. Check that the edited education records in the database are equal to the data for editing.
14. Get edited experience records from the database using the random resume id.
15. Check that the edited experience records in the database are equal to the data for editing.


