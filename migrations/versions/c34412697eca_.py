"""empty message

Revision ID: c34412697eca
Revises: 99ff344ce92f
Create Date: 2023-12-01 03:31:51.062633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c34412697eca'
down_revision = '99ff344ce92f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.alter_column('prompt',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.alter_column('prompt',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
