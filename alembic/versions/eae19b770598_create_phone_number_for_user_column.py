"""create phone number for user column


Revision ID: eae19b770598
Revises: 
Create Date: 2023-03-11 22:58:35.170274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eae19b770598'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable=True))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')