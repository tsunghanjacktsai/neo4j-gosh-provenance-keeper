"""empty message

Revision ID: 9896e5b4eca4
Revises: 3b26029bcbc4
Create Date: 2021-02-06 19:07:21.594985

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9896e5b4eca4'
down_revision = '3b26029bcbc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('patient_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('upload_time', sa.TIMESTAMP(), nullable=False),
    sa.Column('log_storage_time', sa.TIMESTAMP(), nullable=False),
    sa.Column('patient_name', sa.String(length=255), nullable=False),
    sa.Column('cypher_mutation', sa.Text(), nullable=False),
    sa.Column('fhir_data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('patient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient')
    # ### end Alembic commands ###
