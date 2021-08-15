# THE RECOMMENDED ROUTINE
#### Video Demo: https://youtu.be/d6-FN4qXMyE

The Recommended Routine is a web application based off of
/r/bodyweightfitness's workout program. ou can access the full guide here
(https://www.reddit.com/r/bodyweightfitness/wiki/kb/recommended_routine).
This web application is submitted as my final project for HarvardX's CS50
(https://cs50.harvard.edu/x/2021/project/).     
The Recommended Routine can be accessed via a desktop browser,
but is also mobile-friendly.

The back-end is written in Python, while the front-end is in JavaScript.

## How to Use

Usage is very straightforward. Simply select your desired training level  
between 1 and 5, where level 1 is the most beginner-friendly
and level 5 is the most difficult and advanced.
Level 3, 4, and 5 also features a longer warm-up session.

The web application will then give you a series of instructions you are
to complete one at a time. The instructions are separated into three parts:
The warm-up, the main circuit training program, and some final core exercises.
The main circuit is further divided into three pairs:
squat/pull exercises, hinge/dip exercises, and push/row exercises.

Each exercises will be done in three sets with rest periods in between.
Most sets are rep-based, but there are time-based exercises as well.
During those rest periods and time-based exercises,
the web app will display a timer.

When your allotted time for a particular instruction is up,
the web app will automatically move on to the next part of the routine.

## Features

This web page includes:
* Five different levels of training level for each muscle groups
* Additional warm-up exercises for more advanced user
* An automatic timer for rest periods and time-based exercises

## Structure

The web application includes one back-end program app.py,
four HTML pages, one CSS, and one JavaScript.

App.py begins with the configuration of the web application.
This task is done with the help of packages flask, flask_session,
and temp. Later on, it will also utilize numpy.
These packages and their respective versions are listed in requirements.txt.

In app.py, the user will initialize a Python object in the class Routine.
The class Routine is composed of a couple of tuples,
grouping exercises, grouping exercise groups into workout segments,
and notes some exeptions.

It will then generate an exercise program according to the selected training level.
The user can choose this training level by heading to the default ("/") route
via the GET method (redirection/hyperlink). The corresponding webpage is setup.html.

After submitting the POST request, the user will head to the workout.html,
which lists all of the instructions for the day's workout session.
The instruction is displayed one at a time, thanks to the JavaScript program
available at the front-end. The script does this through the event listener
traversing through the list at each "Next" or "Previous" button press.

If the JavaScript program detects a time-based exercise,
it will also display an automatic timer, aided by the setInterval functionality.

Besides the default ("/") route, the user can also access the about page
and read more information on the workout routine or head to /r/bodyweightfitness.
Every HTML page above extends the layout.html page and uses Boostrap,
as well as the custom styles.css file for styling.
