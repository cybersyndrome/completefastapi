"""create address table

Revision ID: 28423388494f
Revises: eae19b770598
Create Date: 2023-03-12 15:27:43.556876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28423388494f'
down_revision = 'eae19b770598' #points to last revision made
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(30), nullable=False),
                    sa.Column('address2', sa.String(30), nullable=False),
                    sa.Column('city', sa.String(30), nullable=False),
                    sa.Column('state', sa.String(30), nullable=False),
                    sa.Column('country', sa.String(30), nullable=False),
                    sa.Column('postalcode', sa.String(15), nullable=False)
                    )
def downgrade() -> None:
    op.drop_table('address')