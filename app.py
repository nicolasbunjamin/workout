""" Web app for /r/bodyweightfitness's Recomended Routine™. """

from flask import Flask, flash, redirect, render_template, request
# TODO: import time

app = Flask(__name__)


class Exercise:
    """ List of exercises and function to generate workout circuit. """

    dynamic_stretches = ("Yuri's Shoulder Band Warmup",
                         "Squat Sky Reaches",
                         "GMB Wrist Prep",
                         "Deadbugs")  # 30 seconds

    advanced_warmups = ("Arch Hangs",
                        "Parallel Bar Support Hold",  # 30 seconds
                        "Squats",
                        "Romanian Deadlifts")

    squat = ("Assisted Squats",
             "Squats",
             "Bulgarian Split Squats",
             "Beginner Shrimp Squats",
             "Shrimp Squats")
    pull = ("Scapular Pulls",
            "Arch Hangs",
            "Negative Pull-ups",
            "Pull-ups",
            "Weighted Pull-ups")
    hinge = ("Romanian Deadlifts",
             "Single Legged Deadlifts",
             "Banded Nordic Curl Negatives",
             "Banded Nordic Curls",
             "Nordic Curls")
    dip = ("Parallel Bar Support Hold",  # 60 seconds
           "Negative Dips",
           "Parallel Bar Dips",
           "Parallel Bar Dips",
           "Weighted Dips")
    push = ("Vertical Push-ups",
            "Incline Push-ups",
            "Full Push-ups",
            "Diamond Push-ups",
            "Pseudo Planche Push-ups")
    row = ("Vertical Rows",
           "Incline Rows",
           "Horizontal Rows",
           "Wide Rows",
           "Weighted Inverted Rows")
    progressions = (squat, pull, hinge, dip, push, row)

    core = ("Ring Ab Rollouts",
            "Banded Pallof Presses",
            "Reverse Hyperextension")

    def __init__(self, level):
        """ Set difficulty level on a scale of 0 to 4 """
        self.level = level

        """ Generate today's main circuit """
        self.circuit = []
        for item in self.progressions:
            self.circuit.append(item[level])


@ app.route("/", methods=['GET', 'POST'])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':

        # Select exercise difficulty level
        level = request.form.get("level")
        exercise = Exercise(level)

        if not level:
            flash("Please select level of training.")
            return render_template("/setup")

        # TODO: Start workout with timer
        """ Exercise will consist of:
        – dynamic stretches
        – advanced warm-ups if level > 1
        – main strength training circuit split to three pairs,
          three sets each (alternating, with 90 seconds rest)
            • squat and pull
            • hinge and dip
            • push and row
        – core training circuit, three sets each

        Unless otherwise stated, do eight reps for each set.

        Click on anything/tap screen to proceed to next exercise.
        """

        return redirect("workout.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/setup")


@ app.route("/about")
def setup():
    return render_template("about.html")


# TODO: Register, log-in, and workout history feature
