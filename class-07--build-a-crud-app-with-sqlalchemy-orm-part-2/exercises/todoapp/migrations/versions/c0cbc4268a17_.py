"""empty message

Revision ID: c0cbc4268a17
Revises: 3a63c07bab63
Create Date: 2019-12-01 14:15:28.027803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0cbc4268a17'
down_revision = '3a63c07bab63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###