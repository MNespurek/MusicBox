from flask import Flask, render_template, redirect, render_template_string, request, url_for
from markupsafe import Markup, escape
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, IntegerField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields import DateField

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

class MusicFormular(FlaskForm):

    nazev = StringField('Název', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Napiš název"})
    datum_vydani = DateField('Datum vydání', validators=[DataRequired()], format='%d-%m-%Y', render_kw={"class": "form-control"})
    cislo_stopy = IntegerField('Číslo stopy', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder" : "Napiš číslo stopy"})
    delka = TimeField('Délka', validators=[DataRequired()], render_kw={ "class": "form-control", "step": "1" })
    zanry = SelectField('Vyberte žánr', validators=[DataRequired()], render_kw={"class": "form-control"})
    alba = SelectField('Vyberte album', validators=[DataRequired()], render_kw={"class": "form-control"})
    interpreti = SelectField('Vyberte interpreta', validators=[DataRequired()], render_kw={"class": "form-control"})
    narodnosti = SelectField('Vyberte národnost', validators=[DataRequired()], render_kw={"class": "form-control"})
    skladby = SelectField('Vyberte skladbu', validators=[DataRequired()], render_kw={"class": "form-control"})
    pridat = SubmitField('Přidat', render_kw={"class": "btn btn-outline-primary"})

class Anchor:
    def __init__(self, text, endpoint, **kwargs):
        self.text = text
        self.url = url_for(endpoint, **kwargs)
   
    def render(self):
        
        anchor_html = f'<a class="nav-link" href="{self.url}">{self.text}</a>'
        return Markup(anchor_html)

class Div:
    def __init__(self, obsah, class_):
        self.obsah = obsah
        self.class_ = class_

    def render(self):
        vlastnosti = f'<div class="{self.class_}">{self.obsah}'
        print(vlastnosti)
        return Markup(vlastnosti)

class Form:
    def __init__(self, action, method):
        self.action = action
        self.method = method

    def render(self):
        vlastnosti = f'<form action="{self.action}" method="{self.method}">'
        return Markup(vlastnosti)
    
class Img:
    def __init__(self, src, alt='', class_=None, width = None, height = None):
        self.src = src
        self.class_=class_
        self.alt = alt
        self.width = width
        self.height = height

    def render(self):
        obrazek = f'<img src="{self.src}" alt="{self.alt}" class="{self.class_}" width="{self.width}" height="{self.height}>'
        print (self.class_)
        return Markup(obrazek)

class Nav:
    def __init__(self, class_, style):
        self.class_ = class_
        self.style = style

    def render(self):
        nav = f'<nav class="{self.class_}" style="{self.style}">'
        print(nav)
        return Markup(nav)

class Ul:
    def __init__(self, class_):
        self.class_ = class_
    
    def render(self):
        ul = f'<ul class="{self.class_}">'
        return Markup(ul)
    
class Li:
    def __init__(self, class_):
        self.class_ = class_
    
    def render(self):
        li = f'<li class="{self.class_}">'
        return Markup(li)


@app.route('/')
def index():
    link_zanr = Anchor('Žánr', 'zanr')
    div_container = Div('', "container text-center")
    div_row = Div('', "row")
    div_center = Div('', "center")
    obrazek = Img(src='static/obrazky/music.webp', alt='Music', class_= "center", width=500, height=500)
    nav = Nav(class_= "navbar", style="background-color: rgb(196, 199, 201);")
    ul = Ul(class_="nav nav-tabs")
    li = Ul(class_="nav-item")
    return render_template('index.html', div_center = div_center, link_zanr = link_zanr, div_container = div_container, div_row = div_row, nav=nav, obrazek = obrazek, ul = ul, li = li) 

@app.route('/zanr')
def zanr():
    formular = MusicFormular()
    return render_template('zanr.html', formular = formular)

@app.route('/pridej_zanr', methods = ['POST'])
def pridej_zanr():
    formular = MusicFormular()
    zanr = Zanr(nazev = formular.nazev.data)
    db.session.add(zanr)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/skladba')
def skladba():
    formular = MusicFormular()
    print(url_for('skladba'))
    return render_template('skladba.html', formular = formular)

@app.route('/pridej_skladbu', methods = ['POST'])
def pridej_skladbu():
    formular = MusicFormular()
    if formular.validate_on_submit():
        skladba = Skladba(nazev = formular.nazev.data, delka = formular.delka.data)
        db.session.add(skladba)
        db.session.commit()
    return redirect('/ulozit')

@app.route('/album')
def album():
    formular = MusicFormular()
    form = Form(action="/pridej_album", method="POST")
    zanry = Zanr.query.all()
    seznam_zanry = []
    for zanr in zanry:
        choice = (zanr.id_typ_zanr, zanr.nazev)
        seznam_zanry.append(choice)
    formular.zanry.choices = seznam_zanry
    return render_template('album.html', zanry = zanry, formular = formular, form = form)

@app.route('/pridej_album', methods = ['POST'])
def pridej_album():
    formular = MusicFormular()
    if formular.validate_on_submit():
        album = Album(id_typ_zanr = formular.zanry.data, nazev = formular.nazev.data, datum_vydani = formular.datum_vydani.data)
    db.session.add(album)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/album_skladba')
def album_skladba():
    formular = MusicFormular()
    alba = Album.query.all()
    seznam_alba = []
    for album in alba:
        choice = (album.id_album, album.nazev)
        seznam_alba.append(choice)

    formular = MusicFormular()
    skladby = Skladba.query.all()
    seznam_skladby = []
    for skladba in skladby:
        choice = (skladba.id_skladba, skladba.nazev)
        seznam_skladby.append(choice)

    formular.alba.choices = seznam_alba
    formular.skladby.choices = seznam_skladby
    
    return render_template('album_skladba.html', alba = alba, skladby = skladby, formular = formular)

@app.route('/pridej_album_skladbu', methods = ['POST'])
def pridej_album_skladbu():
    formular = MusicFormular()
    album_skladba = Album_Skladba(cislo_stopy = formular.cislo_stopy.data, id_album = formular.alba.data, id_skladba = formular.skladby.data)
    db.session.add(album_skladba)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/album_interpret')
def album_interpret():
    formular = MusicFormular()
    alba = Album.query.all()
    seznam_alba = []
    for album in alba:
        choice = (album.id_album, album.nazev)
        seznam_alba.append(choice)
    formular.alba.choices = seznam_alba
    interpreti = Interpret.query.all()
    seznam_interpreti = []
    for interpret in interpreti:
        choice = (interpret.id_interpret, interpret.nazev)
        seznam_interpreti.append(choice)
    formular.interpreti.choices = seznam_interpreti
    return render_template('album_interpret.html', alba = alba, interpreti = interpreti, formular = formular)

@app.route('/pridej_album_interpret', methods = ['POST'])
def pridej_album_interpret():
    formular = MusicFormular()
    if formular.validate_on_submit():
        album_interpret = Album_Interpret(id_album = formular.alba.data, id_interpret = formular.interpreti.data)
    db.session.add(album_interpret)
    db.session.commit()
    return redirect('/ulozit')

@app.route('/interpret')
def interpret():
    formular = MusicFormular()
    narodnosti = Narodnost.query.all()
    seznam_narodnosti = []
    for narodnost in narodnosti:
        choice = (narodnost.id_typ_narodnost, narodnost.nazev)
        seznam_narodnosti.append(choice)
    formular.narodnosti.choices = seznam_narodnosti
    return render_template('interpret.html', formular = formular, narodnosti = narodnosti)

@app.route('/pridej_interpreta', methods = ['POST'])
def pridej_interpreta():
    formular = MusicFormular()
    if formular.validate_on_submit():
        interpret = Interpret(id_typ_narodnost = formular.narodnosti.data, nazev = formular.nazev.data)
    db.session.add(interpret)
    db.session.commit()
    return redirect('/ulozit')


@app.route('/narodnost')
def narodnost():
    formular = MusicFormular()
    return render_template('narodnost.html', formular = formular)

@app.route('/pridej_narodnost', methods = ['POST'])
def pridej_narodnost():
    print("volána fce pridej_zanr")
    formular = MusicFormular()
    narodnost = Narodnost(nazev = formular.nazev.data)
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

