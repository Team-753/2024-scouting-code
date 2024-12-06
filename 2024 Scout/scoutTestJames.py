# Imports
import logging
from os import getenv
import pymssql
from flask import Flask, render_template, make_response, request


#Setup Logging
logFilename=r"C:\dev\Scouting.Team753.org\scoutTest.log"
log = logging.getLogger('')
log.setLevel(logging.DEBUG)
#log.setLevel(logging.INFO)
format = logging.Formatter("%(asctime)s: %(levelname)s:%(message)s")

#Setup console handler to see logging on console
##ch = logging.StreamHandler(sys.stdout)
##ch.setFormatter(format)
##log.addHandler(ch)
#Setup file handler for logging to file at same time.
fh = logging.FileHandler(logFilename)
fh.setFormatter(format)
log.addHandler(fh)

# DB setup
server = "ec2-44-229-180-148.us-west-2.compute.amazonaws.com"
user = "Team753CGI"
password = "svRBLWC7s2UCBczXuc9p"
database = "2023Scout"

# Flask setup
app = Flask(__name__)

# Page
@app.route("/", methods=["GET"])
def start():
    #return("Hello World!")
    return render_template("index.html")


@app.route("/getScenario", methods=["GET"])
def getData():
    return render_template("scenarioHome.html")
def setcookie():
    resp = make_response("Setting the cookie")
    resp.set_cookie("scenario", "scenario1")
    return resp


@app.route("/ranking", methods = ["GET", "POST"])
def test():
    if request.method == "POST":
        scenario= request.form["scenarios"]
    conn = pymssql.connect(server, user, password, database)
    cursor = conn.cursor()
    cursor.callproc("dbo.ScenarioRanking", (scenario,))
    teamList = []
    pointList = []
    for row in cursor:
        print('row = %r' % (row,))
        teamList.append(row[1])
        pointList.append(row[2])
    conn.close()
    return render_template("ranking.html", scenario = scenario, team1 = teamList[0], points1 = pointList[0], team2 = teamList[1], points2 = pointList[1], team3 = teamList[2], points3 = pointList[2],team4 = teamList[3], points4 = pointList[3], team5 = teamList[4], points5 = pointList[4], team6 = teamList[5], points6 = pointList[5], team7 = teamList[6], points7 = pointList[6], team8 = teamList[7], points8 = pointList[7], team9 = teamList[8], points9 = pointList[8], team10 = teamList[9], points10 = pointList[9], team11 = teamList[10], points11 = pointList[10], team12 = teamList[11], points12 = pointList[11], team13 = teamList[12], points13 = pointList[12], team14 = teamList[13], points14 = pointList[13], team15 = teamList[14], points15 = pointList[14], team16 = teamList[15], points16 = pointList[15], team17 = teamList[16], points17 = pointList[16], team18 = teamList[17], points18 = pointList[17], team19 = teamList[18], points19 = pointList[18], team20 = teamList[19], points20 = pointList[19], team21 = teamList[20], points21 = pointList[20], team22 = teamList[21], points22 = pointList[21], team23 = teamList[22], points23 = pointList[22], team24 = teamList[23], points24 = pointList[23], team25 = teamList[24], points25 = pointList[24])


@app.route("/matches", methods=["GET", "POST"])
def matchTable():
    return render_template("chooseMatch.html")


@app.route("/humanScout/<alliance1>/<matchteam1>/<match1>", methods=["GET"])
def humanScoutStart(alliance1, matchteam1, match1):
    return render_template("humanScouting.html", team = 753, match = match1, alliance = alliance1, matchteam = matchteam1)


@app.route("/postH", methods=["GET", "POST"])
def setHumanPost():
    if request.method =="POST":
        match = request.form["match"]
        team = request.form["team"]
        ring1 = request.form["ring1"]
        thro1 = request.form["thro1"]
        ring2 = request.form["ring2"]
        thro2 = request.form["thro2"]
        ring3 = request.form["ring3"]
        thro3 = request.form["thro3"]
        notes = request.form["notes"]
        time = None
        conn = pymssql.connect(server, user, password, database)
        cursor = conn.cursor()
        cursor.callproc("[dbo].[addHumanData]", (team, match, ring1, thro1, ring2, thro2, ring3, thro3, notes, time, ))
        conn.commit()
        conn.close()
    return render_template("postM.html")


@app.route("/matchScout", methods=["GET", "POST"])
def matchStart():
    if request.method == "POST":
        team = int(request.form["teamNo"])
        print(team)
        match = int(request.form["matchNo"])
        print(match)
        rawAlliance = request.form["alliance"]
        color = rawAlliance.split()
        alliance = color[0]
        print(color)
        number = int(color[1])
    return render_template("matchScouting.html", team=team, match = match, alliance = alliance, matchteam = number)
def matchSet():
    resp = make_response("Setting the cookie")
    resp.set_cookie("matchR", "matchR")
    return resp


@app.route("/postM", methods=["GET", "POST"])
def setMatchPost():
    global leave1, spotlit1, harmony1
    leave1 = 0
    spotlit1 = 0
    harmony1 = 0
    if request.method == "POST":
        if("leave" in request.form):
            leave = request.form["leave"]
        else:
            leave = False
        print("Test")
        print(leave)
        ampAuto = int(request.form["ampAuto"])
        speakerAuto = int(request.form["sAuto"])
        amp = int(request.form["amp"])
        nAmpS = int(request.form["nAmp"])
        sAmp = int(request.form["sAmp"])
        trap = int(request.form["t"])
        stage = request.form["stage"]
        park = None
        onstage = None
        if(stage=="park"):
            park = "True"
            onstage = "False"
        elif(stage == "onstage"):
            onstage = "True"
            park = "False"
        else:
            park = "False"
            onstage = "False"
        if("spotlit" in request.form):
            spotlit = request.form["spotlit"]
        else:
            spotlit = 0
        if("harmony" in request.form):
            harmony = request.form["harmony"]
        else:
            harmony = 0
        robots = str(request.form["robots"])
        order = str(request.form["order"])
        team = str(request.form["team"])
        match = str(request.form["match"])
        time = None
        conn = pymssql.connect(server, user, password, database)
        cursor = conn.cursor()
        print(leave, ampAuto, speakerAuto, amp, nAmpS, sAmp, trap, park, onstage, spotlit, harmony, robots, order, team, match, time)
        cursor.callproc("dbo.addMatchData", (leave, ampAuto, speakerAuto, amp, nAmpS, sAmp, trap, park, onstage, spotlit, harmony, robots, order, team, match, time, ))
        conn.commit()
        conn.close()
    return render_template("postM.html")


if __name__ == "__main__":
    log.debug("Starting.....")
    #app.run()
    app.run(debug=True)
