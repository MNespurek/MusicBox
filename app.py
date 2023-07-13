from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'music_Box'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@:5432/db_music_box'
db = SQLAlchemy(app)

class Zanr(db.Model):
    id_typ_zanr = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nazev = db.Column(db.String, nullable = False)

class Album(db.Model):
    id_album = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_typ_zanr = db.Column(db.Integer, db.ForeignKey('zanr.id_typ_zanr'))

class Skladba(db.Model):
    id_skladba = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nazev = db.Column(db.String, nullable = False)
    delka = db.Column(db.Integer, nullable = False)

class Album_Skladba(db.Model):
    id_album_skladba = db.Column(db.Integer, primary_key = True, autoincrement = True)
    cislo_stopy = db.Column(db.Integer, nullable = False)
    id_album = db.Column(db.Integer, db.ForeignKey('album.id_album'))
    id_skladba = db.Column(db.Integer, db.ForeignKey('skladba.id_skladba'))

class Narodnost(db.Model):
    id_typ_narodnost = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nazev = db.Column(db.String, nullable = False)

class Interpret(db.Model):
    id_interpret = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nazev = db.Column(db.String, nullable = False)
    id_typ_narodnost = db.Column(db.Integer, db.ForeignKey('narodnost.id_typ_narodnost'))

class Album_Interpret(db.Model):
    id_album_interpret = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_album = db.Column(db.Integer, db.ForeignKey('album.id_album'))
    id_interpret = db.Column(db.Integer, db.ForeignKey('interpret.id_interpret'))

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/zanr')
def zanr():
    return render_template('zanr.html')

@app.route('/skladba')
def skladba():
    return render_template('skladba.html')

@app.route('/album')
def album():
    return render_template('album.html')

@app.route('/album_interpret')
def album_interpret():
    return render_template('album_interpret.html')

@app.route('/interpret')
def interpret():
    return render_template('interpret.html')

@app.route('/narodnost')
def narodnost():
    return render_template('narodnost.html')

@app.route('/album_skladba')
def album_skladba():
    return render_template('album_skladba.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

