"""empty message

Revision ID: a9e218d65f0b
Revises: 8667e9012d22
Create Date: 2018-06-04 23:19:22.364571

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a9e218d65f0b'
down_revision = '8667e9012d22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('f_backup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('show_name', sa.String(length=500), nullable=True),
    sa.Column('file_name', sa.String(length=500), nullable=True),
    sa.Column('file_size', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('is_trash', sa.INTEGER(), nullable=True),
    sa.Column('is_share', sa.INTEGER(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('f_backup')
    # ### end Alembic commands ###
