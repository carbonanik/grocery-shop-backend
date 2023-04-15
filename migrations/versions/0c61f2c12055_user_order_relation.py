"""user order relation

Revision ID: 0c61f2c12055
Revises: a9cc148a2330
Create Date: 2023-03-24 17:38:57.574604

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '0c61f2c12055'
down_revision = 'a9cc148a2330'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'order', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_column('order', 'user_id')
    # ### end Alembic commands ###