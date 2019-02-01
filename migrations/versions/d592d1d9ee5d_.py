"""empty message

Revision ID: d592d1d9ee5d
Revises: e6b6a3977bf4
Create Date: 2019-02-01 10:18:34.078923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd592d1d9ee5d'
down_revision = 'e6b6a3977bf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('memory', sa.Integer(), nullable=True))
    op.add_column('submissions', sa.Column('score', sa.Integer(), nullable=True))
    op.add_column('submissions', sa.Column('time', sa.Integer(), nullable=True))
    op.add_column('submissions', sa.Column('verdict', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submissions', 'verdict')
    op.drop_column('submissions', 'time')
    op.drop_column('submissions', 'score')
    op.drop_column('submissions', 'memory')
    # ### end Alembic commands ###