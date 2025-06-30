from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # For flash messages

# Setup SQLite DB URI (file 'visitors.db' in current folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Visitor model
class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100))
    purpose = db.Column(db.Text)
    host = db.Column(db.String(100))
    visit_date = db.Column(db.String(20), nullable=False)  # Store as string (YYYY-MM-DD)
    visit_time = db.Column(db.String(10))
    id_type = db.Column(db.String(50))
    id_number = db.Column(db.String(100))

with app.app_context():
    db.create_all()  # Create DB tables if they don't exist

@app.route('/')
def index():
    return render_template('login.html')


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
        return redirect(url_for('index'))

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


if __name__ == '__main__':
    app.run(debug=True)
