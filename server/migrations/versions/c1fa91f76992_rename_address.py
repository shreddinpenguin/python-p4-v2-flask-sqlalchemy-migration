"""rename address

Revision ID: c1fa91f76992
Revises: 1d37be500dda
Create Date: 2023-11-15 16:19:42.004297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1fa91f76992'
down_revision = '1d37be500dda'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(), nullable=True))
        batch_op.drop_column('address')


def downgrade():
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('location')
