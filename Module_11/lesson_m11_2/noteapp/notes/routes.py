
from flask import render_template, flash, url_for, redirect, abort, request
from noteapp import db, mail
from flask_login import login_required, current_user
from noteapp.notes.forms import NoteForm
from noteapp.models import Note
from noteapp.notes import note_bp
from flask_mail import Message


@note_bp.route('/')
def about():
    return render_template('about.html')


@note_bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = NoteForm()
    if form.validate_on_submit():
        post = Note(body=form.note.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('You have a new note')
        return redirect(url_for('notes.index'))
    notes = Note.query.filter_by(author=current_user).all()
    return render_template('index.html', title="home page", form=form, notes=notes)


@note_bp.route('/index/<int:note_id>', methods=['GET', 'POST'])
@login_required
def note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', note=note)


@note_bp.route("/index/<int:note_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('notes.index'))


@note_bp.route("/index/<int:note_id>/update", methods=['GET', 'POST'])
@login_required
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    form = NoteForm()
    if form.validate_on_submit():
        note.body = form.note.data
        db.session.commit()
        flash('Your note has been updated!', 'success')
        return redirect(url_for('notes.note', note_id=note.id))
    elif request.method == 'GET':
        form.note.data = note.body
    return render_template('index.html',form=form)


@note_bp.route("/index/<int:note_id>/email", methods=['GET', 'POST'])
@login_required
def send_email(note_id):
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    msg = Message('Note!',
                  recipients=[current_user.email],
                  body=str(note))

    mail.send(msg)
    flash('Your note has been send!', 'success')
    return render_template('email.html')


