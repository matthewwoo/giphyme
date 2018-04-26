"""empty message

Revision ID: 4a10f32cb198
Revises: 47c35baa13ff
Create Date: 2018-04-27 07:29:43.201439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a10f32cb198'
down_revision = '47c35baa13ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gif', sa.Column('filename', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gif', 'filename')
    # ### end Alembic commands ###
