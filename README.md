# CofG Calculator
#### Video Demo: https://youtu.be/0U0Owll9zGo
#### Description: It is a web app that allows users to calculate the Center of Gravity and Actual take off mass of different DHC-6 400 and 300 series of a given fleet.
#### The code is deployed in heroku using the following link: https://cofg-calculator.herokuapp.com/
#### What is the Center of gravity? The center of gravity of an object is where we can consider all of the weight of the object to be concentrated. 
#### This is a useful concept in physics and engineering. It is used to determine the stability of objects when they are tilted.
#### In aviation in particular it is used to know the effectiveness of the control surfaces (aileron, rudder...), if it is within a certain range, the aricraft will be able to fly
#### and be controlled by the pilot; otherwise the aircraft will not be controllable leading to obvious catastrophic results. This is why all pilots must submit 
#### a documents stating the mass distribution of each flight and the calculation of the center of gravity to make sure it is within limits.
#### This project is using a flask framework of python. There is a main application.py where you can find all the logic of the web app. In the same
#### directory you can find a folder called static where all media an css is found and another folder called templates where you can find all html.
#### There is also a procfile and a requirements.txt in order to be able to deploy the code in heroku

## Technologies used:

- python
- jinja
- html
- css
- javascript
- bootstrap 5

## How the webpage works?

The idea is simple. The user can select one of the following aircrafts:

- G-HIAL
- G-BVVK
- G-GSTS

There are two inpot fields to put aircraft fuel the first one is for the forward tank and the second one is for the aft tank. There is a maximum capacity in each tank of 1250 Lbs and the app won't let you submit any fuel greater than that.
After this there is a Nose compartent to load any sort of cargo. The weight limit on that is 136 Kg and again it is not possible to submit heavier loads. The reason we are using Kilos here is because loads in load sheet will be in Kgs whist fuel indication in the aircraft is in Lbs therefore we avoig having to convert the loads with the possible mistakes this would imply.
Following this there is a display of buttons labeled as per the seat they represent and clicking them will change it's value circularly from male to female, female to child, child to empty (default value) and back to male again.
Finally there is another input for the aft hold with the same behavior as the nose one, exept this one allows heavier loads (227 Kg).
To see the result you only neet to press the calculate button located at the end or at the top of the form and a message will appear at the top of the site with the result and in green color if the result is within limits or red if it is not.

### Routing

There is one route for the main page showing pictures of each aircraft in the fleet and then a route for every aircraft and a separate route to display index information.

### Database

There is no database needed but I would consider using SQLAlchemy for bigger fleets

## Possible improvements

As all applications this one can also be improved. Possible improvements:

- As stated before use a database an allow an admin to update and add/delete aircrafts
- Create Users to be able to sign in and store submited data by each user
- To be able to do that Sessions would need to be implemented as well
- Notificaitons to email CG submissions.
- Be able to go back to submited data to be able to modify and update last minute changes.

## How use the application

1. Check that you have pip or a similar python package installer
2. Clone the code: `git clone https://github.com/a-dal/cs50project.git`
3. Run command prompt in the folder and run `pip install requirements.txt` to install all dependencies
4. Change the name of application.py to app.py this willmake easier running falsk
5. Run command `flask run`
6. In your browser go to `localhost:3000`
7. You are ready to go!