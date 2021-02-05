from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    upload_timestamp = db.Column(db.TIMESTAMP, nullable=False)
    patient_id = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    fhir_data = db.Column(db.Text)
    cypher_mutation = db.Column(db.String(255))
