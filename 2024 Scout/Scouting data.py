import pymssql, logging, os
from flask import Flask, render_template, make_response, request
from pymssql import _mssql
server = "ec2-44-229-180-148.us-west-2.compute.amazonaws.com"
user = "Team753CGI"
password = "svRBLWC7s2UCBczXuc9p"
database = "2023Scout"
as_dict = True

log = logging.getLogger('')
app = Flask(__name__)
@app.route("/", methods=['GET'])
def choose():
    return render_template("index.html")
def setcookie():
    resp = make_response("Setting the cookie")
    resp.set_cookie('scenario', 'scenario1')
    return resp
#render_template()
@app.route("/cookieresult", methods=["POST"])
def start():
    if request.method == "POST":
        scenario = request.form['scenarios']
        #x = {'date':[u'2012-06-28', u'2012-06-29', u'2012-06-30'], 'users': [405, 368, 119], 'name':[1,2,3]}
        with _mssql.connect(server, user, password, database) as conn:
            with conn.cursor(as_dict=True) as cursor:
                output = cursor.callproc('dbo.Next3Matches')
            #return("Hi!")
            return(output)
    return render_template("ranking.html", scenario=scenario)
def test():
    scenario = request.form['scenarios']
    screen = render_template("index.html")
    return screen
@app.route("/ranking/<scenario>")
def table(scenario):
    return render_template("ranking.html", scenario=scenario)
'''
def GetScores(scenario):
    try:
        log.info("Attempting to use scenario "+scenario)
        with pymssql.connect(server, user, password, database) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.callproc('dbo.scenarioRanking', scenario)
            conn.commit()
            log.info("Site loaded")
            output=""
            return (output)
    except Exception as e:
        log.error('Error: ' + str(e.args))
        return('Error: ' + str(e.args))
'''
if __name__=="__main__":
    app.run(debug=True)