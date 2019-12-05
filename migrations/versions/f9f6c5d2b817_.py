"""empty message

Revision ID: f9f6c5d2b817
Revises: e40657bfa333
Create Date: 2019-12-04 14:31:17.717714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f6c5d2b817'
down_revision = 'e40657bfa333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('trial', sa.String(length=75), nullable=True))
    op.drop_constraint('test_sample_key', 'test', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('test_sample_key', 'test', ['sample'])
    op.drop_column('test', 'trial')
    # ### end Alembic commands ###
