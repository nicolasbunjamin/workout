""" Web app for /r/bodyweightfitness's Recomended Routine™. """

from flask import Flask, flash, redirect, render_template, request
from flask_session import Session
from numpy import array_split
# TODO: import time

app = Flask(__name__)


# TODO Add separate config.py and .env
# Read https://flask.palletsprojects.com/en/2.0.x/config/
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "secret"
# TODO Implement sessions
Session(app)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


class Routine:
    """ List of exercises and function to generate workout circuit. """

    dynamic_stretches = ("Yuri's Shoulder Band Warmup",
                         "Squat Sky Reaches",
                         "GMB Wrist Prep",
                         "Deadbugs")
    advanced_warmups = ("Arch Hangs",
                        "Parallel Bar Support Hold",
                        "Squats",
                        "Romanian Deadlifts")
    warmup_exceptions = ("Deadbugs", "Parallel Bar Support Hold")
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
    dip = ("Parallel Bar Support Hold",
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
    circuit_exceptions = ("Parallel Bar Support Hold")
    core = ("Ring Ab Rollouts",
            "Banded Pallof Presses",
            "Reverse Hyperextension")

    def __init__(self, level):
        """ Set difficulty level on a scale of 0 to 4 and
        generate today's main circuit components accordingly.
        """

        self.level = level
        self.circuit = []
        for item in self.progressions:
            self.circuit.append(item[level])

    def generate_instructions(self):
        """ Generate a list of instructions to be displayed in webpage. """
        self.instructions = []

        # FIXME
        # Find a more elegant solution to implement rep count exceptions.

        # Dynamic stretches
        self.instructions.append("Let's begin with some warm-ups!")
        for item in self.dynamic_stretches:
            if item in self.warmup_exceptions:
                self.instructions.append("30 seconds of "+item)
            else:
                self.instructions.append("8 reps of "+item)

        # Advanced warm-ups
        if self.level > 1:
            for item in self.advanced_warmups:
                if item in self.warmup_exceptions:
                    self.instructions.append("30 seconds of "+item)
                else:
                    self.instructions.append("8 reps of "+item)

        # Main strength training circuit
        self.instructions.append("Here we go! Do your best!")
        pairs = array_split(self.circuit, 3)
        for i in range(len(pairs)):
            self.instructions.append("Pair "+str(i+1))
            for j in range(3):
                self.instructions.append("Set "+str(j+1))
                for item in pairs[i]:
                    if item in self.circuit_exceptions:
                        self.instructions.append("60 seconds of "+item)
                    else:
                        self.instructions.append("8 reps of "+item)
                    self.instructions.append("Rest for 90 seconds")

        # Core training circuit
        self.instructions.append("Last part: core!")
        for i in range(3):
            for item in self.core:
                self.instructions.append("8 reps of "+item)
                self.instructions.append("Rest for 60 seconds")

        return self.instructions


@app.after_request
def after_request(response):

    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@ app.route("/", methods=['GET', 'POST'])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':

        # Select exercise difficulty level
        level = request.form.get("level")

        if not level or not level.isdigit():
            flash("Please select level of training.")
            return redirect("/")

        # Generate today's routine
        routine = Routine(int(level))
        instructions = routine.generate_instructions()
        instructions[-1] = "You're done!"

        return render_template("workout.html", instructions=instructions)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("setup.html")


@ app.route("/about")
def about():
    return render_template("about.html")


# TODO: Register, log-in, and workout history feature
# TODO: Illustrations/guides for exercises
