from application import db

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    IdentificationKey = db.Column(db.String)
    Password = db.Column(db.String)
    authenticated_on = db.Column(db.DateTime, nullable=False)

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