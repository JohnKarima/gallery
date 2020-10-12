# Project Name 
Gallery App

# Project Description 
- A personal gallery application that displays your photos for others to see.

# Link to Live Project
- 

# Author 
- [John Karima](https://github.com/JohnKarima)

# Setup Instructions 

## Cloning

- Clone the repository 
```
$ git clone https://github.com/JohnKarima/gallery
```
- Move into directory and install requirements
```
$ cd gallery
$ pip install -r requirements.txt 
```
- Install and activate a Virtual Environment
```
$ python3 -m venv virtual 
$ source virtual/bin/activate  
```

- Set-up a Database
```
Set your database User and Password 
```
- Make Migrations
```
$ python manage.py makemigrations <DB Name> 
```
- Migrate
```
$ python manage.py migrate 
```
- Run the application
```
python manage.py runserver 
```
- Run the test for the application:
```
$ python3 manage.py test
```

# Technologies Used
- Python
- Django
- Bootstrap
- pillow

# Contact Information
karimajohn24@gmail.com

# License Copyright 
- 2020, John Karima.

https://opensource.org/licenses/MIT