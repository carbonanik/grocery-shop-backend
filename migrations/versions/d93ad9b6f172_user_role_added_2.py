"""user role added 2

Revision ID: d93ad9b6f172
Revises: 70bac43b9e52
Create Date: 2024-07-04 19:32:29.007414

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'd93ad9b6f172'
down_revision = '70bac43b9e52'
branch_labels = None
depends_on = None


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('user', sa.Column('account_type', sa.Enum('USER', 'VENDOR', 'ADMIN', name='userrole'), nullable=True))
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_column('user', 'account_type')
#     # ### end Alembic commands ###

def upgrade():
    banner_status = postgresql.ENUM('USER', 'VENDOR', 'ADMIN', name='account_type')
    banner_status.create(op.get_bind())

    op.add_column('user', sa.Column('account_type', sa.Enum('USER', 'VENDOR', 'ADMIN', name='account_type'), nullable=True))

def downgrade():
    op.drop_column('user', 'account_type')

    banner_status = postgresql.ENUM('USER', 'VENDOR', 'ADMIN', name='account_type')
    banner_status.drop(op.get_bind())