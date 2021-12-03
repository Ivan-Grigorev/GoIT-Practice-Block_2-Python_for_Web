from flask import render_template, flash, redirect, url_for
from Module_11.lesson_m11_1.notes import app, db
from Module_11.lesson_m11_1.notes.forms import LoginForm, RegistrationForm, NoteForm
from Module_11.lesson_m11_1.notes.models import User, Note
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = NoteForm()
    if form.validate_on_submit():
        post = Note(body=form.note.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    notes = Note.query.filter_by(author=current_user).all()
    return render_template("index.html", title='Home Page', form=form,
                           notes=notes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/index/<int:note_id>")
def note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', note=note)


@app.route("/index/<int:note_id>/delete", methods=['POST', 'GET'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))