""" Web app for /r/bodyweightfitness's Recomended Routine™. """

from flask import Flask, flash, redirect, render_template, request
from numpy import array_split
# TODO: import time

app = Flask(__name__)

# FIXME What is 'SECRET_KEY' and how do I properly implement it?
app.config['SECRET_KEY'] = "secret"


class Routine:
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
            if item == "Deadbugs":  # FIXME
                self.instructions.append("30 seconds of "+item)
            else:
                self.instructions.append("8 reps of "+item)

        # Advanced warm-ups
        if self.level > 1:
            for item in self.advanced_warmups:
                if item == "Parallel Bar Support Hold":  # FIXME
                    self.instructions.append("30 seconds of "+item)
                else:
                    self.instructions.append("8 reps of "+item)

        # Main strength training circuit
        self.instructions.append("\nHere we go! Do your best!")
        pairs = array_split(self.circuit, 3)
        for i in range(len(pairs)):
            self.instructions.append("Pair "+str(i+1))
            for j in range(3):
                self.instructions.append("Set "+str(j+1))
                for item in pairs[i]:
                    if item == "Parallel Bar Support Hold":  # FIXME
                        self.instructions.append("60 seconds of "+item)
                    else:
                        self.instructions.append("8 reps of "+item)
                    self.instructions.append("Rest for 90 seconds")

        # Core training circuit
        self.instructions.append("\Last part: core!")
        for i in range(3):
            for item in self.core:
                self.instructions.append("8 reps of "+item)
                self.instructions.append("Rest for 60 seconds")

        return self.instructions


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
        exercises = routine.generate_instructions()

        # TODO: Use timer to record workout duration
        # TODO: Show exercises one at a time by scrolling down
        # TODO: Go back to previous by scrolling up

        return render_template("workout.html", exercises=exercises)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("setup.html")


@ app.route("/about")
def about():
    return render_template("about.html")


# TODO: Register, log-in, and workout history feature
# TODO: Illustrations/guides for exercises
