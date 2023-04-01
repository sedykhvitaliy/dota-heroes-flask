"""add usermixin

Revision ID: 7622bd879a5a
Revises: 4cd059f2883c
Create Date: 2023-04-01 15:29:55.983161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7622bd879a5a'
down_revision = '4cd059f2883c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'db_users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'db_users', type_='unique')
    # ### end Alembic commands ###