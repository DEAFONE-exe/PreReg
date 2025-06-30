from application import app, db
from application.models import LogEntry, Visitor
from datetime import datetime
from application.forms import LoginForm
from flask import render_template, request, flash, json, jsonify, redirect, url_for

@app.route('/')
def index():
    loginform = LoginForm()
    return render_template('login.html', form=loginform, title="Authentication")

@app.route('/auth', methods=['GET','POST'])
def auth():
    loginform = LoginForm()
    if request.method =='POST':
        if loginform.validate_on_submit():
            IdentificationKey = loginform.IdentificationKey.data
            Password = loginform.Password.data
            new_entry = LogEntry(
                IdentificationKey = IdentificationKey,
                Password = Password,
                authenticated_on = datetime.utcnow()
            )
            add_entry(new_entry)
            flash("Authentication Successful", "success")
        else:
            flash("Error, cannot proceed","danger")
    return redirect(url_for('prereg'))


@app.route('/reg')
def prereg():
    return render_template('pre_registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    full_name = request.form.get('full_name')
    contact_number = request.form.get('contact_number')
    email = request.form.get('email')
    company = request.form.get('company')
    purpose = request.form.get('purpose')
    host = request.form.get('host')
    visit_date = request.form.get('visit_date')
    visit_time = request.form.get('visit_time')
    id_type = request.form.get('id_type')
    id_number = request.form.get('id_number')

    # Simple validation
    if not full_name or not contact_number or not email or not visit_date:
        flash('Please fill in all required fields (Name, Contact, Email, Visit Date)')
        return redirect(url_for('prereg'))

    # Create Visitor object
    visitor = Visitor(
        full_name=full_name,
        contact_number=contact_number,
        email=email,
        company=company,
        purpose=purpose,
        host=host,
        visit_date=visit_date,
        visit_time=visit_time,
        id_type=id_type,
        id_number=id_number
    )

    # Save to DB
    db.session.add(visitor)
    db.session.commit()

    flash('Pre-registration successful! Your visit details have been saved.')
    return redirect(url_for('hello_world'))

@app.route('/hello')
def hello_world():
    return "<h1>Hello World</h1>"


# Optional: show all visitors (for testing)
@app.route('/visitors')
def visitors():
    all_visitors = Visitor.query.all()
    return render_template('visitors.html', visitors=all_visitors)


def add_entry(new_entry):
    try:
        db.session.add(new_entry)
        db.session.commit()
        return new_entry.id
    except Exception as error:
        db.session.rollback()
        flash(error,"danger")