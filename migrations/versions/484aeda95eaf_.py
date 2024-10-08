"""empty message

Revision ID: 484aeda95eaf
Revises: 0e51c0be31c7
Create Date: 2023-12-01 07:19:39.816222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '484aeda95eaf'
down_revision = '0e51c0be31c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prompt_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('response_prompt_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'prompt', ['prompt_id'], ['id'])
        batch_op.drop_column('prompt')

    with op.batch_alter_table('sample', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('response_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('sample_response_fkey', type_='foreignkey')
        batch_op.drop_constraint('sample_question_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'response', ['response_id'], ['id'])
        batch_op.create_foreign_key(None, 'question', ['question_id'], ['id'])
        batch_op.drop_column('response')
        batch_op.drop_column('question')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sample', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('response', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('sample_question_fkey', 'question', ['question'], ['id'])
        batch_op.create_foreign_key('sample_response_fkey', 'response', ['response'], ['id'])
        batch_op.drop_column('response_id')
        batch_op.drop_column('question_id')

    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prompt', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('response_prompt_fkey', 'prompt', ['prompt'], ['id'])
        batch_op.drop_column('prompt_id')

    # ### end Alembic commands ###
