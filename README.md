# Hiver - Scrapping App

Used Technologies:

1. Language: python3.6
2. Framework: Django==2.1.5
3. Packages: Requests, BeautifulSoup


# Steps to Run This Project.

1. `git clone https://github.com/monetree/hiver.git`
2. `cd hiver`
3. `virtualenv -p python3.6 env`
4. `cd env && source bin/activate && cd ..`
5. `pip install -r requirements.txt`
6. `python manage.py migrate runserver`
7. `python manage.py runserver`


###### Note: This command i have shared for linux system. You can change the command as per appropriate OS.



### After all these steps:
  open browser:
  1. visit `http://127.0.0.1:8000` to get top 5 occourances words
  2. visit `http://127.0.0.1:8000/api/` to get all data in json structure.
