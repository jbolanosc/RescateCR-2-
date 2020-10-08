"""empty message

Revision ID: dd7a178d2da0
Revises: 
Create Date: 2020-10-08 08:31:53.828956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd7a178d2da0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refuge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photos', sa.String(), nullable=True),
    sa.Column('refuge', sa.Integer(), nullable=True),
    sa.Column('adopted', sa.Boolean(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('animal_type', sa.String(), nullable=True),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ),
    sa.ForeignKeyConstraint(['refuge'], ['refuge.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('refuge', sa.Integer(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['refuge'], ['refuge.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fav_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('animal', sa.Integer(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_list')
    op.drop_table('employee')
    op.drop_table('Animals')
    op.drop_table('user')
    op.drop_table('refuge')
    # ### end Alembic commands ###