"""empty message

Revision ID: adb67757f288
Revises: e6af78c67c28
Create Date: 2018-05-13 12:07:02.280973

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'adb67757f288'
down_revision = 'e6af78c67c28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s_user', sa.Column('username', sa.String(length=16), nullable=True))
    op.drop_column('s_user', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('s_user', sa.Column('user', mysql.VARCHAR(length=16), nullable=True))
    op.drop_column('s_user', 'username')
    # ### end Alembic commands ###
