"""OAuth tables should use Model (for created timestamp)

Revision ID: f7f27412d13f
Revises: 131bc6d9d550
Create Date: 2016-09-16 16:45:54.677503

"""

# revision identifiers, used by Alembic.
revision = 'f7f27412d13f'
down_revision = '131bc6d9d550'

from alembic import op
import sqlalchemy as sa
import server
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('grant', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('token', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('token', 'created')
    op.drop_column('grant', 'created')
    op.drop_column('client', 'created')
    ### end Alembic commands ###
