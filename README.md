# ExchangeLogisticsApp
This is an app for a logistics company with built in freight exchange.

Stack used:
 - python
 - django - server side rendering
 - django rest framework
 - bootstrap - carousel templates
 
 This project has both - server side rendering and APIs.
 All endpoints are visible in the swagger url -- - http://127.0.0.1:8000/swagger-ui/
 
 
 
 In this app we have three common templates where the information for the logistics company is displayed.
 I have put some exemplary text in the templates in order for the app to start without creating a superuser.
 There are three models for the basic data regarding the company ( in common/models.py) which can be used, but only after a superuser is creted.
 Using the admin page we can add the desired information and then render it to the teplates ( see the lines marked as comments on the common templates)
 
 The second feature of the app is a freight exchange where registered users can publish their loads or free trucks.
 A user can sign up with username and password. After that a blank profile is created and the user should fill the neccessary data for his profile.
 After that he can publish freight or truck offers on the market. The user can search for siutable offers on the market and see the offer's details by clicking on it.
 Every offer includes information about the company that had posted it and also a link to this company's profile, where the user can see all actual offers of this particular company.
 
 # Run the project
 Since the project is data dependent I have also made an image working with some sample data, so you can just create a user and a profile and browse through the app.
 You can also test the api endpoints.
 
 I. Using Docker image:
 
 You can pull the image from Docker Hub https://hub.docker.com/r/vasilmg/logistics_app
 
 1. Execute the pull command - docker pull vasilmg/logistics_app
 
 2. Find the image id:
 - docker image ls
 
 3. Run the image:
 - docker run --name <desired_name>  -dp 8000:8000 <image_id> python manage.py runserver 0.0.0.0:8000
 
 4. Open your browser and type - http://127.0.0.1:8000/ or http://localhost:8000/
 
 II. Clone the repository from GitHub
 
 1. Clone the repository

 2. Open it with your preferred IDE and create a virtual environment
 - python3 -m venv ./env   - to create a virtual environment
 - source ./env/bin/activate - to activate it
 
 3. Install all dependencies
  - pip install -r requirements.txt
  
 4. Make the migrations
  - python manage.py makemigrations
  - python manage.py migrate
 
 5. Run the project
 - python manage.py runserver

 6. Finally open the project in your browser - http://127.0.0.1:8000/ or http://localhost:8000/
 
 I have used the default SQLite database for this basic project.
 
  - Below you can find some photos:
 
![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20233520.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20233434.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20231650.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-05%20232347.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-11%20232327.png)

