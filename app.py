# app.py (Flask backend)

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

# In-memory store for demo (replace with DB)
visitor_registrations = []

@app.route('/')
def index():
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

    visitor = {
        'full_name': full_name,
        'contact_number': contact_number,
        'email': email,
        'company': company,
        'purpose': purpose,
        'host': host,
        'visit_date': visit_date,
        'visit_time': visit_time,
        'id_type': id_type,
        'id_number': id_number
    }

    visitor_registrations.append(visitor)

    flash('Pre-registration successful! We have recorded your visit details.')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
