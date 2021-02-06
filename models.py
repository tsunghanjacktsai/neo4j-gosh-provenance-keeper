import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON, UUID

db = SQLAlchemy()


class PatientModel(db.Model):
    """
    Patient Model
    """

    __tablename__ = 'patients'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    patient_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False, unique=True)
    upload_time = db.Column(db.TIMESTAMP, nullable=False)
    log_storage_time = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now().isoformat())
    patient_name = db.Column(db.String(255), nullable=False)
    cypher_mutation = db.Column(db.Text, nullable=False)
    fhir_data = db.Column(JSON)
