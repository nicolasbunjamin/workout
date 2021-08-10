from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)


class Exercise:

    stretches = ("Yuri's Shoulder Band Warmup",
                 "Squat Sky Reaches",
                 "GMB Wrist Prep",
                 "Deadbugs")
    warmups = ("Arch Hangs",
               "Parallel Bar Support Hold",
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
    core = ("Ring Ab Rollouts",
            "Banded Pallof Presses",
            "Reverse Hyperextension")

    def __init__(self, level):
        """ Set difficulty level on a scale of 0 to 4 """
        self.level = level

        """ Generate today's exercise plan """
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

        # Start workout

        return redirect("workout.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/setup")


@ app.route("/about")
def setup():
    return render_template("about.html")
