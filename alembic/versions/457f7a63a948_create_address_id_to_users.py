"""create address_id to users

Revision ID: 457f7a63a948
Revises: 28423388494f
Create Date: 2023-03-12 15:46:50.405367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '457f7a63a948'
down_revision = '28423388494f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address',
                          local_cols=['address_id'], remote_cols=['id'], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_constraint('users', 'address_id')