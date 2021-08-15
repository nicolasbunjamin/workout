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
