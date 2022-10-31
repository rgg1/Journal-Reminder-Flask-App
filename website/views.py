from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Entry, Reminder
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/journal', methods=['GET', 'POST'])
@login_required
def journal():
    if request.method == 'POST':
        entry = request.form.get('entry')
        if len(entry) < 1:
            flash('Entry is too short', category='error')
        else:
            new_entry = Entry(data=entry, user_id=current_user.id)
            db.session.add(new_entry)
            db.session.commit()
            flash('Entry added', category='success')
    return render_template("journal.html", user=current_user)

@views.route('/reminder', methods=['GET', 'POST'])
@login_required
def reminder():
    if request.method == 'POST':
        reminder=request.form.get('reminder')
        due=request.form.get('due')
        if len(reminder) < 1:
            flash('Reminder is too short', category='error')
        else:
            new_reminder = Reminder(duedate=due, data=reminder, user_id=current_user.id)
            db.session.add(new_reminder)
            db.session.commit()
            flash('Reminder added', category='success')
    return render_template("reminder.html", user=current_user)

@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    entry = json.loads(request.data)
    entryId = entry['entryId']
    entry = Entry.query.get(entryId)
    if entry:
        if entry.user_id == current_user.id:
            db.session.delete(entry)
            db.session.commit()
    return jsonify({})

@views.route('/delete-reminder', methods=['POST'])
def delete_reminder():
    reminder = json.loads(request.data)
    reminderId = reminder['reminderId']
    reminder = Reminder.query.get(reminderId)
    if reminder:
        if reminder.user_id == current_user.id:
            db.session.delete(reminder)
            db.session.commit()
    return jsonify({})