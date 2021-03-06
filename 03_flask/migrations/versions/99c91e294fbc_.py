"""empty message

Revision ID: 99c91e294fbc
Revises: 4c374b9f075e
Create Date: 2021-02-24 10:52:12.473423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99c91e294fbc'
down_revision = '4c374b9f075e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=12), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
