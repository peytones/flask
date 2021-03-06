"""second migration

Revision ID: 25299e90154
Revises: 5011715801b1
Create Date: 2014-12-31 01:35:32.589187

"""

# revision identifiers, used by Alembic.
revision = '25299e90154'
down_revision = '5011715801b1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    ### end Alembic commands ###
