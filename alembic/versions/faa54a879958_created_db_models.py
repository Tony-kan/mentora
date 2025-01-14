"""created db models

Revision ID: faa54a879958
Revises: 
Create Date: 2024-10-05 22:49:17.798360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'faa54a879958'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('journal_entries',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('entry_date', sa.Date(), nullable=False),
    sa.Column('most_important_task', sa.String(), nullable=False),
    sa.Column('grateful_things', sa.String(), nullable=False),
    sa.Column('overall_day_rating', sa.Enum('awful', 'bad', 'ok', 'good', 'great', name='moodrating'), nullable=False),
    sa.Column('overall_mood_rating', sa.Enum('awful', 'bad', 'ok', 'good', 'great', name='moodrating'), nullable=False),
    sa.Column('completed_most_important_task', sa.Boolean(), nullable=False),
    sa.Column('day_summary', sa.String(), nullable=False),
    sa.Column('mood_tags', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journal_entries')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
