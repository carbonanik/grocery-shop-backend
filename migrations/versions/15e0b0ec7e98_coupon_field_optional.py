"""coupon field optional

Revision ID: 15e0b0ec7e98
Revises: 5b12825413a3
Create Date: 2023-03-17 17:56:38.422384

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '15e0b0ec7e98'
down_revision = '5b12825413a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('coupon', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('coupon', 'code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('coupon', 'discount',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.drop_index('ix_coupon_title', table_name='coupon')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_coupon_title', 'coupon', ['title'], unique=False)
    op.alter_column('coupon', 'discount',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('coupon', 'code',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('coupon', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###