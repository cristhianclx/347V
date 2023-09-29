"""empty message

Revision ID: 6e7adfc615b3
Revises: a385dbb44628
Create Date: 2023-09-28 20:24:47.842572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e7adfc615b3'
down_revision = 'a385dbb44628'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('content')

    # ### end Alembic commands ###
