"""Remove Experiment column

Revision ID: 2d0c784e3112
Revises: 8d49ca786f03
Create Date: 2023-02-04 17:58:12.962329

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '2d0c784e3112'
down_revision = '8d49ca786f03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'experiment_one')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('experiment_one', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###