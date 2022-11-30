from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:/flask_assgn/sqlite3.db'
app.config['SQLALCHEMY_BINDS'] = {'two' : 'mysql+pymysql://root:Rahul123@localhost/flask_two',
                                 'three' : 'postgresql://postgres:Rahul123@localhost/flask_three'}                             


db = SQLAlchemy(app)

class Emp(db.Model):
   id = db.Column('emp_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))

   def __init__(self, id, name, city):
      self.id = id
      self.name = name
      self.city = city
   

class Emp_two(db.Model):
   __bind_key__ = 'two'
   id = db.Column('emp_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))

   def __init__(self, id, name, city):
      self.id = id
      self.name = name
      self.city = city

class Emp_three(db.Model):
   __bind_key__ = 'three'
   id = db.Column('emp_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))

   def __init__(self, id, name, city):
      self.id = id
      self.name = name
      self.city = city
   

   
# e1 = Emp(1, "Rahul_sqlite3","Bhopal")
# e2 = Emp_two(1, "Rahul_mysql", "Bhopal")
# e3 = Emp_three(1, "Rahul_postgres", "Bhopal")



@app.route('/PostgreSQL/')
def call_postgre():
   emps = Emp_three.query.all()
   return render_template("postgres.html", content=emps)



@app.route('/MySQL/')
def call_sql():
   emps = Emp_two.query.all()
   return render_template("mysql.html", content=emps)





"""
with app.app_context():
   if __name__ == '__main__':

      "" for creating the tables in the respective databases ""
      # db.create_all()

      "" for adding the data into the database ""
      # db.session.add(e3)
      # db.session.commit()
"""


with app.app_context():
   if __name__ == '__main__':
      app.run(debug = True)

