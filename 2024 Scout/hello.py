import os, sys, click, urilib
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

DATABASE_HOST ="" #TODO replace
DATABASE_NAME =""
DATABASE_USERNAME = ""
DATABASE_PASSWORD = ""

app = Flask(__name__)
db = SQLAlchemy(app)
with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))
        print('\n\n--------Connection successful !')
    except Exception as e:
        print('\n\n--------- Connection failed ! ERROR : ', e)
class Test(db.Model):
    __tablename__ = 't_test'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    applicationnumber = db.Column(db.String(15))
    source = db.Column(db.String(50))
    def __init__(self, applicationnumber, source):
        self.applicationnumber = applicationnumber
        self.source = source
        print("Executed __init__ !")
@app.route('/api/test', methods = ['POST'])
def insert():
    try:
        applicationnumber = request.json['applicationnumber']
        source = request.json['source']
        try:
            t_test_obj = Test(applicationnumber, source)
            db.session.add(t_test_obj)
            db.session.commit()
            print("\nRow commited -------")
        except Exception as e:
            error = f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}, file : {os.path.basename(__file__)}"
            click.secho(error, fg="red")
            return jsonify({"status": "failure", "message": f"{error}"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "failure", "message": str(e)}), 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

            