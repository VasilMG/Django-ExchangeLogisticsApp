# ExchangeLogisticsApp
Basic app for a logistics company with built in freight echange built with:
 - python
 - django - server side rendering
 - bootstrap - carousel templates
 
 In this app we have three common templates where the information for the logistics company is displayed.
 I have put some exemplary text in the templates in order for the app to start without creating a superuser.
 There are three models for the basic data regarding the company ( in common/models.py) which can be used, but only after a superuser is creted.
 Using the admin page we can add the desired information and then render it to the teplates ( see the lines marked as comments on the common templates)
 
 The second feature of the app is a freight exchange where registered users can publish their loads or free trucks.
 A user can sign up with username and password. After that a blank profile is created and the user should fill the neccessary data for his profile.
 After that he can publish freight or truck offers on the market.
 Every offer includes information about the company that had posted it and also a link to this company's profile, where the user can see all actual offers of this particular company.
 
 # Run the project
 
 1. Clone the repository

 2. Open it with your preferred IDE and create a virtual environment
 - Here is a useful link - https://djangowaves.com/tips-tricks/fix-import-error-no-module-named-django-core-management/
 
 3. Install all dependencies
  - pip install -r requirements.txt
  
 4. Make the migrations ( I have made a custom user so if you just run it without migrations you will get an error. )
  - python manage.py makemigrations
  - python manage.py migrate
 
 5. Run the project
 - python manage.py runserver

 6. Finally open th project in your browser - http://127.0.0.1:8000/ or http://localhost:8000/
 
 I have used the default SQLite database for this basic project.
 
  - Below you can find some photos:
 
![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20233520.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20233434.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20231650.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20232347.png)

