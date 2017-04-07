from flask import Flask, render_template, redirect, url_for, request
import os
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import sqlite3

app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'comments.db'),
    SECRET_KEY='development key'
))
Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('profile.html')

@app.route('/short_story.html')
def short_story():
    return render_template('short_story.html')

@app.route('/educational_background.html')
def educational_background():
    return render_template('educational_background.html')

@app.route('/employment_and_volunteering_activities.html')
def employment_and_volunteering_activities():
    return render_template('employment_and_volunteering_activities.html')

@app.route('/project.html')
def project():
    return render_template('projects.html')

@app.route('/skills_and_abilities.html')
def skills_and_abilities():
    return render_template('skills_and_abilities.html')


@app.route('/interests.html')
def interests():
    return render_template('interests.html')

@app.route('/contact_form.html', methods=['get', 'post'])
#def contact_form():
def view_form():

    if request.method == 'POST':
            name = request.form['name']
            comments = request.form['comments']
            return render_template('contact_form.html', name=name, comments=comments)
    else:
            return render_template('contact_form.html')


@app.route('/flask_sqlite.html')
def flask_sqlite():
    return render_template('flask_sqlite.html')

#
# @app.route('/', methods=['GET', 'post'])
# def view_form():
#     if request.method == 'POST':
#         name = request.form['name']
#         comments = request.form['comments']
#         return render_template('contact_form.html', name=name, comments=comments)
#     else:
#         return render_template('contact_form.html')
#
# @app.route('/')
# def view_form():
#     return render_template('contact_form_bootstrap.html')


class CommentForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    comments = TextAreaField('Comments', validators=[DataRequired(), Length(min=3, max=10)])
    submit = SubmitField('Submit')
#
# @app.route('/', methods=['GET', 'POST'])
# def view_form():
#     form = CommentForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         comments = form.comments.data
#         with sqlite3.connect(app.config['DATABASE']) as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO comments_table (name, comments) VALUES (?,?)", (name, comments))
#             con.commit()
#
#         return redirect(url_for('list_results'))
#     return render_template('form_wtf.html', form=form)

@app.route('/display')
def list_results():
    with sqlite3.connect(app.config['DATABASE']) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM comments_table")
        entries = cur.fetchall()
        return render_template('flask_sqlite.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
