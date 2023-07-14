from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'music_Box'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@:5432/db_music_box'
db = SQLAlchemy(app)
session = Session()
class Zanr(db.Model):
    id_typ_zanr = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nazev = db.Column(db.String, nullable = False)
    
class Album(db.Model):
    id_album = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_typ_zanr = db.Column(db.Integer, db.ForeignKey('zanr.id_typ_zanr'))
    nazev = db.Column(db.String, nullable = False)
    datum_vydani = db.Column(db.DateTime, nullable = False)

class Skladba(db.Model):
    id_skladba = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nazev = db.Column(db.String, nullable = False)
    delka = db.Column(db.Time, nullable = False)

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

@app.route('/pridej_zanr', methods = ['POST'])
def pridej_zanr():
    print("volána fce pridej_zanr")
    nazev = request.form['nazev']
    zanr = Zanr(nazev = nazev)
    db.session.add(zanr)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/skladba')
def skladba():
    return render_template('skladba.html')

@app.route('/pridej_skladbu', methods = ['POST'])
def pridej_skladbu():
    print("volána fce pridej_skladbu")
    nazev = request.form['nazev']
    delka = request.form['delka']
    skladba = Skladba(nazev = nazev, delka = delka)
    db.session.add(skladba)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/album')
def album():
    zanry = Zanr.query.all()
    return render_template('album.html', zanry = zanry)

@app.route('/pridej_album', methods = ['POST'])
def pridej_album():
    id_typ_zanr = request.form['id_typ_zanr']
    nazev = request.form['nazev']
    datum_vydani = request.form['datum_vydani']
    album = Album(id_typ_zanr = id_typ_zanr, nazev = nazev, datum_vydani = datum_vydani)
    db.session.add(album)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/album_skladba')
def album_skladba():
    alba = Album.query.all()
    skladby = Skladba.query.all()
    return render_template('album_skladba.html', alba = alba, skladby = skladby)

@app.route('/pridej_album_skladbu', methods = ['POST'])
def pridej_album_skladbu():
    cislo_stopy = request.form['cislo_stopy']
    id_album = request.form['id_album']
    id_skladba = request.form['id_skladba']
    album_skladba = Album_Skladba(cislo_stopy = cislo_stopy, id_album = id_album, id_skladba = id_skladba)
    db.session.add(album_skladba)
    db.session.commit()
    return redirect('/ulozit')


@app.route('/album_interpret')
def album_interpret():
    alba = Album.query.all()
    interpreti = Interpret.query.all()
    return render_template('album_interpret.html', alba = alba, interpreti = interpreti)

@app.route('/pridej_album_interpret', methods = ['POST'])
def pridej_album_interpret():
    id_album = request.form['id_album']
    id_interpret = request.form['id_interpret']
    album_interpret = Album_Interpret(id_album = id_album, id_interpret = id_interpret)
    db.session.add(album_interpret)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/interpret')
def interpret():
    narodnosti = Narodnost.query.all()
    return render_template('interpret.html', narodnosti = narodnosti)

@app.route('/pridej_interpreta', methods = ['POST'])
def pridej_interpreta():
    nazev = request.form['nazev']
    id_typ_narodnost = request.form['id_typ_narodnost']
    interpret = Interpret(id_typ_narodnost = id_typ_narodnost, nazev = nazev)
    db.session.add(interpret)
    db.session.commit()
    return redirect('/ulozit')


@app.route('/narodnost')
def narodnost():
    return render_template('narodnost.html')

@app.route('/pridej_narodnost', methods = ['POST'])
def pridej_narodnost():
    print("volána fce pridej_zanr")
    nazev = request.form['nazev']
    narodnost = Narodnost(nazev = nazev)
    db.session.add(narodnost)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/ulozit')
def ulozit():
    return render_template('ulozit.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

