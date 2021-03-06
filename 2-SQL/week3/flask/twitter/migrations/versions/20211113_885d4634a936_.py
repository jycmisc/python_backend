"""empty message

Revision ID: 885d4634a936
Revises: c3b471dc6d3e
Create Date: 2021-11-13 11:35:33.501480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '885d4634a936'
down_revision = 'c3b471dc6d3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['tweet_id'], ['tweets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###
